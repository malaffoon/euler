package internal

import (
	"github.com/malaffoon/euler/go/euler/utils"
	"math"
)

type Problem233 struct {
}

func (p *Problem233) Name() string {
	return "Problem 233"
}

func (p *Problem233) Desc() string {
	return "Lattice points on a circle"
}

func (p *Problem233) Solve() int {
	maxN := 100000000000
	ps := make([]int, 0, 10000)
	for _, prime := range utils.Primes(maxN / 5 / 5 / 5 / 13 / 13) {
		if prime%4 == 1 {
			ps = append(ps, prime)
		}
	}

	baseValues := make([]int, 0, 10000)
	for _, fs := range []struct {
		f1 int
		f2 int
		f3 int
	}{
		{3, 2, 1},
		{7, 3, 0},
		{10, 2, 0},
	} {
		for _, p1 := range ps {
			v1 := int(math.Pow(float64(p1), float64(fs.f1)))
			if v1 > maxN {
				break
			}
			for _, p2 := range ps {
				if p2 == p1 {
					continue
				}
				v2 := v1 * int(math.Pow(float64(p2), float64(fs.f2)))
				if v2 > maxN {
					break
				}
				if fs.f3 == 0 {
					baseValues = append(baseValues, v2)
				} else {
					for _, p3 := range ps {
						if p3 == p2 || p3 == p1 {
							continue
						}
						v3 := v2 * p3
						if v3 > maxN {
							break
						}
						baseValues = append(baseValues, v3)
					}
				}
			}
		}
	}

	maxF := maxN/baseValues[0] + 1
	sieve := make([]bool, maxF+1)
	for _, p := range ps {
		for f := p; f < maxF; f += p {
			sieve[f] = true
		}
	}
	factors := make([]int, 0, 10000)
	for f, flag := range sieve {
		if !flag && f != 0 {
			factors = append(factors, f)
		}
	}

	sum := 0
	for _, v := range baseValues {
		for _, f := range factors {
			value := v * f
			if value > maxN {
				break
			}
			sum += value
		}
	}
	return sum
}

func (p *Problem233) Run() {
	runProblem(p, 271204031455541309)
}
