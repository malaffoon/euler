package internal

import (
	"fmt"
	"github.com/malaffoon/euler/go/euler/utils"
	"sort"
	"strconv"
)

type Problem049 struct {
}

func (p *Problem049) Name() string {
	return "Problem 49"
}

func (p *Problem049) Desc() string {
	return "Prime permutations"
}

func (p *Problem049) Solve() int {
	// TODO - this is still much too slow, ~10s !

	// collect the 4 digit primes in a set
	primes := make(map[int]bool)
	for _, prime := range utils.Primes(10000) {
		if prime < 1000 {
			continue
		}
		primes[prime] = true
	}

	for prime, flag := range primes {
		// skip primes we have already visited
		if !flag {
			continue
		}
		// collect prime permutations
		perms := make([]int, 0, 24)
		VisitPermutations([]rune(strconv.Itoa(prime)), func(perm []rune) bool {
			prime, _ := strconv.Atoi(string(perm))
			if primes[prime] {
				perms = append(perms, prime)
				primes[prime] = false
			}
			return true
		})
		if len(perms) < 3 {
			continue
		}
		// might as well skip the given known answer
		if indexOfInt(perms, 1487) > -1 {
			continue
		}
		for _, perm := range IndexPermutations(len(perms)) {
			trio := []int{perms[perm[0]], perms[perm[1]], perms[perm[2]]}
			sort.Ints(trio)
			if trio[1]-trio[0] == trio[2]-trio[1] {
				s := fmt.Sprintf("%d%d%d", trio[0], trio[1], trio[2])
				if result, err := strconv.Atoi(s); err == nil {
					return result
				}
			}
		}
	}

	return 0
}

func (p *Problem049) Run() {
	runProblem(p, 296962999629)
}
