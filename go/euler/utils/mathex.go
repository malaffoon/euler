package utils

// Return the Least Common Multiple of two values
func LCM(values []uint) uint {
	lcm := values[0]
	for _, value := range values[1:] {
		lcm = lcm * (uint(value) / GCD(lcm, uint(value)))
	}
	return lcm
}

// Return the Greatest Common Divisor of two values
func GCD(a uint, b uint) uint {
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
