package internal

import (
	"io/ioutil"
	"sort"
	"strings"
)

type Problem022 struct {
}

func (p *Problem022) Name() string {
	return "Problem 22"
}

func (p *Problem022) Desc() string {
	return "Names scores"
}

func (p *Problem022) Solve() int {
	names := readProblem22Names()
	sort.Strings(names)
	sum := 0
	for n, name := range names {
		for _, r := range name {
			sum += (n + 1) * int(r-'A'+1)
		}
	}
	return sum
}

func (p *Problem022) Run() {
	runProblem(p, 871198282)
}

func readProblem22Names() []string {
	data, _ := ioutil.ReadFile("../../resources/p022_names.txt")
	rawNames := strings.Split(string(data), ",")
	names := make([]string, len(rawNames))
	for n, rawName := range rawNames {
		names[n] = strings.Trim(rawName, "\"")
	}
	return names
}
