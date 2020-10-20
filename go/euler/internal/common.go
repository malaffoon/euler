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

// Helper to determine if a (set of) value is pandigital given the allowed digits.
// IsPandigital([]int{1,2,3,4}, 12, 34) == true
// IsPandigital([]int{1,2,3,4}, 12, 345) == false (5 isn't allowed)
// IsPandigital([]int{1,2,3,4}, 12, 3) == false (4 not found)
// IsPandigital([]int{1,2,3,4}, 12344) == false (4 found twic)
func IsPandigital(digits []int, values ...int) bool {
	found := make(map[int]bool)
	for _, value := range values {
		for ; value > 0; value /= 10 {
			d := value % 10
			if indexOfInt(digits, d) == -1 || found[d] {
				return false
			}
			found[d] = true
		}
	}
	return len(found) == len(digits)
}

// Generate all permutations of a string, applying a function to each. It
// continues visiting permutations while the function returns true. It returns
// true if all permutations were visited (i.e. function never returned false).
//
// This uses []rune for efficiency. Recall,
//  - to make rune array from string: []rune(s)
//  - to make string from rune array: string(runes)
// Sequence is not "stable"; e.g. abc -> abc bac cab acb bca cba (stable would be abc -> abc acb bac bca cab cba).
func VisitPermutations(runes []rune, f func([]rune) bool) bool {
	// for this non-recursive approach, the stack keeps track of where we are
	stack := make([]int, len(runes))
	if !f(runes) {
		return false
	}
	for s := 0; s < len(runes); {
		if stack[s] < s {
			if s%2 == 0 {
				runes[0], runes[s] = runes[s], runes[0]
			} else {
				runes[stack[s]], runes[s] = runes[s], runes[stack[s]]
			}
			if !f(runes) {
				return false
			}
			stack[s] += 1
			s = 0
		} else {
			stack[s] = 0
			s += 1
		}
	}
	return true
}

// Recursive permutations; more stable sequence, works from right to left
func VisitPermutations2(runes []rune, f func([]rune) bool) bool {
	return perm(runes, f, 0)
}

func perm(runes []rune, f func([]rune) bool, i int) bool {
	if i > len(runes) {
		return f(runes)
	}
	flag := perm(runes, f, i+1)
	for j := i + 1; j < len(runes) && flag; j++ {
		runes[i], runes[j] = runes[j], runes[i]
		flag = perm(runes, f, i+1)
		runes[i], runes[j] = runes[j], runes[i]
	}
	return flag
}

// Returns an array of permutations of an array of ints up to (excluding) the value given, e.g.
// IndexPermutations(3) -> [0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]
func IndexPermutations(n int) [][]int {
	data := make([]int, n)
	for i := 0; i < n; i++ {
		data[i] = i
	}
	perms := make([][]int, 0, Factorial(n))
	perms = append(perms, append([]int(nil), data...))
	stack := make([]int, n)
	for s := 0; s < n; {
		if stack[s] < s {
			if s%2 == 0 {
				data[0], data[s] = data[s], data[0]
			} else {
				data[stack[s]], data[s] = data[s], data[stack[s]]
			}
			perms = append(perms, append([]int(nil), data...))
			stack[s] += 1
			s = 0
		} else {
			stack[s] = 0
			s += 1
		}
	}
	return perms
}

// simple factorial function for small int values
func Factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * Factorial(n-1)
}
