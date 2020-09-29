package utils

import (
	"math"
	"sort"
)

// Calculate all primes up to a limit, using Sieve of Eratosthenes.
// Obviously, this is limited to values less than max int value.
func Primes(limit int) (primes []int) {
	sieve := make([]bool, limit)
	sqrtOfLimit := int(math.Floor(math.Sqrt(float64(limit))))
	for i := 2; i < limit; i++ {
		if sieve[i] == false {
			primes = append(primes, i)
			if i <= sqrtOfLimit {
				for j := i * i; j < limit; j += i {
					sieve[j] = true
				}
			}
		}
	}
	return
}

func NthPrime(n int) int {
	limit := 30
	if n >= 10 {
		nf := float64(n)
		limit = int(math.Ceil(nf * (math.Log(nf) + math.Log(math.Log(nf)))))
	}
	primes := Primes(limit)
	return primes[n-1]
}

type PrimeFactor struct {
	prime int
	count int
}

func getPrimeFactors(value int) (factors []PrimeFactor) {
	for _, prime := range Primes(int(1 + math.Round(math.Sqrt(float64(value))))) {
		count := 0
		for value > 1 && value%prime == 0 {
			count += 1
			value = value / prime
		}
		if count > 0 {
			factors = append(factors, PrimeFactor{prime, count})
		}
		if value == 1 || value < prime*prime {
			break
		}
	}
	if value > 1 {
		factors = append(factors, PrimeFactor{value, 1})
	}
	return
}

func PrimeFactors(value int) (factors []int) {
	for _, pf := range getPrimeFactors(value) {
		for i := 0; i < pf.count; i++ {
			factors = append(factors, pf.prime)
		}
	}
	return
}

// return a list of the divisors of a value, including 1 and the value
func Divisors(value int) (divisors []int) {
	// catch degenerate case
	if value == 1 {
		return []int{1}
	}

	// using 1350 as an example; 1350 = 2 x 3 x 3 x 3 x 5 x 5
	// first, get the factors, e.g. 1350 -> (2,1),(3,3),(5,2)
	factors := getPrimeFactors(value)

	// expand into tuples of exponentiated values -> (1,2),(1,3,9,27),(1,5,25)
	tuples := make([][]int, len(factors))
	for f, factor := range factors {
		tuples[f] = make([]int, factor.count+1)
		for i, v := 0, 1; i <= factor.count; i, v = i+1, v*factor.prime {
			tuples[f][i] = v
		}
	}

	// generate cross product of the tuples -> (1,2),(1,5,25,3,15,75,...,675) -> (1,5,25,3,15,75,...,1350)
	for len(tuples) > 1 {
		last := len(tuples) - 1
		product := make([]int, 0, len(tuples[last-1])*len(tuples[last]))
		for _, v1 := range tuples[last-1] {
			for _, v2 := range tuples[last] {
				product = append(product, v1*v2)
			}
		}
		tuples[last-1] = product
		tuples = tuples[:last]
	}
	// sort remaining tuple and return it
	sort.Ints(tuples[0])
	return tuples[0]
}
