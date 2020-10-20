package internal

import "math/big"

type Problem046 struct {
}

func (p *Problem046) Name() string {
	return "Problem 46"
}

func (p *Problem046) Desc() string {
	return "Goldbach's other conjecture"
}

func (p *Problem046) Solve() int {
	// cache the twice a square values
	twiceSquares := make([]int, 100)
	for i := 0; i < 100; i++ {
		twiceSquares[i] = 2 * i * i
	}

	for n := 35; ; n += 2 {
		hasSolution := false
		for _, ts := range twiceSquares {
			if ts >= n {
				break
			}
			if big.NewInt(int64(n - ts)).ProbablyPrime(0) {
				hasSolution = true
				break
			}
		}
		if !hasSolution {
			return n
		}
	}
}

func (p *Problem046) Run() {
	runProblem(p, 5777)
}
