package internal

import (
	"math/big"
)

type Problem016 struct {
}

func (p *Problem016) Name() string {
	return "Problem 16"
}

func (p *Problem016) Desc() string {
	return "Power digit sum"
}

func (p *Problem016) Solve() int {
	return p.SolveExample(1000)
}

func (p *Problem016) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{5, 5},
		{15, 26},
		{1000, 1366},
	})
}

func (p *Problem016) SolveExample(n int) int {
	text := new(big.Int).Exp(big.NewInt(2), big.NewInt(int64(n)), nil).Text(10)
	sum := 0
	for _, r := range text {
		sum += int(r - '0')
	}
	return sum
}
