package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
	"sort"
	"strconv"
	"strings"
)

type Problem035 struct {
}

func (p *Problem035) Name() string {
	return "Problem 35"
}

func (p *Problem035) Desc() string {
	return "Circular primes"
}

func (p *Problem035) Solve() int {
	return p.SolveExample(1000000)
}

func (p *Problem035) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{100, 13},
		{1000000, 55},
	})
}

func (p *Problem035) SolveExample(n int) int {
	count := 0
	primes := utils.Primes(n)
	for _, p := range primes {
		if isCircularPrime(primes, p) {
			count++
		}
	}
	return count
}

func isCircularPrime(primes []int, p int) bool {
	if p < 10 {
		return true
	}
	s := strconv.Itoa(p)
	if strings.ContainsAny(s, "024568") {
		return false
	}
	for i := 1; i < len(s); i++ {
		s = s[1:] + s[0:1]
		r, _ := strconv.Atoi(s)
		idx := sort.SearchInts(primes, r)
		if idx >= len(primes) || primes[idx] != r {
			return false
		}
	}
	return true
}
