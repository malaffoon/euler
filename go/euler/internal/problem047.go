package internal

type Problem047 struct {
}

func (p *Problem047) Name() string {
	return "Problem 47"
}

func (p *Problem047) Desc() string {
	return "Distinct primes factors"
}

func (p *Problem047) Solve() int {
	return p.SolveExample(4)
}

func (p *Problem047) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{2, 14},
		{3, 644},
		{4, 134043},
	})
}

func (p *Problem047) SolveExample(distinct int) int {
	// create sieve of distinct prime counts
	S := 150000
	sieve := make([]int, S)
	for i := 2; i < S; i++ {
		if sieve[i] == 0 {
			for j := i; j < S; j += i {
				sieve[j] += 1
			}
		}
	}

	// now find 'distinct' consecutive entries in sieve with value 'distinct'
	for i := 2; i < S; i++ {
		if sieve[i] != distinct {
			continue
		}
		found := true
		for d := 1; d < distinct; d++ {
			if sieve[i+d] != distinct {
				found = false
				break
			}
		}
		if found {
			return i
		}
	}
	return 0
}
