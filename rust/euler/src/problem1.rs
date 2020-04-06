pub fn solve(limit: u32) -> u32 {
    (1..limit).filter(|n| n % 3 == 0 || n % 5 == 0).sum()
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn it_works() {
        assert_eq!(solve(10), 23);
        assert_eq!(solve(1000), 233168);
    }
}
