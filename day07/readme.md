## Day 07

Woke up kinda late today.

Part 1 was easy, after I wrote the parsing functions and remembered how you sort
with a compare function in python (looked it up eh).

Part 2 was trickier, I saw some people were hand optimizing, I just bruteforced
the highest joker combo. At one point I was forgetting to reset the hand
(to have a joker instead of a concrete value) and this tripped me up for a bit,
since my answear for the sample was correct but too low for the full data.

### Refactoring

More like code golfing here, actually.

Most importantly, you can represent hand types with a number, and full house as 3.5
I shortened the dictionary definitions, the comparison function, and the end sum.

For part 2, I also unwrapped the loop a bit, making it a whole lot slower
(0.42s vs 0.08s on my MacBook M1) but slightly more readable.
