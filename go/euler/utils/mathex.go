package utils

import "math"

// Return the Least Common Multiple of two values
func LCM(values []int) int {
	lcm := values[0]
	for _, value := range values[1:] {
		lcm = lcm * (value / GCD(lcm, value))
	}
	return lcm
}

// Return the Greatest Common Divisor of two values
func GCD(a int, b int) int {
	// use Euclid's Algorithm
	for a != b {
		if a > b {
			a -= b
		} else {
			b -= a
		}
	}
	return a
}

// Return the binomial coefficient, i.e. "n choose k"
func Binomial(n int, k int) int {
	// non-recursive, forward calculating version of the recursive additive formula
	cache := make(map[bin]int, 0)
	for ni := 1; ni <= n; ni++ {
		for ki := 0; ki <= k && ki <= ni; ki++ {
			if ni == ki || ki == 0 {
				cache[bin{ni, ki}] = 1
			} else {
				cache[bin{ni, ki}] = cache[bin{ni - 1, ki - 1}] + cache[bin{ni - 1, ki}]
			}
		}
	}
	return cache[bin{n, k}]
}

type bin struct {
	n int
	k int
}

func Trigonal(n int) int {
	return n * (n + 1) / 2
}

func IsTrigonal(v int) bool {
	n := (math.Sqrt(float64(1+8*v)) - 1) / 2
	return float64(int(n)) == n
}

func Pentagonal(n int) int {
	return n * (3*n - 1) / 2
}

func IsPentagonal(v int) bool {
	n := (math.Sqrt(float64(1+24*v)) + 1) / 6
	return float64(int(n)) == n
}

func Hexagonal(n int) int {
	return n * (2*n - 1)
}

func IsHexagonal(v int) bool {
	n := (math.Sqrt(float64(1+8*v)) + 1) / 4
	return float64(int(n)) == n
}
