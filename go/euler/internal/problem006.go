package internal

type Problem006 struct {
}

func (p *Problem006) Name() string {
	return "Problem 6"
}

func (p *Problem006) Desc() string {
	return "Sum square difference"
}

func (p *Problem006) Solve() int {
	return p.SolveExample(100)
}

func (p *Problem006) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{10, 2640},
		{100, 25164150},
	})
}

func (p *Problem006) SolveExample(n int) int {
	return n * (n + 1) * (n - 1) * (3*n + 2) / 12
}
