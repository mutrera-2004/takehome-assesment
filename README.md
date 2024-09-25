## Question
I'm answering question #1.

## Solution 1:

### Reasoning
I went through the list once in the for loop and for each element, I sliced the rest of the list. If the element 'i' in question is in the sliced list, then that 'i' value is the repeated integer. 

### Time complexity
The solution loops over the entire list, but it also loops over the sliced list. So, the time complexity is:

\[ O(N) + O(N - 1) + O(N - 2) + ... + O(1) = O(N^2) \]

### Space Complexity:
The solution uses a constant amount of extra space so the space complexity is: 

\[ O(1) \]


## Solution 2:

### Reasoning
I sorted the list using a built-in method and then looped through the list by selecting pairs. If a pair 'i' and 'i + 1' are both the same number, that means 'i' is the repeated integer.

### Time Complexity
The time complexity of the Timsort method is:

\[ O((N + 1) \log(N + 1)) \]

The time complexity of the posterior 'for' loop is: 

\[ O(N) \]

In conclusion, the total time complexity is:

\[ O(N \log N) \]

### Space Complexity:
Due to the Timsort algorithm, the space complexity is:

\[ O(N) \]

## Running tests
On the CLI, paste the following: 
python3 -m unittest tests.py

**Disclaimer:** I used chatGPT to implement the testing framework (the test cases are mine), and to calculate the time and space complexities of both solutions.