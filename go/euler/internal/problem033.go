package internal

import "github.com/malaffoon/euler/go/euler/utils"

type Problem033 struct {
}

func (p *Problem033) Name() string {
	return "Problem 33"
}

func (p *Problem033) Desc() string {
	return "Digit cancelling fractions"
}

func (p *Problem033) Solve() int {
	product := []int{1, 1} // product of matching fractions
	for d := 11; d < 100; d++ {
		for n := 10; n < d; n++ {
			f := float64(n) / float64(d)
			nd, dd := digits(n), digits(d)
			if (nd[0] == dd[1] && dd[0] != 0 && f == float64(nd[1])/float64(dd[0])) ||
				(nd[1] == dd[0] && dd[1] != 0 && f == float64(nd[0])/float64(dd[1])) {
				product[0] *= n
				product[1] *= d
			}
		}
	}
	return product[1] / utils.GCD(product[0], product[1])
}

func (p *Problem033) Run() {
	runProblem(p, 100)
}
