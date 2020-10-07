package internal

type Problem032 struct {
}

func (p *Problem032) Name() string {
	return "Problem 32"
}

func (p *Problem032) Desc() string {
	return "Pandigital products"
}

func (p *Problem032) Solve() int {
	// generate all the valid multipliers (unique digits with no zeroes)
	multipliers := make([]int, 0, 1000)
	for m := 1; m < 10000; m++ {
		if distinctValidDigits(false, m) {
			multipliers = append(multipliers, m)
		}
	}
	// find all the products for expressions that are pandigital
	products := make(map[int]struct{})
	exists := struct{}{}
	for ai, max := 0, len(multipliers); ai < max; ai++ {
		a := multipliers[ai]
		for bi := ai + 1; bi < max; bi++ {
			b := multipliers[bi]
			prod := a * b
			if prod > 10000 {
				break
			}
			if distinctValidDigits(true, a, b, prod) {
				products[prod] = exists
			}
		}
	}
	result := 0
	for prod := range products {
		result += prod
	}
	return result
}

func (p *Problem032) Run() {
	runProblem(p, 45228)
}
