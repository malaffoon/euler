package internal

import (
	"bytes"
)

var Problem17Number = []string{
	"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
	"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
}

var Problem17Tens = []string{
	"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
}

type Problem017 struct {
}

func (p *Problem017) Name() string {
	return "Problem 17"
}

func (p *Problem017) Desc() string {
	return "Number letter counts"
}

func (p *Problem017) Solve() int {
	return p.SolveExample(1000)
}

func (p *Problem017) Run() {
	runProblemExamples(p, []ExpectedExampleResult{
		{5, 19},
		{1000, 21124},
	})
}

func (p *Problem017) SolveExample(maxN int) int {
	sum := 0
	for n := 1; n <= maxN; n++ {
		for _, ch := range words(n) {
			if ch != ' ' {
				sum++
			}
		}
	}
	return sum
}

func words(n int) string {
	var buf bytes.Buffer

	switch {
	case n < 1:
	case n < 20:
		buf.WriteString(Problem17Number[n])
	case n < 100:
		buf.WriteString(Problem17Tens[n/10])
		if n%10 != 0 {
			buf.WriteString(" ")
			buf.WriteString(Problem17Number[n%10])
		}
	case n < 1000:
		buf.WriteString(Problem17Number[n/100])
		buf.WriteString(" hundred")
		if n%100 != 0 {
			buf.WriteString(" and ")
			buf.WriteString(words(n % 100))
		}
	case n == 1000:
		buf.WriteString("one thousand")
	}
	return buf.String()
}
