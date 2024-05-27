package main

import (
	"fmt"

	"github.com/shivakar/xxhash"
)

const (
	seed = uint64(5575352424011909552)
)

func HashString(content []byte) string {
	h := xxhash.NewSeedXXHash64(seed)
	defer h.Reset()

	h.Write(content)

	return fmt.Sprintf("%v", h.Uint64())
}
