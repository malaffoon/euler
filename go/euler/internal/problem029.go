package internal

import (
	"math/big"
)

type Problem029 struct {
}

func (p *Problem029) Name() string {
	return "Problem 29"
}

func (p *Problem029) Desc() string {
	return "Distinct powers"
}

func (p *Problem029) Solve() int {
	return p.SolveExample(100)
}

func (p *Problem029) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{5, 15},
		{100, 9183},
	})
}

func (p *Problem029) SolveExample(n int) int {
	// go's "best" version of a set is a map of empty structs
	terms := make(map[string]struct{})
	exists := struct{}{}

	// create a "worker" big.Int and all the big.Int values once
	z := big.NewInt(0)
	bigs := make([]*big.Int, 0, n)
	for b := 2; b <= n; b++ {
		bigs = append(bigs, big.NewInt(int64(b)))
	}

	// brute-force all the combinations, and use a set to de-dup them
	for _, a := range bigs {
		for _, b := range bigs {
			// base-16 is the fastest base to use
			terms[z.Exp(a, b, nil).Text(16)] = exists
		}
	}
	return len(terms)
}
