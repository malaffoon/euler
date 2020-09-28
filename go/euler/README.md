# Project Euler - Go

This is my first foray into Go. Wish me luck.

NOTE: I started Project Euler with Python. As such, many of my thoughts are captured in those files.
When solving the problems in Rust, Go, and other languages, i just copied the approach from Python
without much comment. So, if you don't understand something in Go, look for the Python solution. 

I haven't figured out a good framework for running and timing the solutions. I'd like it to:
* run and time a single problem's solution
* run a single problem's examples (including solution example)
* run and time all problems' solutions (and/or a subset of them)
* run all problems' examples 
* verify all the examples of all the problems are still being calculated correctly
* not be overly complex unless that teaches me something about Go

I need to learn more about Go's best practices. Should the examples be handled as tests?
Go is all about performance, so there are probably tools/utils for that.
Looks like there are TestXxx and BenchmarkXxx functions that are invoked by go flags.
See https://golang.org/pkg/testing/

Anyway, for now, you can run all the problems' examples by doing
```bash
go run cmd/main.go
```

### TODO
* figure out framework for running and timing some or all problems
* i'm using problem pointers to avoid copying problem objects, not to mutate them. What is best practice?


### Useful Links
* https://golang.org/
    * https://golang.org/pkg/
    * https://golang.org/pkg/math/
* http://www.golangpatterns.info/home