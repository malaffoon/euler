// TODO - Think this is a good idea?
// TODO   It complicates things but would allow for more explicit behaviors
trait Problem {
    fn name() -> String;
    fn desc() -> String;
    fn solve() -> u64;
}
