pub fn solve() -> u64 {
    solve_example(1000)
}

fn solve_example(n: u64) -> u64 {
    let a_max = n / 3;
    let mut a = 1;
    while a < a_max {
        let b = (n*n-2*a*n) as f64 / (n-a) as f64 / 2.;
        if b.fract() == 0. {
            let b_int = b.trunc() as u64;
            return a * b_int * (n - a - b_int)
        }
        a += 1;
    }
    return 0;
}

#[cfg(test)]
mod tests {
    use super::solve_example;

    #[test]
    fn it_works() {
        assert_eq!(solve_example(12), 60);
        assert_eq!(solve_example(1000), 31875000);
    }
}
