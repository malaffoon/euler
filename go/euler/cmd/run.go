package main

import (
	"fmt"
	. "github.com/malaffoon/euler/go/euler/internal"
	"time"
)

// just a wrapper to run a hard-coded test, for debugging
func main() {
	p := new(Problem018)

	p.Run()

	start := time.Now()
	actual := p.Solve()
	elapsed := time.Since(start)
	fmt.Printf("%s: %d (%s)\n", p.Name(), actual, elapsed)
}
