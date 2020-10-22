pub fn solve() -> u32 {
    solve_example(1000)
}

fn solve_example(limit: u32) -> u32 {
    (1..limit).filter(|n| n % 3 == 0 || n % 5 == 0).sum()
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
