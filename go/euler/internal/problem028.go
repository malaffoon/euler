package internal

type Problem028 struct {
}

func (p *Problem028) Name() string {
	return "Problem 28"
}

func (p *Problem028) Desc() string {
	return "Number spiral diagonals"
}

func (p *Problem028) Solve() int {
	return p.SolveExample(1001)
}

func (p *Problem028) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{5, 101},
		{1001, 669171001},
	})
}

func (p *Problem028) SolveExample(n int) int {
	// see python solution for explanation
	sum := 1
	for r, rmax := 1, (n-1)/2; r <= rmax; r++ {
		sum += 4 * (4*r*r + r + 1)
	}
	return sum

}
