package utils

import (
	"fmt"
	"reflect"
	"testing"
)

func TestCollatzSequence(t *testing.T) {
	var tests = []struct {
		n        int
		expected []int
	}{
		{1, []int{1}},
		{2, []int{2, 1}},
		{13, []int{13, 40, 20, 10, 5, 16, 8, 4, 2, 1}},
		{16, []int{16, 8, 4, 2, 1}},
	}
	for _, test := range tests {
		actual := CollatzSequence(test.n)
		if !reflect.DeepEqual(actual, test.expected) {
			t.Errorf("CollatzGenerator(%d) = %s. Expected %s", test.n, fmt.Sprint(actual), fmt.Sprint(test.expected))
		}
	}
}
