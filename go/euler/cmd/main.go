package main

import (
	"fmt"
	. "github.com/malaffoon/euler/go/euler/internal"
	"os"
	"time"
)

type Action int

const (
	SOLVE Action = iota
	RUN
)

// parse action subcommand; exit if not valid
func parseAction(args []string) Action {
	if len(args) < 2 {
		fmt.Println("run or solve subcommand required")
		os.Exit(1)
	}
	switch args[1] {
	case "run":
		fmt.Println("Running Project Euler problems ...")
		return RUN
	case "solve":
		fmt.Println("Solving Project Euler problems ...")
		return SOLVE
	default:
		fmt.Printf("unknown subcommand: %s", os.Args[1])
		os.Exit(1)
	}
	return SOLVE
}

// parse the (remaining) args for problems
// TODO - is there a way to discover the problems instead of explicitly listing them?
func getProblems(args []string) []Problem {
	problems := []Problem{
		new(Problem001), new(Problem002), new(Problem003), new(Problem004), new(Problem005),
		new(Problem006), new(Problem007), new(Problem008), new(Problem009), new(Problem010),
		new(Problem011), new(Problem012), new(Problem013), new(Problem014), new(Problem015),
		new(Problem016), new(Problem017), new(Problem018), new(Problem019), new(Problem020),
		new(Problem021), new(Problem022), new(Problem023), new(Problem024), new(Problem025),
		new(Problem026), new(Problem027), new(Problem028), new(Problem029), new(Problem030),
		new(Problem031), new(Problem032), new(Problem033), new(Problem034), new(Problem035),
		new(Problem036), new(Problem037), new(Problem038), new(Problem039), new(Problem040),
	}
	// TODO - parse for specific test numbers
	// TODO   for now, always return all of them
	return problems
}

func main() {
	action := parseAction(os.Args)

	for _, p := range getProblems(os.Args[2:]) {
		switch action {
		case SOLVE:
			start := time.Now()
			actual := p.Solve()
			elapsed := time.Since(start)
			fmt.Printf("%s: %d (%s)\n", p.Name(), actual, elapsed)
		case RUN:
			p.Run()
		}
	}
}
