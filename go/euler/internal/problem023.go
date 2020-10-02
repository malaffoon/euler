package internal

import "github.com/malaffoon/euler/go/euler/utils"

type Problem023 struct {
}

func (p *Problem023) Name() string {
	return "Problem 23"
}

func (p *Problem023) Desc() string {
	return "Non-abundant sums"
}

func (p *Problem023) Solve() int {
	// first find all the abundants
	abundants := make([]int, 0)
	for n := 1; n < 28124; n++ {
		if sumInt(utils.Divisors(n)...)-n > n {
			abundants = append(abundants, n)
		}
	}
	// next, create a sieve of all values and mark those that are the sum of two abundants
	summable := make([]bool, 28124)
	for i, max := 0, len(abundants); i < max; i++ {
		for j := i; j < max; j++ {
			s := abundants[i] + abundants[j]
			if s >= 28124 {
				break
			}
			summable[s] = true
		}
	}
	// finally, sum up the non-summable values
	sum := 0
	for s, flag := range summable {
		if !flag {
			sum += s
		}
	}
	return sum
}

func (p *Problem023) Run() {
	runProblem(p, 4179871)
}
