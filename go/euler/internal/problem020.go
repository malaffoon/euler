package internal

import "math/big"

type Problem020 struct {
}

func (p *Problem020) Name() string {
	return "Problem 20"
}

func (p *Problem020) Desc() string {
	return "Factorial digit sum"
}

func (p *Problem020) Solve() int {
	return p.SolveExample(100)
}

func (p *Problem020) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{10, 27},
		{100, 648},
	})
}

func (p *Problem020) SolveExample(n int) int {
	// use big Int to do factorial
	f := big.NewInt(1)
	for i := 2; i <= n; i++ {
		f = f.Mul(f, big.NewInt(int64(i)))
	}
	sum := 0
	for _, r := range f.String() {
		sum += int(r - '0')
	}
	return sum
}
