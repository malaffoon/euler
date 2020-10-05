package internal

import "strconv"

type Problem034 struct {
}

func (p *Problem034) Name() string {
	return "Problem 34"
}

func (p *Problem034) Desc() string {
	return "Digit factorials"
}

func (p *Problem034) Solve() int {
	factorials := map[int]int{0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
	result := 0
	for n, nmax := 10, 7*factorials[9]; n < nmax; n++ {
		sum := 0
		for _, r := range strconv.Itoa(n) {
			sum += factorials[int(r-'0')]
		}
		if n == sum {
			result += n
		}
	}
	return result
}

func (p *Problem034) Run() {
	runProblem(p, 40730)
}
