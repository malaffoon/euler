use fibonacci::fibonacci;

pub fn solve() -> u32 {
    solve_example(4_000_000)
}

fn solve_example(max_value: u32) -> u32 {
    fibonacci().filter(|n| n % 2 == 0).take_while(|n| n < &max_value).sum()
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(100), 44);
        assert_eq!(solve_example(4_000_000), 4_613_732);
    }
}
