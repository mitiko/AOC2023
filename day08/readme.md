## Day 08

Woke up 45 minutes late again, forgot to set my alarm and stayed till late
yesterday.

Part 1 was quick and simple, although I suspected I'd need to unroll the list,
naive python solution was fast enough.

Part 2 was trickier. I coded it up and immediately saw it's going to be too slow
to just simulate the process. I needed to find a loop. At first I thought I may
unroll the list and see how much I move left or write for a single iteration of
all ops (way harder), but then I noticed I only need the cycle lengths of each
chain. Then you can use the [chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
to find when they'll all meet. However, it turned out all chains are the same
length on the first iteration and on each subsequent one, making it a
[LCM](https://en.wikipedia.org/wiki/Least_common_multiple) problem instead of a CRT.
