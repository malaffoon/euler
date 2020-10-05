package utils

import (
	"fmt"
	"testing"
)

func TestLCM(t *testing.T) {
	tests := []struct {
		values   []int
		expected int
	}{
		{[]int{1}, 1},
		{[]int{7}, 7},
		{[]int{1, 1, 1}, 1},
		{[]int{1, 2}, 2},
		{[]int{2, 5}, 10},
		{[]int{8, 9, 12}, 72},
		{[]int{17, 71}, 1207},
		{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 2520},
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
