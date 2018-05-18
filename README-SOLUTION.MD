# Bubble Sort Kata Solution

Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.

### Solving the Algorithm ... Test-First?
Considering this list -

> [5470, 58]

The easiest way to make the test pass is to return 
> [58, 5470]

Next, let's consider this list of three elements - 

> [5470, 58, 19]

For the first iteration of continuously stepping through the list, we will use a "for loop" and an "if" statement; swapping adjacent items until we have traversed the entire list. 

Next, let's write some tests to determine if we are correctly swapping adjacent elements into numerical order during the first iteration through the list.

Consider these lists of elements - 

> [1, 2, 3] should be [1, 2, 3]

> [1, 3, 2] should be [1, 2, 3]

> [5470, 58, 19, 60] should be [58, 19, 60, 5470]


Next, let's write a test for the functionality to fully sort the list. We must iterate through the list until no more swapping is required.
To accomplish multiple iterations, let's implement a "do while(not sorted)". As python does not have a "do while()" we will emulate this construct.

Consider this list of elements - 

> [5470, 58, 19, 60] should be [58, 19, 60, 5470]

##### Note: At this point many of the previous tests will fail. Explain why. Also,these now failing tests are removed.
