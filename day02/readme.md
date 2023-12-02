## Day 02

I was pretty slow on parsing logic but at least I didn't have to modify much for
part 2.

For part 1, I panicked and did a simple for-loop that short-circuits.

For part 2, just modify the samples check, and compute powers instead of game
ids

### Refactoring

For part 1, I extracted the parsing and acceptance criteria code into seperate
functions, I'm also using a dictionary for the colors instead of variables.

For part 2, having the parse function simplifies things a lot, and I wouldn't've
written the maxc function as cleanly if I hadn't already solved it.

Overall, good reminder to extract parse functions. Ends up being easier to work
with and reason about.
