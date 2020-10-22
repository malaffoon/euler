use std::time::Instant;

mod problem1;
mod problem2;
mod problem3;

fn main() {
    let problems: Vec<fn() -> u32> = vec![
        problem1::solve, problem2::solve, problem3::solve
    ];
    for (i, p) in problems.iter().enumerate() {
        let start = Instant::now();
        let actual = p();
        let elapsed = start.elapsed();
        println!("Problem {}: {} ({:?})", i+1, actual, elapsed);
    }
}
