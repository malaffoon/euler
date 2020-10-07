package internal

type Problem039 struct {
}

func (p *Problem039) Name() string {
	return "Problem 39"
}

func (p *Problem039) Desc() string {
	return "Integer right triangles"
}

func (p *Problem039) Solve() int {
	maxCount, maxPerimeter := 0, 0
	for perimeter := 12; perimeter < 1001; perimeter += 2 {
		count := 0
		for a, amax := 1, perimeter/2; a < amax; a++ {
			b := float64(perimeter) * float64(perimeter-2*a) / 2. / float64(perimeter-a)
			if b == float64(int(b)) {
				count++
			}
		}
		if count > maxCount {
			maxCount, maxPerimeter = count, perimeter
		}
	}
	return maxPerimeter
}

func (p *Problem039) Run() {
	runProblem(p, 840)
}
