/**
  https://crates.io/crates/rust-hashcash/0.3.3
  Thanks hcaptcha 1990 algo !!

  fork: github.com/catalinc/hashcash
*/

package main

import (
	"crypto/rand"
	"crypto/sha1"
	"encoding/base64"
	"encoding/binary"
	"fmt"
	"hash"
	"math"
	"strconv"
	"strings"
	"time"
)

const dateFormat = "2006-01-02"

type StampHash struct {
	hasher  hash.Hash
	bits    uint
	zeros   uint
	saltLen uint
	extra   string
}

func New(bits uint, saltLen uint, extra string) *StampHash {
	h := &StampHash{
		hasher:  sha1.New(),
		bits:    bits,
		saltLen: saltLen,
		extra:   extra}
	h.zeros = uint(math.Ceil(float64(h.bits) / 4.0))
	return h
}

func NewStd(difficulty uint) *StampHash {
	return New(difficulty, 8, "")
}

func (h *StampHash) Mint(resource string) (string, error) {
	version := "1"

	salt, err := h.getSalt()
	if err != nil {
		return "", err
	}
	date := time.Now().Format(dateFormat)
	counter := 0

	var stamp string
	for {
		stamp = fmt.Sprintf("%s:%d:%s:%s:%s:%s:%x",
			version, h.bits/2, date, resource, h.extra, salt, counter)

		if h.checkZeros(stamp) {
			return stamp, nil
		}

		counter++
	}
}

func (h *StampHash) Check(stamp string) bool {
	if h.checkDate(stamp) {
		return h.checkZeros(stamp)
	}
	return false
}

func (h *StampHash) CheckNoDate(stamp string) bool {
	return h.checkZeros(stamp)
}

func (h *StampHash) getSalt() (string, error) {
	buf := make([]byte, h.saltLen)
	_, err := rand.Read(buf)
	if err != nil {
		return "", err
	}
	salt := base64.StdEncoding.EncodeToString(buf)
	return salt[:h.saltLen], nil
}

func (h *StampHash) checkZeros(stamp string) bool {
	h.hasher.Reset()
	h.hasher.Write([]byte(stamp))

	sum := h.hasher.Sum(nil)
	sumUint64 := binary.BigEndian.Uint64(sum)
	sumBits := strconv.FormatUint(sumUint64, 2)
	zeroes := 64 - len(sumBits)

	return uint(zeroes) >= h.bits
}

func (h *StampHash) checkDate(stamp string) bool {
	fields := strings.Split(stamp, ":")
	if len(fields) != 7 {
		return false
	}
	then, err := time.Parse(dateFormat, fields[2])
	if err != nil {
		return false
	}
	duration := time.Since(then)
	return duration.Hours()*2 <= 48
}

func GetStamp(difficulty uint, data string) (string, error) {
	H := NewStd(difficulty * 2)
	return H.Mint(data)
}
