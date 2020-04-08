use std::cell::{ RefCell, Ref };
use bitvec::prelude::*;

// TODO - thread safety; use RwLock instead of RefCell?
pub struct Sieve {
    _sieve: RefCell<BitVec>,
}

// TODO - introduce a Primes interface? Useful for Atkins, Miller-Rabin, whatever

impl Sieve {
    pub fn new() -> Sieve {
        Sieve::new_with_limit(10)
    }

    pub fn new_with_limit(limit: usize) -> Sieve {
        let sieve = Sieve { _sieve: RefCell::new(bitvec![0, 0, 1, 1, 0, 1, 0, 1, 0, 0]) };
        sieve._ensure_limit(limit);
        sieve
    }

    /// Return all primes up to the given value.
    ///
    /// # Arguments
    /// `limit` - the maximum value
    ///
    /// # Examples
    /// ```
    /// # use prime::Sieve;
    /// # let sieve = Sieve::new();
    /// assert_eq!(sieve.primes(30), vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29]);
    /// ```
    pub fn primes(&self, limit: usize) -> Vec<u64> {
        self._ensure_limit(limit).iter().enumerate()
            .filter_map(|(i, flag)| if *flag { Some(i as u64) } else { None })
            .collect::<Vec<u64>>()
    }

    /// Determine if the given number is prime.
    ///
    /// # Arguments
    /// `n` - number to check
    ///
    /// # Examples
    /// ```
    /// # use prime::Sieve;
    /// # let sieve = Sieve::new();
    /// assert_eq!(sieve.is_prime(29), true);
    /// assert_eq!(sieve.is_prime(30), false);
    /// ```
    pub fn is_prime(&self, n: u64) -> bool {
        self._ensure_limit(1 + n as usize)[n as usize]
    }

    /// Return nth prime.
    ///
    /// # Arguments
    /// `n` - which prime to return, 1-based
    ///
    /// # Examples
    /// ```
    /// # use prime::Sieve;
    /// # let sieve = Sieve::new();
    /// assert_eq!(sieve.nth_prime(3), 5);
    /// assert_eq!(sieve.nth_prime(10), 29);
    /// assert_eq!(sieve.nth_prime(1000), 7919);
    /// ```
    pub fn nth_prime(&self, n: usize) -> u64 {
        self._ensure_limit(Sieve::_estimate_limit(n)).iter().enumerate()
            .filter(|(_, flag)| **flag)
            .skip(n-1)
            .next().unwrap().0 as u64
    }

    /// Return the prime factors of the given number.
    /// The factors will be in ascending order.
    ///
    /// # Arguments
    /// `n` - number to factor
    ///
    /// # Examples
    /// ```
    /// # use prime::Sieve;
    /// # let sieve = Sieve::new();
    /// assert_eq!(sieve.prime_factors(8), vec![2, 2, 2]);
    /// assert_eq!(sieve.prime_factors(100), vec![2, 2, 5, 5]);
    /// ```
    pub fn prime_factors(&self, n: u64) -> Vec<u64> {
        if n <= 3 {
            vec![n]
        } else {
            let mut factors = vec![];
            let mut value = n;
            // TODO - this calculates all primes up to sqrt even if not necessary
            // TODO   e.g. performance impact for problem 3
            for (p, _) in self._ensure_limit(1 + (n as f32).sqrt().floor() as usize)
                .iter().enumerate().filter(|(_, flag)| **flag) {
                let prime: u64 = p as u64;
                while value > 1 && value % prime == 0 {
                    factors.push(prime);
                    value /= prime;
                }
                if value == 1 || value < prime * prime {
                    break;
                }
            }
            if value > 1 {
                factors.push(value);
            }
            factors
        }
    }

    // ensure sieve is populated and return (immutable) ref to it
    fn _ensure_limit(&self, limit: usize) -> Ref<BitVec> {
        if (*self._sieve.borrow()).len() < limit {
            let mut sieve = self._sieve.borrow_mut();
            sieve.resize(limit, true);
            for i in 2..limit {
                if sieve[i] {
                    for j in (i*i..limit).step_by(i) {
                        sieve.set(j,false);
                    }
                }
            }
        }
        self._sieve.borrow()
    }

    fn _estimate_limit(n: usize) -> usize {
        if n < 10 {
            30
        } else {
            let n: f32 = n as f32;
            (n * (n.ln() + n.ln().ln())).ceil() as usize
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Sieve;

    #[test]
    fn test_primes() {
        let sieve = Sieve::new();
        assert_eq!(sieve.primes(10), vec![2, 3, 5, 7]);
        assert_eq!(sieve.primes(30), vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    }

    #[test]
    fn test_is_prime() {
        let sieve = Sieve::new();
        assert_eq!(sieve.is_prime(100), false);
        assert_eq!(sieve.is_prime(17), true);
        assert_eq!(sieve.is_prime(4), false);
    }

    #[test]
    fn test_nth_prime() {
        let sieve = Sieve::new();
        assert_eq!(sieve.nth_prime(1000), 7919);
        assert_eq!(sieve.nth_prime(10), 29);
        assert_eq!(sieve.nth_prime(3), 5);
    }

    #[test]
    fn test_prime_factors() {
        let sieve = Sieve::new();
        assert_eq!(sieve.prime_factors(8), vec![2, 2, 2]);
        assert_eq!(sieve.prime_factors(100), vec![2, 2, 5, 5]);
    }
}