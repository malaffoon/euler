package internal

import "strconv"

type Problem036 struct {
}

func (p *Problem036) Name() string {
	return "Problem 36"
}

func (p *Problem036) Desc() string {
	return "Double-base palindromes"
}

func (p *Problem036) Solve() int {
	return p.SolveExample(1000000)
}

func (p *Problem036) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{10, 25},
		{1000000, 872187},
	})
}

func (p *Problem036) SolveExample(limit int) int {
	sum := 0
	for n := 1; n < limit; n += 2 {
		if isPalindrome(strconv.FormatInt(int64(n), 10)) && isPalindrome(strconv.FormatInt(int64(n), 2)) {
			sum += n
		}
	}
	return sum
}
