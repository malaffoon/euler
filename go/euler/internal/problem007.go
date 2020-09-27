package internal

import (
	"fmt"
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem007 struct {
}

func (p *Problem007) Name() string {
	return "Problem 7"
}

func (p *Problem007) Desc() string {
	return "10001st prime"
}

func (p *Problem007) Solve() int {
	return int(p.solve(10001))
}

func (p *Problem007) Run() {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	fmt.Printf("  Solve(10) = %d\n", p.solve(10))       // 29
	fmt.Printf("  Solve(100) = %d\n", p.solve(100))     // 541
	fmt.Printf("  Solve(1000) = %d\n", p.solve(1000))   // 7919
	fmt.Printf("  Solve(10001) = %d\n", p.solve(10001)) // 104743
}

func (p *Problem007) solve(n uint) uint {
	return uint(utils.Nth(n))
}
