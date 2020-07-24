#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) n^3 / n^2 leaves runtime of n 


b) O (log n) because the range of the second while loop is halved each iteration 

c) O(n) one or constant - just adds 2 for each bunny. One operation per call. 


## Exercise II

this is a good use case for a binary search. This would allow us to minimize the number of eggs broken in the search for the best floor. Ideally we pick the correct floor on first guess. Worst case scenario we halve the number of wrong guesses each time until we only have one choice left. 

F is not know, and this idea needs to work for an n story building. 

start halfway up the building, drop egg, check if it breaks. 

If it breaks choose a floor halfway between current floor and the ground and repeat. 

It it does not break choose a floor halfway up the building higher than the current floor, repeat. 

best case O(1) - pick the right floor first guess
average O(log n) - takes log time to get correct floor
worst O(log n) - takes log time to get correct floor


