package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
)

func main() {
	content, err := ioutil.ReadFile("custom.wat")
	if err != nil {
	}

	for _, match := range regexp.MustCompile(`\b5[^\s]*552\b`).FindAllString(string(content), -1) {
		fmt.Println(match)
	}
}
