package internal

import (
	"math"
	"strconv"
)

type Problem030 struct {
}

func (p *Problem030) Name() string {
	return "Problem 30"
}

func (p *Problem030) Desc() string {
	return "Digit fifth powers"
}

func (p *Problem030) Solve() int {
	return p.SolveExample(5)
}

func (p *Problem030) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{4, 19316},
		{5, 443839},
	})
}

func (p *Problem030) SolveExample(n int) int {
	result := 0
	fn := float64(n)
	for i, imax := 10, int(float64(n+1)*math.Pow(9, fn)); i <= imax; i++ {
		sum := 0
		for _, r := range strconv.Itoa(i) {
			sum += int(math.Pow(float64(r-'0'), fn))
		}
		if sum == i {
			result += i
		}
	}
	return result
}
