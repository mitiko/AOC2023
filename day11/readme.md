## Day 11

For part 1, I had this clever idea that it's easier to add rows than it is to add
columns, so we can just transpose the ~matrix~ grid and repeat the expansion.
Then the distance function is a quick trip to [Wikipedia](https://en.wikipedia.org/wiki/Taxicab_geometry).

For part 2, you have to use math - aka the classic AOC switcheroo - write it
fast with data, then use math for part 2. I think I figured it pretty quickly
that you can just count the expanding rows/cols and modify the distance function
itself (rather than the "universe"), and it's probably a lot similar to how
scientists would do it IRL.
