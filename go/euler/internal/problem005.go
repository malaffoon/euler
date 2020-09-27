package internal

import (
	"fmt"
	"github.com/malaffoon/euler/go/euler/utils"
)

type Problem005 struct {
}

func (p *Problem005) Name() string {
	return "Problem 5"
}

func (p *Problem005) Desc() string {
	return "Smallest multiple"
}

func (p *Problem005) Solve() int {
	return int(p.solve([]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}))
}

func (p *Problem005) Run() {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	fmt.Printf("  Solve(1..10) = %d\n", p.solve([]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))                                         // 2520
	fmt.Printf("  Solve(1..20) = %d\n", p.solve([]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20})) // 232792560
}

func (p *Problem005) solve(values []uint) uint {
	return utils.LCM(values)
}
