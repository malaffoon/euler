mod problem001;
mod problem002;
mod problem003;
mod problem004;
mod problem005;
mod problem006;
mod problem007;
mod problem008;

// use automod to pull in all problem modules
// TODO - problem with this is CLion doesn't know modules are attached to crate
// automod::dir!("src");

fn main() {
    let problems: Vec<fn() -> u64> = vec![
        problem001::solve, problem002::solve, problem003::solve, problem004::solve,
        problem005::solve, problem006::solve, problem007::solve, problem008::solve,
    ];
    for (i, p) in problems.iter().enumerate() {
        let start = std::time::Instant::now();
        let actual = p();
        let elapsed = start.elapsed();
        println!("Problem {}: {} ({:?})", i+1, actual, elapsed);
    }
}
