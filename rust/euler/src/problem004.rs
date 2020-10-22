pub fn solve() -> u64 {
    let mut result: u64 = 0;
    for i in 900..1000 {
        for j in i..1000 {
            let value: u64 = i * j;
            if value == reverse(value) && value > result {
                result = value
            }
        }
    }
    return result
}

fn reverse(n: u64) -> u64 {
    let mut result: u64 = 0;
    let mut value = n;
    while value > 0 {
        result = 10 * result + value % 10;
        value /= 10
    }
    result
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn it_works() {
        assert_eq!(solve(), 906609);
    }
}
