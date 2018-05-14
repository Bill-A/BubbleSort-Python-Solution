# Bubble Sort Kata

Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.

### How Bubble Sort Works?
The Bubble sort continuously steps through a list, swapping items until they appear in the correct order. Consider this list -

[5470, 58, 19, 60, 1998, 1960, 1957]

Bubble sort starts with very first two elements, comparing them to check which one is greater.

[**5470, 58,** 19, 60, 1998, 1960, 1957]

We find that 58 is smaller than 5470 and these two values must be swapped. The new array should look like this −

[58, **5470,** 19, 60, 1998, 1960, 1957]

Next we compare 5470 and 19. We find that 19 is smaller than 5470 and these two values must be swapped. The new array should look like this −

[58, 19, **5470,** 60, 1998, 1960, 1957]

Next we compare 5470 and 60. We find that 60 is smaller than 5470 and these two values must be swapped. The new array should look like this −

[58, 19, 60, **5470,**  1998, 1960, 1957]

Next we compare 5470 and 1998. We find that 1998 is smaller than 5470 and these two values must be swapped. The new array should look like this −

[58, 19, 60, 1998, **5470,**  1960, 1957]

Next we compare 5470 and 1960. We find that 1960 is smaller than 5470 and these two values must be swapped. The new array should look like this −

[58, 19, 60, 1998, 1960, **5470,**  1957]

Next we compare 5470 and 1957. We find that 1957 is smaller than 5470 and these two values must be swapped. We find that we have reached the end of the array. After one iteration, the array should look like this −

[58, 19, 60, 1998, 1960,  1957, **5470** ]

After reaching the end of the array, we start the comparison from the begining. After the second iteration, it should look like this −

[19, **58,** 60, 1998, 1960, 1957, 5470 ]

After the third iteration, it should look like this −

[19, 58 60, 1960, 1957, **1998,** 5470 ]

After the fourth iteration, it should look like this −

[19, 58 60, **1957,** 1960, 1998, 5470 ]