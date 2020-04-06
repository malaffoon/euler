#[derive(Debug, Eq, PartialEq)]
pub struct Fibonacci {
    curr: u32,
    next: u32,
}

impl Iterator for Fibonacci {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        let temp = self.curr + self.next;
        self.curr = self.next;
        self.next = temp;
        Some(self.curr)
    }
}

// TODO - reread https://blog.jcoglan.com/2019/04/22/generic-returns-in-rust/
// TODO   and figure out exactly what i should be implementing in here
// impl From<Fibonacci> for u32 {
//     fn from(f: Fibonacci) -> Self {
//         f.curr
//     }
// }

/// Returns a Fibonacci sequence generator
pub fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

/// Return the nth Fibonacci number.
/// Presumes sequence starts with 1, i.e. 1,1,2,3,5,8,13,21,34,55,...
/// so the 10th fibonacci number is 55.
///
/// Uses Binet's formula so is faster than navigating the series.
///
/// # Arguments
/// `n` - 1-based n
pub fn fibn(n: u32) -> u32 {
    let sqrt5: f64 = 5f64.sqrt();
    let phi: f64 = (1.0 + sqrt5) / 2.0;

    (0.5f64 + phi.powi(n as i32) / sqrt5).floor() as u32
}

#[cfg(test)]
mod tests {
    use super::fibn;
    use super::fibonacci;

    #[test]
    fn test_iterator() {
        assert_eq!(fibonacci().take(4).collect::<Vec<_>>(), vec![1,1,2,3]);
        assert_eq!(fibonacci().skip(7).take(3).collect::<Vec<_>>(), vec![21,34,55]);
    }

    #[test]
    fn test_fibn() {
        assert_eq!(fibn(10), 55);
        assert_eq!(fibn(20), 6_765);
        assert_eq!(fibn(30), 832_040);
        assert_eq!(fibn(40), 102_334_155);
    }
}
