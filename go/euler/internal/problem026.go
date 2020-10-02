package internal

type Problem026 struct {
}

func (p *Problem026) Name() string {
	return "Problem 26"
}

func (p *Problem026) Desc() string {
	return "Reciprocal cycles"
}

func (p *Problem026) Solve() int {
	return p.SolveExample(1000)
}

func (p *Problem026) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{10, 7},
		{100, 97},
		{1000, 983},
	})
}

func (p *Problem026) SolveExample(limit int) int {
	maxD, maxCycle := 0, 0
	for d := 2; d < limit; d++ {
		if cycle := reciprocalCycleLength(d); cycle > maxCycle {
			maxD, maxCycle = d, cycle
		}
	}
	return maxD
}

func reciprocalCycleLength(n int) int {
	seen := []int{10}
	for i := 0; i < n; i++ {
		val := 10 * (seen[len(seen)-1] % n)
		if val == 0 {
			break
		}
		if idx := indexOfInt(seen, val); idx >= 0 {
			return len(seen) - idx
		}
		seen = append(seen, val)
	}
	return 0
}
