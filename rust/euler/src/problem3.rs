use prime::Sieve;

pub fn solve() -> u32 {
    solve_example(600851475143)
}

fn solve_example(value: u64) -> u32 {
    let sieve = Sieve::new();
    sieve.prime_factors(value).last().copied().unwrap() as u32
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(1), 1);
        assert_eq!(solve_example(3), 3);
        assert_eq!(solve_example(13147), 13147);
        assert_eq!(solve_example(13195), 29);
        assert_eq!(solve_example(600851475143), 6857);
    }
}
