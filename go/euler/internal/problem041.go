package internal

import (
	"math/big"
)

type Problem041 struct {
}

func (p *Problem041) Name() string {
	return "Problem 41"
}

func (p *Problem041) Desc() string {
	return "Pandigital prime"
}

func (p *Problem041) Solve() int {
	// see python notes; there are two approaches
	// - generate (descending) all 7-digit pandigital numbers and check for primeness, first prime wins
	// - generate all primes between 7654321 and 7612345 and check for pandigitalness
	// I tried it both ways, first approach is much faster (80µs vs. 30ms) and uses less memory.
	// Note we have to use VisitPermutations2 because we're relying on the descending order of permutations.
	result := 0
	value := big.NewInt(0)
	VisitPermutations2([]rune("7654321"), func(runes []rune) bool {
		value.SetString(string(runes), 10)
		if value.ProbablyPrime(0) {
			result = int(value.Int64())
			return false
		} else {
			return true
		}
	})
	return result
}

func (p *Problem041) Run() {
	runProblem(p, 7652413)
}
