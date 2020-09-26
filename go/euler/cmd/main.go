package main

import (
	"fmt"
	. "github.com/malaffoon/euler/go/euler/internal"
	"time"
)

func main() {
	fmt.Println("Running all (Go solved) Project Euler problems ...")
	problems := []Problem{
		new(Problem001),
		new(Problem002),
	}
	for _, p := range problems {
		start := time.Now()
		actual := p.Solve()
		fmt.Printf("%s: %d (%s)\n", p.Name(), actual, time.Since(start))
		//p.Run()
	}
}
