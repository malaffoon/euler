package utils

import "math"

// Calculate all primes up to a limit, using Sieve of Eratosthenes
func Primes(limit uint32) (primes []uint32) {
	sieve := make([]bool, limit)
	for i := uint32(2); i < limit; i++ {
		if sieve[i] == false {
			primes = append(primes, i)
			for j := i * i; j < limit; j += i {
				sieve[j] = true
			}
		}
	}
	return
}

func PrimeFactors(value uint64) (factors []uint32) {
	//vf := float64(value)
	//vfs := math.Sqrt(vf)
	//vfsr := math.Round(vfs)
	//primes := Primes(uint32(1 + vfsr))
	//for _, prime := range primes {
	for _, prime := range Primes(uint32(1 + math.Round(math.Sqrt(float64(value))))) {
		for value > 1 && value%uint64(prime) == 0 {
			factors = append(factors, uint32(prime))
			value = value / uint64(prime)
		}
		if value == 1 || value < uint64(prime*prime) {
			break
		}
	}
	if value > 1 {
		factors = append(factors, uint32(value))
	}
	return
}

func Nth(n uint) uint32 {
	limit := uint32(30)
	if n >= 10 {
		nf := float64(n)
		limit = uint32(math.Ceil(nf * (math.Log(nf) + math.Log(math.Log(nf)))))
	}
	primes := Primes(limit)
	return primes[n-1]
}
