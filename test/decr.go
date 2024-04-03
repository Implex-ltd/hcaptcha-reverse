package main

import (
    "crypto/aes"
    "crypto/cipher"
    "encoding/hex"
    "fmt"
)

func decryptData(keyStr, cipherTextStr string) ([]byte, error) {
    key, err := hex.DecodeString(keyStr)
    if err != nil {
        return nil, err
    }

    cipherText := []byte(cipherTextStr)

    nonceSize := aes.BlockSize
    if len(cipherText) < nonceSize {
        return nil, fmt.Errorf("cipherText too short. It should be at least %d bytes", nonceSize)
    }

    nonce := cipherText[:nonceSize]
    cipherText = cipherText[nonceSize:]

    block, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }

    gcm, err := cipher.NewGCM(block)
    if err != nil {
        return nil, err
    }

    decrypted, err := gcm.Open(nil, nonce, cipherText, nil)
    if err != nil {
        return nil, err
    }

    return decrypted, nil
}

func main() {
    key := "b78d6e3b21244ab4934795aab7bfd69c9da9d214d52d5ab4dbdf81c97d5d0aee"
    cipherText := "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"
    decrypted, err := decryptData(key, cipherText)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }

    fmt.Println("Decrypted data:", string(decrypted))
}
