package internal

type Problem650 struct {
}

func (p *Problem650) Name() string {
	return "Problem 650"
}

func (p *Problem650) Desc() string {
	return "Divisors of Binomial Product"
}

func (p *Problem650) Solve() int {
	return p.SolveExample(20000)
}

func (p *Problem650) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{5, 5736},
		{10, 721034267},
		{100, 332792866},
		{20000, 0},
	})
}

func (p *Problem650) SolveExample(n int) int {
	return 0
}
