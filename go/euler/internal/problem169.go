package internal

import (
	"math/big"
)

type Problem169 struct {
	big0  *big.Int
	big1  *big.Int
	big2  *big.Int
	cache map[string]int
}

func (p *Problem169) Name() string {
	return "Problem 169"
}

func (p *Problem169) Desc() string {
	return "Exploring the number of different ways a number can be expressed as a sum of powers of 2"
}

func (p *Problem169) Solve() int {
	// from python notes, the diatomic series:
	// a(0)=0, a(1)=1, a(2n)=a(n), a(2n+1)=a(n)+a(n+1)
	// 0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, ...
	bn := big.NewInt(10)
	bn = bn.Exp(bn, big.NewInt(25), nil)

	p.big0 = big.NewInt(0)
	p.big1 = big.NewInt(1)
	p.big2 = big.NewInt(2)
	// seed the cache with powers of 2 (which have exactly 1 way)
	p.cache = make(map[string]int)
	for i := 0; i < 25; i++ {
		e := big.NewInt(2)
		e = e.Exp(e, big.NewInt(int64(i)), nil)
		p.cache[e.String()] = 1
	}

	// NOTE, there is an offset from that series and our problem, so add 1 to input
	bn = bn.Add(bn, p.big1)
	return p.a(bn)
}

func (p *Problem169) Run() {
	runProblem(p, 178653872807)
}

// recursive, memoizing helper
func (p *Problem169) a(n *big.Int) int {
	key := n.String()
	v, found := p.cache[key]
	if !found {
		k := big.NewInt(0)
		m := big.NewInt(0)
		k, m = k.DivMod(n, p.big2, m)
		if m.Cmp(p.big0) == 0 {
			v = p.a(k)
		} else {
			v = p.a(k)
			k = k.Add(k, p.big1)
			v += p.a(k)
		}
		p.cache[key] = v
	}
	return v
}
