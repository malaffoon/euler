package utils

// Helpers for Collatz sequences
//
// The following iterative sequence is defined for the set of positive integers:
//   n → n/2 (n is even), n → 3n + 1 (n is odd)
//
// Using the rule above and starting with 13, we generate the following sequence:
//   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

// Return the next Collatz sequence number
// Returns 0 after 1, to avoid infinite recurse on 4,2,1
func NextCollatz(n int) int {
	switch {
	case n == 1:
		return 0
	case n%2 == 0:
		return int(n / 2)
	default:
		return 3*n + 1
	}
}

func CollatzGenerator(n int) chan int {
	c := make(chan int)

	go func() {
		for ; n != 0; n = NextCollatz(n) {
			c <- n
		}
		close(c)
	}()

	return c
}

func CollatzSequence(n int) []int {
	data := make([]int, 0, 16)
	for n := range CollatzGenerator(n) {
		data = append(data, n)
	}
	return data
}
