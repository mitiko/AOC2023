## Day 01

Relatively easy for day 1, although harder than last year's.

For part 1, I knew I could do it with a regex but I forgot the syntax so I just
hardcoded the digits and it was fine.

For part 2, I now had to use regex. One issue I ran into was the fact regex
matching is lazy, so with interlapping matches the last match is not what you
want it to be.
Instead of fighting the state machine mechanics (I'm not building an FSM for
this, come on) I created this terrible hack, where I'd reverse the string and
also reverse all the patterns, so that the first match is actually the last.
Then you just modify the word lookup dictionary and you're done.

### Refactoring

For part 1, using regex is obviously way shorter.

For part 2, I built the pattern from the dictionary and wrote the key reversal
in code, rather than by hand.

Nothing tweaked on the algos, just make them shorter.
