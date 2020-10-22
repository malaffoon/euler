pub fn solve() -> u64 {
    solve_example(1000)
}

fn solve_example(limit: u32) -> u64 {
    (1..limit).filter(|n| n % 3 == 0 || n % 5 == 0).sum::<u32>() as u64
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(10), 23);
        assert_eq!(solve_example(1000), 233168);
    }
}
