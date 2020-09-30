package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem015 struct {
}

func (p *Problem015) Name() string {
	return "Problem 15"
}

func (p *Problem015) Desc() string {
	return "Lattice paths"
}

func (p *Problem015) Solve() int {
	return p.SolveExample(20)
}

func (p *Problem015) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{2, 6},
		{3, 20},
		{4, 70},
		{20, 137846528820},
	})
}

func (p *Problem015) SolveExample(n int) int {
	return utils.Binomial(2*n, n)
}
