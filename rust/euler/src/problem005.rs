pub fn solve() -> u64 {
    solve_example(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
}

fn solve_example(values: Vec<u32>) -> u64 {
    let mut result: u64 = values[0] as u64;
    for v in values {
        result = num::integer::lcm(result, v as u64);
    }
    return result
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2520);
        assert_eq!(solve_example(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 232792560);
    }
}
