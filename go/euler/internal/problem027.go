package internal

import (
	"fmt"
	"github.com/malaffoon/euler/go/euler/utils"
	"math/big"
)

type Problem027 struct {
}

func (p *Problem027) Name() string {
	return "Problem 27"
}

func (p *Problem027) Desc() string {
	return "Quadratic primes"
}

func (p *Problem027) Solve() int {
	// see comment in Python solution for this
	a, b := -61, 971
	return a * b
}

func (p *Problem027) Run() {
	runProblem(p, -59231)
}

// brute force does work, takes about 1-2 seconds
func (p *Problem027) BruteForce() int {
	maxPrimes, result := 0, 0
	for _, b := range utils.Primes(1001) {
		for a := -b; a < 1000; a += 2 {
			if primes := numberOfPrimesFor(a, b); primes > maxPrimes {
				maxPrimes, result = primes, a * b
				fmt.Println(a, b, maxPrimes, result)
			}
		}
	}
	return result
}

func numberOfPrimesFor(a, b int) int {
	count := 0
	for n := 0; ; n++ {
		q := int64(n * n + a * n + b)
		if q <= 1 || !big.NewInt(q).ProbablyPrime(0) {
			break
		}
		count++
	}
	return count
}
