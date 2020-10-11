package internal

import "github.com/malaffoon/euler/go/euler/utils"

type Problem045 struct {
}

func (p *Problem045) Name() string {
	return "Problem 45"
}

func (p *Problem045) Desc() string {
	return "Triangular, pentagonal, and hexagonal"
}

func (p *Problem045) Solve() int {
	for n := 286; ; n++ {
		v := utils.Trigonal(n)
		if utils.IsPentagonal(v) && utils.IsHexagonal(v) {
			return v
		}
	}
}

func (p *Problem045) Run() {
	runProblem(p, 1533776805)
}
