package internal

type Problem002 struct {
}

func (p *Problem002) Name() string {
	return "Problem 2"
}

func (p *Problem002) Desc() string {
	return "Even Fibonacci numbers"
}

func (p *Problem002) Solve() int {
	return p.SolveExample(4000000)
}

func (p *Problem002) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{100, 44},
		{4000000, 4613732},
	})
}

func (p *Problem002) SolveExample(maxValue int) int {
	var sum int
	for f, n := 1, 1; f < maxValue; f, n = n, f+n {
		if f%2 == 0 {
			sum += f
		}
	}
	return sum
}
