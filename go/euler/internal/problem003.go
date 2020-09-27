package internal

import (
	"fmt"
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem003 struct {
}

func (p *Problem003) Name() string {
	return "Problem 3"
}

func (p *Problem003) Desc() string {
	return "Largest prime factor"
}

func (p *Problem003) Solve() int {
	return int(p.solve(600851475143))
}

func (p *Problem003) Run() {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	fmt.Printf("  Solve(13195) = %d\n", p.solve(13195))               // 29
	fmt.Printf("  Solve(600851475143) = %d\n", p.solve(600851475143)) // 6857
}

func (p *Problem003) solve(n uint64) uint32 {
	factors := utils.PrimeFactors(n)
	return factors[len(factors)-1]
}
