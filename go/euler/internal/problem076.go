package internal

type Problem076 struct {
}

func (p *Problem076) Name() string {
	return "Problem 76"
}

func (p *Problem076) Desc() string {
	return "Counting summations"
}

func (p *Problem076) Solve() int {
	return p.SolveExample(100)
}

func (p *Problem076) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{5, 6},
		{100, 190569291},
	})
}

func (p *Problem076) SolveExample(n int) int {
	combos := make([]int, n+1)
	combos[0] = 1
	for d := 1; d < n; d++ {
		for i := d; i <= n; i++ {
			combos[i] += combos[i-d]
		}
	}
	return combos[n]
}
