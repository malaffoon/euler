package internal

import (
	"fmt"
)

type Problem001 struct {
}

func (p *Problem001) Name() string {
	return "Problem 1"
}

func (p *Problem001) Desc() string {
	return "Multiples of 3 and 5"
}

func (p *Problem001) Solve() int {
	return p.solve(1000)
}

func (p *Problem001) Run() {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	fmt.Printf("  Solve(10) = %d\n", p.solve(10))     // 23
	fmt.Printf("  Solve(1000) = %d\n", p.solve(1000)) // 233168
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
