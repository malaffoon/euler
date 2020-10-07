package internal

import (
	"math"
)

// A place for common functionality that doesn't qualify as general utility.

func productInt(values ...int) int {
	result := 1
	for _, value := range values {
		result *= value
	}
	return result
}

func maxInt(values ...int) int {
	maxValue := math.MinInt16
	for _, value := range values {
		if value > maxValue {
			maxValue = value
		}
	}
	return maxValue
}

func minInt(values ...int) int {
	minValue := math.MaxInt16
	for _, value := range values {
		if value < minValue {
			minValue = value
		}
	}
	return minValue
}

func sumInt(values ...int) int {
	sum := 0
	for _, value := range values {
		sum += value
	}
	return sum
}

func indexOfInt(values []int, element int) int {
	for i, value := range values {
		if value == element {
			return i
		}
	}
	return -1
}

// NOTE: using this function seems a teeny bit slower (?!) than inlining Itoa, i.e.
// sum := 0
// for _, r := range strconv.Itoa(n) {
//     sum += int(r-'0')
// }
// Much of the slower-ness appears to be the function call itself.
func digits(n int) []int {
	// peel off digits
	result := make([]int, 0, 8)
	for n > 0 {
		result = append(result, n%10)
		n /= 10
	}
	// reverse them
	for i, j := 0, len(result)-1; i < j; i, j = i+i, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	return result
}

func isPalindrome(text string) bool {
	for i, j := 0, len(text)-1; i < j; i, j = i+1, j-1 {
		if text[i] != text[j] {
			return false
		}
	}
	return true
}

// used in "pandigital" problems
func distinctValidDigits(pan bool, values ...int) bool {
	digits := make(map[int]bool)
	for _, value := range values {
		for ; value > 0; value /= 10 {
			d := value % 10
			if d == 0 || digits[d] {
				return false
			}
			digits[d] = true
		}
	}
	return !pan || len(digits) == 9
}
