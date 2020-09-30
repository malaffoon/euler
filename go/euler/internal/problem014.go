package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem014 struct {
}

func (p *Problem014) Name() string {
	return "Problem 14"
}

func (p *Problem014) Desc() string {
	return "Longest Collatz sequence"
}

func (p *Problem014) Solve() int {
	return p.solve()
}

func (p *Problem014) Run() {
	runProblem(p, 837799)
}

func (p *Problem014) solve() int {
	// could brute force it using CollatzSequence but ...
	// this approach caches lengths to short-circuit the calculations
	lengths := map[int]int{1: 1, 2: 2, 4: 3, 8: 4, 16: 5}
	maxValue, longest := 16, 5
	for v := 500000; v < 1000000; v++ {
		l, c := 0, v
		for c > 0 {
			if cached, ok := lengths[c]; ok {
				l += cached
				lengths[v] = l
				if l > longest {
					maxValue, longest = v, l
				}
				break
			}
			l += 1
			c = utils.NextCollatz(c)
		}
	}
	return maxValue
}
