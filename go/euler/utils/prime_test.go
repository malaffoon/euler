package utils

import (
	"fmt"
	"reflect"
	"testing"
)

func TestPrimes(t *testing.T) {
	expected := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
	actual := Primes(100)
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Primes(100) = %s. Expected %s", fmt.Sprint(actual), fmt.Sprint(expected))
	}
}

func TestPrimeFactors(t *testing.T) {
	tests := []struct {
		n        int
		expected []int
	}{
		{2, []int{2}},
		{3, []int{3}},
		{10, []int{2, 5}},
		{17, []int{17}},
		{13195, []int{5, 7, 13, 29}},
		{600851475143, []int{71, 839, 1471, 6857}},
	}

	for _, test := range tests {
		actual := PrimeFactors(test.n)
		if !reflect.DeepEqual(actual, test.expected) {
			t.Errorf("PrimeFactors(%d) = %s. Expected %s", test.n, fmt.Sprint(actual), fmt.Sprint(test.expected))
		}
	}
}

func TestDivisors(t *testing.T) {
	tests := []struct {
		n        int
		expected []int
	}{
		{2, []int{1, 2}},
		{3, []int{1, 3}},
		{17, []int{1, 17}},
		{12, []int{1, 2, 3, 4, 6, 12}},
		{1350, []int{1, 2, 3, 5, 6, 9, 10, 15, 18, 25, 27, 30, 45, 50, 54, 75, 90, 135, 150, 225, 270, 450, 675, 1350}},
	}

	for _, test := range tests {
		actual := Divisors(test.n)
		if !reflect.DeepEqual(actual, test.expected) {
			t.Errorf("Divisors(%d) = %s. Expected %s", test.n, fmt.Sprint(actual), fmt.Sprint(test.expected))
		}
	}
}
