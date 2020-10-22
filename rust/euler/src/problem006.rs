pub fn solve() -> u64 {
    solve_example(100)
}

fn solve_example(n: u32) -> u64 {
    return (n * (n + 1) * (n - 1) * (3*n + 2) / 12) as u64
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(10), 2640);
        assert_eq!(solve_example(100), 25164150);
    }
}
