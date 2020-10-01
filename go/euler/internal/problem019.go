package internal

import "time"

type Problem019 struct {
}

func (p *Problem019) Name() string {
	return "Problem 19"
}

func (p *Problem019) Desc() string {
	return "Counting Sundays"
}

func (p *Problem019) Solve() int {
	count := 0
	for year := 1901; year <= 2000; year++ {
		for month := time.January; month <= time.December; month++ {
			if time.Date(year, month, 1, 0, 0, 0, 0, time.UTC).Weekday() == time.Sunday {
				count++
			}
		}
	}
	return count
}

func (p *Problem019) Run() {
	runProblem(p, 171)
}
