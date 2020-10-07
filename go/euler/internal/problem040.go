package internal

import (
	"strconv"
	"strings"
)

type Problem040 struct {
}

func (p *Problem040) Name() string {
	return "Problem 40"
}

func (p *Problem040) Desc() string {
	return "Champernowne's constant"
}

func (p *Problem040) Solve() int {
	// build a string by concatenating all the numbers
	var sb strings.Builder
	sb.Grow(1000020)
	sb.WriteString(".") // just to avoid off-by-one confusion
	for n := 1; sb.Len() < 1000004; n++ {
		sb.WriteString(strconv.Itoa(n))
	}
	s := sb.String()
	// now calculate product of requested digits
	product := 1
	for _, i := range []int{1, 10, 100, 1000, 10000, 100000, 1000000} {
		digit, _ := strconv.Atoi(s[i : i+1])
		product *= digit
	}
	return product
}

func (p *Problem040) Run() {
	runProblem(p, 210)
}
