package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem021 struct {
}

func (p *Problem021) Name() string {
	return "Problem 21"
}

func (p *Problem021) Desc() string {
	return "Amicable numbers"
}

func (p *Problem021) Solve() int {
	sum := 0
	for n := 100; n < 10000; n++ {
		if isAmicableNumber(n) {
			sum += n
		}
	}
	return sum
}

func isAmicableNumber(n int) bool {
	sum := sumInt(properDivisors(n)...)
	return sum != n && n == sumInt(properDivisors(sum)...)
}

func properDivisors(n int) []int {
	// "proper divisors" do not include the number itself
	result := utils.Divisors(n)
	return result[:len(result)-1]
}

func (p *Problem021) Run() {
	runProblem(p, 31626)
}
