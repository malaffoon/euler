package internal

import "fmt"

// Interface for problems run by the wrapper command
type Problem interface {
	// Return the problem name, e.g. "Problem 1"
	Name() string

	// Return the problem short description, e.g. "Multiples of 3 and 5"
	Desc() string

	// Solve the problem, returning the answer
	Solve() int

	// Run the problem; this may run examples, print results, etc.
	Run()
}

// A helper that calls Solve, verifying it produces the expected result.
func runProblem(p Problem, expected int) {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	actual := p.Solve()
	fmt.Printf("  Solve() = %d", actual)
	if actual != expected {
		fmt.Printf("  NOT the expected value of %d!\n", expected)
	} else {
		fmt.Printf("\n")
	}
}

// A problem with multiple examples.
// A helper runs the examples, verifying they produce the expected results.
type ProblemWithExamples interface {
	Problem

	// Solve the problem with the given input
	SolveExample(input int) int
}

type ExpectedExampleResult struct {
	input    int
	expected int
}

func runProblemExamples(p ProblemWithExamples, examples []ExpectedExampleResult) {
	fmt.Printf("%s - %s\n", p.Name(), p.Desc())
	for _, example := range examples {
		actual := p.SolveExample(example.input)
		fmt.Printf("  Solve(%d) = %d", example.input, actual)
		if actual != example.expected {
			fmt.Printf("  NOT the expected value of %d!\n", example.expected)
		} else {
			fmt.Printf("\n")
		}
	}
}
