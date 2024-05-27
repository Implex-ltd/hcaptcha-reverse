package main

import (
	"hash/crc32"
	"math/bits"
)

func RandHash(input []byte) (uint32, float64) {
	crc := crc32.Checksum(input, crc32.MakeTable(bits.Reverse32(79764919)))
	
	return crc, float64(crc) * 2.3283064365386963e-10
}