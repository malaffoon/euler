package internal

type Problem001 struct {
}

func (p *Problem001) Name() string {
	return "Problem 1"
}

func (p *Problem001) Desc() string {
	return "Multiples of 3 and 5"
}

func (p *Problem001) Solve() int {
	return p.SolveExample(1000)
}

func (p *Problem001) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{10, 23},
		{1000, 233168},
	})
}

func (p *Problem001) SolveExample(limit int) int {
	var sum int
	for i := 1; i < limit; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	return sum
}
