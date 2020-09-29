package internal

import (
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
	return p.SolveExample(10001)
}

func (p *Problem007) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{100, 541},
		{1000, 7919},
		{10001, 104743},
	})
}

func (p *Problem007) SolveExample(n int) int {
	return utils.NthPrime(n)
}
