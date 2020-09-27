package internal

import (
	"fmt"
)

type Problem006 struct {
}

func (p *Problem006) Name() string {
	return "Problem 6"
}

func (p *Problem006) Desc() string {
	return "Sum square difference"
}

func (p *Problem006) Solve() int {
	return int(p.solve(100))
}

func (p *Problem006) Run() {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	fmt.Printf("  Solve(10) = %d\n", p.solve(10))   // 2640
	fmt.Printf("  Solve(100) = %d\n", p.solve(100)) // 25164150
}

func (p *Problem006) solve(n uint) uint {
	return n * (n + 1) * (n - 1) * (3*n + 2) / 12
}
