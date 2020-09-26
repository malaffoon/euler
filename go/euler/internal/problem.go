package internal

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
