use prime::Sieve;

pub fn solve(value: u64) -> u64 {
    let sieve = Sieve::new();
    sieve.prime_factors(value).last().copied().unwrap()
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn it_works() {
        assert_eq!(solve(1), 1);
        assert_eq!(solve(3), 3);
        assert_eq!(solve(13147), 13147);
        assert_eq!(solve(13195), 29);
        assert_eq!(solve(600851475143), 6857);
    }
}
