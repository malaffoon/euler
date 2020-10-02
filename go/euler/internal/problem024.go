package internal

type Problem024 struct {
}

func (p *Problem024) Name() string {
	return "Problem 24"
}

func (p *Problem024) Desc() string {
	return "Lexicographic permutations"
}

func (p *Problem024) Solve() int {
	// In Python, i just brute forced this since it has permutations() and slices().
	// Instead, we can calculate each digit by counting the permutations of the
	// remaining digits, and advancing that many. For example, for the first digit
	// we have x permutations of 9 digits; 9! = 362880 so we need two full sets plus
	// some. That is, 0{1,2,3,4,5,6,7,8,9} is 362880, then 1{0,2,3,4,5,6,7,8,9} is
	// another 362880, so the millionth permutation is somewhere in 2{0,1,3,4,5,6,7,8,9}.
	// So we can lock in the 2, subtract 2*362880 from n, and continue to the next digit.
	n := 1000000
	lockedDigits := make([]int, 0, 10)
	remainingDigits := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	for n > 1 {
		// number of permutations using all but one of the remaining digits
		f := factorialInt(len(remainingDigits) - 1)
		d := (n - 1) / f
		lockedDigits = append(lockedDigits, remainingDigits[d])
		copy(remainingDigits[d:], remainingDigits[d+1:])
		remainingDigits = remainingDigits[:len(remainingDigits)-1]
		n -= d * f
	}
	lockedDigits = append(lockedDigits, remainingDigits[0])
	// now build a single number from array of locked digits
	result := 0
	for _, digit := range lockedDigits {
		result = 10*result + digit
	}
	return result
}

func (p *Problem024) Run() {
	runProblem(p, 2783915460)
}

// version of factorial that expects to be dealing in small numbers
func factorialInt(n int) int {
	f := 1
	for ; n > 1; n-- {
		f *= n
	}
	return f
}
