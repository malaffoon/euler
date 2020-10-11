package internal

import (
	"strconv"
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
	// FTR, the brute force solution of building the string and indexing
	// into it work fine and ran in 6-7ms.
	// However, this is more fun and waaay faster ...
	product := 1
	for _, i := range []int{1, 10, 100, 1000, 10000, 100000, 1000000} {
		product *= findChampernowneDigit(i)
	}
	return product
}

func (p *Problem040) Run() {
	runProblem(p, 210)
}

func findChampernowneDigit(n int) int {
	// find digit at nth position
	// first, move to the "powers of ten" section (1..9, 10..99, 100...999, etc.)
	// each "powers of ten" section provides d * 9 * 10^(d-1) digits
	digits := 1
	section := 1
	for ; ; digits, section = digits+1, section*10 {
		tmp := digits * 9 * section
		if n < tmp {
			break
		}
		n -= tmp
	}
	// now, figure out which integer we're at and what the remaining offset is
	n -= 1
	integer := section + n/digits
	offset := n % digits
	digit, _ := strconv.Atoi(strconv.Itoa(integer)[offset : offset+1])
	return digit
}
