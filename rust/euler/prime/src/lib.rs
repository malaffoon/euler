/// Calculate a limit for the nth prime.
/// It will always return a value greater than the actual value.
/// This can be used to size the sieve vector.
///
/// # Arguments
/// * `n` - the nth prime
///
/// # Examples
/// For n < 10, it always returns 30; the 10th prime number is 29.
/// The 1000th prime number is 7919
/// ```
/// # use prime::guess_limit;
/// assert_eq!(guess_limit(6), 30);
/// assert_eq!(guess_limit(1000), 8841);
/// ```
pub fn guess_limit(n: u32) -> usize {
    if n < 10 {
        30
    } else {
        let n: f32 = n as f32;
        (n * (n.ln() + n.ln().ln())).ceil() as usize
    }
}

/// Use the Sieve of Eratosthenes to calculate all primes up to the given value.
///
/// NOTE: there is no caching of values, this recalculates the sieve for every call.
///
/// # Arguments
/// 'limit' - the maximum value
///
/// # Examples
/// ```
/// # use prime::prime_sieve;
/// assert_eq!(prime_sieve(30), vec!(2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
/// ```
pub fn prime_sieve(limit: usize) -> Vec<u32> {
    let mut sieve: Vec<bool> = vec![true; limit+1];
    sieve[0] = false;
    sieve[1] = false;
    for i in 0..=((limit as f32).sqrt().ceil() as usize) {
        if !sieve[i] { continue; }
        for j in (i*i..=limit).step_by(i) {
            sieve[j] = false;
        }
    }
    sieve.into_iter().enumerate()
        .filter_map(|(i, p)| if p {Some(i as u32)} else {None})
        .collect::<Vec<u32>>()
}


#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
