package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem044 struct {
}

func (p *Problem044) Name() string {
	return "Problem 44"
}

func (p *Problem044) Desc() string {
	return "Pentagon numbers"
}

func (p *Problem044) Solve() int {
	for j := 1; ; j++ {
		pj := utils.Pentagonal(j)
		for k := j - 1; k > 0; k-- {
			pk := utils.Pentagonal(k)
			if utils.IsPentagonal(pj+pk) && utils.IsPentagonal(pj-pk) {
				return pj - pk
			}
		}
	}
}

func (p *Problem044) Run() {
	runProblem(p, 5482660)
}
