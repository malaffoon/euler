use prime::Sieve;

pub fn solve() -> u64 {
    solve_example(10001)
}

fn solve_example(n: u32) -> u64 {
    Sieve::new().nth_prime(n as usize)
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(100), 541);
        assert_eq!(solve_example(1000), 7919);
        assert_eq!(solve_example(10001), 104743);
    }
}
