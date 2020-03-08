Assignment 3 Floyd-Warshall Report
From Justen Donzello

The biggest problem I had when completing this assignment was placing the correct variables that the parallel algorithm needed.
I was having different kind of errors that occurred. I was having trouble why these errors were occurring and it was difficult to troubleshoot since it was a parallelized.

Another problem I was having and still have is how to separate the parallel part from the part where I was trying to calculate the time.
For the performance stances, I just add all the time each thread takes to get the total time but I feel like there should be an easier way.
Solving this problem could probably help me solve the extra credit part as well.

I worked on this assignment for about 3-4 hours. I quickly wrote out the code but most of my time was dedicated to debugging the code. .

Performance Stats:
1 Thread - 0.0001 - 0.0006
2 Threads - 0.006 - 0.02
4 Threads - 0.04 - 0.08
8 Threads - 0.2 - 0.4

With more threads the program seems to be taking more time. I believe that this is probably due to the fact that I placed the time functions in the incorrect spot.
Or that the time complexity of each thread is pretty high. 
