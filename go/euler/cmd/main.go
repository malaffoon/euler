package main

//This will probably get messy: it is just a runner for code in "internal".

import (
	"fmt"
	. "github.com/malaffoon/euler/go/euler/internal"
)

func main() {
	fmt.Println("Running all (Go solved) Project Euler problems ...")
	problems := []Problem{
		new(Problem001),
	}
	for _, p := range problems {
		p.Run()
	}
}
