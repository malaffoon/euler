package internal

import (
	"math"
)

type Problem025 struct {
}

func (p *Problem025) Name() string {
	return "Problem 25"
}

func (p *Problem025) Desc() string {
	return "1000-digit Fibonacci number"
}

func (p *Problem025) Solve() int {
	return p.SolveExample(1000)
}

func (p *Problem025) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{3, 12},
		{1000, 4782},
	})
}

func (p *Problem025) SolveExample(n int) int {
	sqrt5 := math.Sqrt(5)
	phi := (1 + sqrt5) / 2
	return int(math.Ceil((float64(n) - 1 + math.Log10(sqrt5)) / math.Log10(phi)))
}
