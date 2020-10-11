package internal

import (
	"fmt"
	"reflect"
	"testing"
)

func TestIsPandigital(t *testing.T) {
	var tests = []struct {
		digits   []int
		values   []int
		expected bool
	}{
		{[]int{1, 2, 3, 4}, []int{12, 34}, true},
		{[]int{1, 2, 3, 4}, []int{12, 35}, false},
		{[]int{1, 2, 3, 4}, []int{12, 3}, false},
		{[]int{1, 2, 3, 4}, []int{12344}, false},
	}
	for _, test := range tests {
		actual := IsPandigital(test.digits, test.values...)
		if actual != test.expected {
			t.Errorf("IsPandigital(%s, %s) = %t. Expected %t", fmt.Sprint(test.digits), fmt.Sprint(test.values), actual, test.expected)
		}
	}
}

func TestVisitPermutations(t *testing.T) {
	expected := []string{"abc", "bac", "cab", "acb", "bca", "cba"}
	actual := make([]string, 0)
	VisitPermutations([]rune("abc"), func(runes []rune) bool {
		actual = append(actual, string(runes))
		return true
	})
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("VisitPermutations('abc') = %s. Expected %s", fmt.Sprint(actual), fmt.Sprint(expected))
	}
}

func TestVisitPermutationsAbort(t *testing.T) {
	count := 0
	VisitPermutations([]rune("7654321"), func(runes []rune) bool {
		if runes[0] == '7' {
			count++
			return true
		} else {
			return false
		}
	})
	// VisitPermutations is much less stable, it swaps first character right away
	if count != 1 {
		t.Errorf("VisitPermutations('7654321') abort test gave count = %d. Expected %d", count, 1)
	}
}

func TestVisitPermutations2(t *testing.T) {
	expected := []string{"abc", "acb", "bac", "bca", "cba", "cab"}
	actual := make([]string, 0)
	VisitPermutations2([]rune("abc"), func(runes []rune) bool {
		actual = append(actual, string(runes))
		return true
	})
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("VisitPermutations2('abc') = %s. Expected %s", fmt.Sprint(actual), fmt.Sprint(expected))
	}
}

func TestVisitPermutations2Abort(t *testing.T) {
	count := 0
	VisitPermutations2([]rune("7654321"), func(runes []rune) bool {
		if runes[0] == '7' {
			count++
			return true
		} else {
			return false
		}
	})
	// VisitPermutations is more stable, it works from the right
	if count != 720 {
		t.Errorf("VisitPermutations2('7654321') abort test gave count = %d. Expected %d", count, 720)
	}
}
