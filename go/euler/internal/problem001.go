package internal

import (
	"fmt"
)

type Problem001 struct {
}

// TODO - using pointer to avoid copying problem, not to mutate it. What is best practice?
func (p *Problem001) Solve() int {
	return p.solve(1000)
}

func (p *Problem001) Run() {
	fmt.Println("Problem 1 - Multiples of 3 and 5")
	fmt.Printf("  Solve for 10: %d\n", p.solve(10))
	fmt.Printf("  Solve for 1000: %d\n", p.solve(1000))
}

func (p *Problem001) solve(limit int) int {
	var sum int
	for i := 1; i < limit; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	return sum
}
