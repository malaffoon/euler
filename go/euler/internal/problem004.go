package internal

type Problem004 struct {
}

func (p *Problem004) Name() string {
	return "Problem 4"
}

func (p *Problem004) Desc() string {
	return "Largest palindrome product"
}

func (p *Problem004) Solve() int {
	return int(p.solve())
}

func (p *Problem004) Run() {
	runProblem(p, 906609)
}

func (p *Problem004) solve() uint {
	var result uint
	for i := 900; i < 1000; i++ {
		for j := i; j < 1000; j++ {
			value := uint(i * j)
			if value == reverse(value) && value > result {
				result = value
			}
		}
	}
	return result
}

// since go's string/rune handling is complex, let's just reverse as a number
func reverse(value uint) uint {
	var result uint
	for value > 0 {
		result = 10*result + value%10
		value /= 10
	}
	return result
}
