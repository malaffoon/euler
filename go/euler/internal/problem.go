package internal

type Problem interface {
	// Solve the problem, returning the answer.
	// This is called by the wrapper command that times performance.
	Solve() int

	// Run the problem; this may run examples, print results, etc.
	Run()
}
