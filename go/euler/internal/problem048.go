package internal

import (
	"math/big"
	"strconv"
)

type Problem048 struct {
}

func (p *Problem048) Name() string {
	return "Problem 48"
}

func (p *Problem048) Desc() string {
	return "Self powers"
}

func (p *Problem048) Solve() int {
	return p.SolveExample(1000)
}

func (p *Problem048) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{10, 405071317},
		{1000, 9110846700},
	})
}

func (p *Problem048) SolveExample(n int) int {
	sum := big.NewInt(0)
	bigN := big.NewInt(0)
	for i := 1; i <= n; i++ {
		bigN.SetInt64(int64(i))
		bigN = bigN.Exp(bigN, bigN, nil)
		sum = sum.Add(sum, bigN)
	}
	s := sum.String()
	last10, _ := strconv.Atoi(s[len(s)-10:])
	return last10
}
