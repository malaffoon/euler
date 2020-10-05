package internal

type Problem031 struct {
}

func (p *Problem031) Name() string {
	return "Problem 31"
}

func (p *Problem031) Desc() string {
	return "Coin sums"
}

func (p *Problem031) Solve() int {
	return p.SolveExample(200)
}

func (p *Problem031) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{2, 2},
		{5, 4},
		{200, 73682},
	})
}

func (p *Problem031) SolveExample(n int) int {
	coins := []int{1, 2, 5, 10, 20, 50, 100, 200}
	combos := make([]int, n+1)
	combos[0] = 1
	for _, coin := range coins {
		for i := coin; i <= n; i++ {
			combos[i] += combos[i-coin]
		}
	}
	return combos[n]
}
