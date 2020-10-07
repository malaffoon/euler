package internal

import "strconv"

type Problem038 struct {
}

func (p *Problem038) Name() string {
	return "Problem 38"
}

func (p *Problem038) Desc() string {
	return "Pandigital multiples"
}

func (p *Problem038) Solve() int {
	// really only one set of numbers to consider: (1,2) with 9123..9487
	largest := 0
	for n := 9123; n < 9488; n++ {
		if distinctValidDigits(true, n, 2*n) {
			p, _ := strconv.Atoi(strconv.Itoa(n) + strconv.Itoa(2*n))
			if p > largest {
				largest = p
			}
		}
	}
	return largest
}

func (p *Problem038) Run() {
	runProblem(p, 932718654)
}
