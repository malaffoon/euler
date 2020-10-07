package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
	"regexp"
	"sort"
	"strconv"
)

type Problem037 struct {
	primes []int
	re     *regexp.Regexp
}

func (p *Problem037) Name() string {
	return "Problem 37"
}

func (p *Problem037) Desc() string {
	return "Truncatable primes"
}

func (p *Problem037) Solve() int {
	// init class vars
	p.primes = utils.Primes(1000000)
	p.re = regexp.MustCompile(`[2357][1379]*[37]`)

	sum := 0
	for _, prime := range p.primes {
		if p.isTruncatablePrime(prime) {
			sum += prime
		}
	}
	return sum
}

func (p *Problem037) Run() {
	runProblem(p, 748317)
}

func (p *Problem037) isTruncatablePrime(prime int) bool {
	s := strconv.Itoa(prime)
	if !p.re.MatchString(s) {
		return false
	}
	for i := 1; i < len(s); i++ {
		if !p.isPrime(s[i:]) || !p.isPrime(s[0:len(s)-i]) {
			return false
		}
	}
	return true
}

func (p *Problem037) isPrime(s string) bool {
	r, _ := strconv.Atoi(s)
	idx := sort.SearchInts(p.primes, r)
	return idx < len(p.primes) && p.primes[idx] == r
}
