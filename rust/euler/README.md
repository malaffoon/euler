I'm not quite sure how to organize things for this project.
Eventually, i'd like a problem runner of some sort, which implies a Problem interface.
For now, each problem will have a module in euler/src with a test demonstrating that it works.
There will also be utils, each in their own sub-folder.
The main function will call each problem's solve method with the required parameters and print the result.

To get here, i created the main project and utility lib projects:
```bash
cargo new euler
cargo new euler/prime --lib
cargo new euler/collatz --lib
...
```
Then i modified the dependencies in euler/Cargo.toml.

