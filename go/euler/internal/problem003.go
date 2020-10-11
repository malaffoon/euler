package internal

import (
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
	return int(p.SolveExample(600851475143))
}

func (p *Problem003) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{13195, 29},
		{600851475143, 6857},
	})
}

func (p *Problem003) SolveExample(n int) int {
	factors := utils.PrimeFactorsExpanded(n)
	return int(factors[len(factors)-1])
}
