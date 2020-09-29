package internal

import (
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
	return p.SolveExample(2000000)
}

func (p *Problem010) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{10, 17},
		{2000000, 142913828922},
	})
}

func (p *Problem010) SolveExample(n int) int {
	var result int
	for _, prime := range utils.Primes(n) {
		result += prime
	}
	return result
}
