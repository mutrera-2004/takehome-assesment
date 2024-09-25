## Question
I'm answering question #1.

## Solution 1:

### Reasoning
I went through the list once in the for loop and for each element, I sliced the rest of the list. If the element 'i' in question is in the sliced list, then that 'i' value is the repeated integer. 

### Time complexity
The solution loops over the entire list, but it also loops over the sliced list. So, the time complexity is:

\[ O(N^2) \]

### Space Complexity:
The solution uses a constant amount of extra space so the space complexity is: 

\[ O(1) \]


## Solution 2:

### Reasoning
I sorted the list using a built-in method and then looped through the list by selecting pairs. If a pair 'i' and 'i + 1' are both the same number, that means 'i' is the repeated integer.

### Time Complexity
The time complexity of the Timsort method is:

\[ O(n*log(n)) \]

The time complexity of the posterior 'for' loop is: 

\[ O(N) \]

### Space Complexity:
Due to the Timsort algorithm and the 'for' loop the space complexity is:

\[ O(N) \]

## Running tests
Simply run the tests.py file. 

**Disclaimer:** I am not well versed in any test frameworks, so I only utilized assert statements to check
for the correct output. If all test pass, I added a statement indicating so. Otherwise there will be an AssertionError.

**Sources:**
- https://towardsdatascience.com/sorting-algorithms-with-python-4ec7081d78a1
- https://www.geeksforgeeks.org/timsort/