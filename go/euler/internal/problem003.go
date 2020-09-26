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
	fmt.Printf("  Solve for 13195, expect 29: %d\n", p.solve(13195))
	fmt.Printf("  Solve for 600851475143, expect 6857: %d\n", p.solve(600851475143))
}

func (p *Problem003) solve(n uint64) uint32 {
	factors := utils.PrimeFactors(n)
	return factors[len(factors)-1]
}
