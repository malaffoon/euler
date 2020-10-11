package internal

import (
	"fmt"
	"strconv"
	"strings"
)

type Problem043 struct {
}

func (p *Problem043) Name() string {
	return "Problem 43"
}

func (p *Problem043) Desc() string {
	return "Sub-string divisibility"
}

func (p *Problem043) Solve() int {
	// find all 3-digit multiples of 17,13,11,7,5,3,2
	// working backwards ...
	// set 3-digit value, check overlap
	return helper([]int{17, 13, 11, 7, 5, 3, 2}, "")
}

func (p *Problem043) Run() {
	runProblem(p, 16695334890)
}

// need a recursive helper
func helper(pq []int, candidate string) int {
	sum := 0
	if len(pq) == 0 {
		// figure out valid starting digit
		for d := '1'; d <= '9'; d++ {
			if !strings.ContainsRune(candidate, d) {
				value, _ := strconv.Atoi(string(d) + candidate)
				sum += value
				return sum
			}
		}
		fmt.Println(candidate)
	} else {
		for n := pq[0]; n < 1000; n += pq[0] {
			sub := fmt.Sprintf("%03d", n)
			if !allUnique(sub) {
				continue
			}
			if len(candidate) == 0 {
				sum += helper(pq[1:], sub)
			} else if sub[1:3] == candidate[0:2] && !strings.Contains(candidate, sub[0:1]) {
				sum += helper(pq[1:], sub[0:1]+candidate)
			}
		}
	}
	return sum
}

func allUnique(value string) bool {
	for i := 0; i < len(value); i++ {
		for j := i + 1; j < len(value); j++ {
			if value[i] == value[j] {
				return false
			}
		}
	}
	return true
}
