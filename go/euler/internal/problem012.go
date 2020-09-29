package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem012 struct {
}

func (p *Problem012) Name() string {
	return "Problem 12"
}

func (p *Problem012) Desc() string {
	return "Highly divisible triangular number"
}

func (p *Problem012) Solve() int {
	return p.solve()
}

func (p *Problem012) Run() {
	runProblem(p, 76576500)
}

func (p *Problem012) solve() int {
	// brute force works in less than 200ms
	var triangle int
	for n := 1; true; n++ {
		triangle += n
		if len(utils.Divisors(triangle)) > 500 {
			return triangle
		}
	}
	return 0
}
