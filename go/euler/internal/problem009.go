package internal

import (
	"math"
)

type Problem009 struct {
}

func (p *Problem009) Name() string {
	return "Problem 9"
}

func (p *Problem009) Desc() string {
	return "Special Pythagorean triplet"
}

func (p *Problem009) Solve() int {
	return p.SolveExample(1000)
}

func (p *Problem009) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{12, 60},
		{1000, 31875000},
	})
}

func (p *Problem009) SolveExample(n int) int {
	for a, amax := 1, n/3; a < amax; a++ {
		b := float64(n*n-2*a*n) / float64(n-a) / 2.
		if math.Round(b) == b {
			return a * int(b) * (n - a - int(b))
		}
	}
	return 0
}
