package utils

import (
	"fmt"
	"reflect"
	"testing"
)

func TestPrimes(t *testing.T) {
	expected := []uint32{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
	actual := Primes(100)
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Primes(100) = %s. Expected %s", fmt.Sprint(actual), fmt.Sprint(expected))
	}
}

func TestPrimeFactors(t *testing.T) {
	tests := []struct {
		n        uint64
		expected []uint32
	}{
		{2, []uint32{2}},
		{3, []uint32{3}},
		{10, []uint32{2, 5}},
		{17, []uint32{17}},
		{13195, []uint32{5, 7, 13, 29}},
		{600851475143, []uint32{71, 839, 1471, 6857}},
	}

	for _, test := range tests {
		actual := PrimeFactors(test.n)
		if !reflect.DeepEqual(actual, test.expected) {
			t.Errorf("PrimeFactors(%d) = %s. Expected %s", test.n, fmt.Sprint(actual), fmt.Sprint(test.expected))
		}
	}
}
