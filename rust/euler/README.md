I'm not quite sure how to organize things for this project.
Eventually, i'd like a problem runner of some sort, which implies a Problem interface.
For now, each problem will have a module in euler/src with a test demonstrating that it works.
There will also be utils, each in their own sub-folder.

Currently, the main function times each problem's solve method and prints the result.
Each problem has tests for the examples given in the description.
```bash
# from the rust/euler folder, with all arguments explicit:
cargo run --package euler --bin euler --release
# or, the lazy, non optimized version:
cargo run

# To run a problem's tests (examples)
cargo test problem007 
```


To get here, i created the main project and utility lib projects:
```bash
cargo new euler
cargo new euler/prime --lib
cargo new euler/collatz --lib
...
```
Then i modified the dependencies in euler/Cargo.toml.

TODO
* Problem interface: name(), desc(), solve()
    * it would be nice if solve() could return different int types (i32, u64, etc.)


