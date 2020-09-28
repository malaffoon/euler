package internal

import (
	"fmt"
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem010 struct {
}

func (p *Problem010) Name() string {
	return "Problem 10"
}

func (p *Problem010) Desc() string {
	return "Summation of primes"
}

func (p *Problem010) Solve() int {
	return int(p.solve(2000000))
}

func (p *Problem010) Run() {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	fmt.Printf("  Solve(10) = %d\n", p.solve(10))           // 17
	fmt.Printf("  Solve(2000000) = %d\n", p.solve(2000000)) // 142913828922
}

func (p *Problem010) solve(n uint32) uint64 {
	var result uint64
	for _, prime := range utils.Primes(n) {
		result += uint64(prime)
	}
	return result
}
