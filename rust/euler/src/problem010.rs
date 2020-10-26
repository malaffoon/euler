use prime::Sieve;

pub fn solve() -> u64 {
    solve_example(2000000)
}

fn solve_example(n: u32) -> u64 {
    let mut sum: u64 = 0;
    for prime in Sieve::new().primes(n as usize) {
        sum += prime
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(10), 17);
        assert_eq!(solve_example(2000000), 142913828922);
    }
}
