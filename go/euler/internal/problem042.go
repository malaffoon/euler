package internal

import (
	"io/ioutil"
	"strings"
)

type Problem042 struct {
}

func (p *Problem042) Name() string {
	return "Problem 42"
}

func (p *Problem042) Desc() string {
	return "Coded triangle numbers"
}

func (p *Problem042) Solve() int {
	numbers := generateTriangleNumbers()
	words := readProblem42Words()
	count := 0
	for _, word := range words {
		value := 0
		for _, r := range word {
			value += int(r-'A') + 1
		}
		if numbers[value] {
			count++
		}
	}
	return count
}

func (p *Problem042) Run() {
	runProblem(p, 162)
}

func generateTriangleNumbers() map[int]bool {
	numbers := make(map[int]bool)
	for n := 1; n < 30; n++ {
		numbers[n*(n+1)/2] = true
	}
	return numbers
}

func readProblem42Words() []string {
	data, _ := ioutil.ReadFile("../../resources/p042_words.txt")
	rawNames := strings.Split(string(data), ",")
	names := make([]string, len(rawNames))
	for n, rawName := range rawNames {
		names[n] = strings.Trim(rawName, "\"")
	}
	return names
}
