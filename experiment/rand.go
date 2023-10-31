package main

import (
	"fmt"
	"hash/crc32"
	"math/bits"
)

func RandHash(input []byte) (uint32, float64) {
	crc := crc32.Checksum(input, crc32.MakeTable(bits.Reverse32(79764919)))
	
	return crc, float64(crc) * 2.3283064365386963e-10
}

func main() {
	out, calc := RandHash([]byte(`webkitCancelAnimationFrame,webkitRequestAnimationFrame,chrome,fence,caches,cookieStore,ondevicemotion,ondeviceorientation,ondeviceorientationabsolute,launchQueue,sharedStorage,documentPictureInPicture,onbeforematch,getScreenDetails,openDatabase,queryLocalFonts,showDirectoryPicker,showOpenFilePicker,showSaveFilePicker,originAgentCluster,credentialless,speechSynthesis,oncontentvisibilityautostatechange,onscrollend,webkitRequestFileSystem,webkitResolveLocalFileSystemURL,Raven`))
	fmt.Println(out, calc)
}