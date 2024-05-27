package main

import (
	"fmt"

	"github.com/golang-jwt/jwt/v5"
)

type JwtData struct {
	FingerprintType float64 `json:"f,omitempty"`
	Difficuly       float64 `json:"s,omitempty"`
	VmType          string  `json:"t,omitempty"`
	PowData         string  `json:"d,omitempty"`
	Location        string  `json:"l,omitempty"`
	Signature       string  `json:"i,omitempty"`
	Timestamp       float64 `json:"e,omitempty"`
	N               string  `json:"n,omitempty"`
	TimeoutValue    float64 `json:"c,omitempty"`
}

func validateClaimString(claims map[string]interface{}, key string) error {
	if value, ok := claims[key].(string); !ok || value == "" {
		return fmt.Errorf("can't parse jwt token at key %v", key)
	}
	return nil
}

func validateClaimInt(claims map[string]interface{}, key string) error {
	if value, ok := claims[key].(float64); !ok || value == 0 {
		return fmt.Errorf("can't parse jwt token at key %v", key)
	}

	return nil
}

func ValidateJwtClaims(claims map[string]interface{}) error {
	stringKeys := []string{"t", "d", "l", "i", "n"}
	intKeys := []string{"s", "e", "c"}

	for _, key := range stringKeys {
		if err := validateClaimString(claims, key); err != nil {
			return err
		}
	}

	for _, key := range intKeys {
		if err := validateClaimInt(claims, key); err != nil {
			return err
		}
	}

	return nil
}

func ParseJWT(token string) (*JwtData, error) {
	payload, _ := jwt.Parse(token, nil)

	if payload == nil {
		return nil, fmt.Errorf("failed to parse jwt")
	}

	claims := payload.Claims.(jwt.MapClaims)

	if err := ValidateJwtClaims(claims); err != nil {
		return nil, err
	}

	return &JwtData{
		FingerprintType: claims["f"].(float64),
		Difficuly:       claims["s"].(float64),
		VmType:          claims["t"].(string),
		PowData:         claims["d"].(string),
		Location:        claims["l"].(string),
		Signature:       claims["i"].(string),
		Timestamp:       claims["e"].(float64),
		N:               claims["n"].(string),
		TimeoutValue:    claims["c"].(float64),
	}, nil
}
