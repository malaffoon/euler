package utils

import (
	"fmt"
	"testing"
)

func TestLCM(t *testing.T) {
	tests := []struct {
		values   []uint
		expected uint
	}{
		{[]uint{1}, 1},
		{[]uint{7}, 7},
		{[]uint{1, 1, 1}, 1},
		{[]uint{1, 2}, 2},
		{[]uint{2, 5}, 10},
		{[]uint{8, 9, 12}, 72},
		{[]uint{17, 71}, 1207},
		{[]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 2520},
	}
	for _, test := range tests {
		actual := LCM(test.values)
		if actual != test.expected {
			t.Errorf("LCD(%s) = %d. Expected %d", fmt.Sprint(test.values), actual, test.expected)
		}
	}
}

func TestBinomial(t *testing.T) {
	tests := []struct {
		n        int
		k        int
		expected int
	}{
		{1, 1, 1},
		{10, 6, 210},
	}
	for _, test := range tests {
		actual := Binomial(test.n, test.k)
		if actual != test.expected {
			t.Errorf("Binomial(%d,%d) = %d. Expected %d", test.n, test.k, actual, test.expected)
		}
	}
}
