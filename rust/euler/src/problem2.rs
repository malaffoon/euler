use fibonacci::fibonacci;

pub fn solve(max_value: u32) -> u32 {
    fibonacci().filter(|n| n % 2 == 0).take_while(|n| n < &max_value).sum()
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn it_works() {
        assert_eq!(solve(100), 44);
        assert_eq!(solve(4_000_000), 4_613_732);
    }
}
