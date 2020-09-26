package internal

import (
	"fmt"
)

type Problem002 struct {
}

func (p *Problem002) Name() string {
	return "Problem 2"
}

func (p *Problem002) Desc() string {
	return "Even Fibonacci numbers"
}

func (p *Problem002) Solve() int {
	return p.solve(4000000)
}

func (p *Problem002) Run() {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	fmt.Printf("  Solve for 100, expect 44: %d\n", p.solve(100))
	fmt.Printf("  Solve for 40000000, expect 4613732: %d\n", p.solve(4000000))
}

func (p *Problem002) solve(maxValue int) int {
	var sum int
	for f, n := 1, 1; f < maxValue; f, n = n, f+n {
		if f%2 == 0 {
			sum += f
		}
	}
	return sum
}
