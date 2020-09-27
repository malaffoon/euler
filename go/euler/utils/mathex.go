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
