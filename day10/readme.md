## Day 10

This was a fun one!!
I slept in till like 09:30 (which is 02:30 after start time) but I think I did
well on part 2 which is more important.

For part 1, I knew I needed a graph, then all of the searching algorithms start
to apply. Parsed the grid, and did a modified BFS that tracks distance (and
reruns the node if the distance has lowered). It's probably not optimal to
search like that but I can't do A* or Dijkstra from memory, plus it's good
enough.  
I only had one subtle bug where I didn't do the starting tile properly, and
instead allowed all directions for first step but when I debugged (with the
visualizer) I handled it properly.

For part 2, I was stumbled for a while. Didn't have a clear idea on how to do it
at first. At some point my math thinking kicked in and I got the idea of
imagining a flowing _river_ along the tubes. Areas with a "_positive_" flow,
going clockwise let's say, would be on one side of the tubing and "_negative_"
flow on the other. This was kinda genius of me I think, I have yet to check
other solutions but it feels like it's the only proper way to do it. Also it's a
pretty generic problem, many must have thought about it before.  
From then on, I could've used one of those islands graph algs to get which
regions of `'.'` are all together, and track its bounding walls to determing the
direction of the flow. I'd also have to handle the case where the bounds are the
grid itself..  
So I coded up the flow tracking - it's sorta like BFS except it's not and it's
just a simple loop. I didn't write the ending properly a first, which meant the
directions for the starting tube were not correct but I knew about it and had
one dirty speed hack around it when that ended up being a problem on the samples -
this is what the `switch` is for.
Then instead of tracking the regions, I just probed all directions from each
blank `'.'` and recorded a clock direction for it. I also had to fix the
assumption that all tubes are part of the maze (which was clearly indicated
anyway, I just simplified - fixed by using `in_loop` set)
