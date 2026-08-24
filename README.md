# DAA - Sorting, Searching, Factorial and Dynamic Programming Algorithms in Python

This repository contains Python implementations of fundamental Sorting, Searching, Factorial, and Dynamic Programming Algorithms as part of the Design and Analysis of Algorithms (DAA) Laboratory.

Each program:

* Takes input from the user
* Performs the required operation
* Displays the result
* Displays Best, Average, and Worst Case Time Complexity
* Displays Space Complexity
* Measures execution time


--------------------------------------------------
ALGORITHMS INCLUDED
--------------------------------------------------

Sorting Algorithms

1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Merge Sort
5. Quick Sort
6. Max Heap Sort

Searching Algorithms

7. Linear Search
8. Binary Search

Factorial Algorithms

9. Factorial using Iterative Method
10. Factorial using Recursive Method

Dynamic Programming

11. Making Change Problem


==================================================
SORTING ALGORITHMS
==================================================

1. BUBBLE SORT
--------------------------------------------------

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

File:

bubblesort.py

Time Complexity:

Best Case       : O(n)
Average Case    : O(n²)
Worst Case      : O(n²)

Space Complexity:

O(1)


--------------------------------------------------
2. INSERTION SORT
--------------------------------------------------

Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

File:

insertionsort.py

Time Complexity:

Best Case       : O(n)
Average Case    : O(n²)
Worst Case      : O(n²)

Space Complexity:

O(1)


--------------------------------------------------
3. SELECTION SORT
--------------------------------------------------

Selection Sort repeatedly finds the smallest element from the unsorted part and places it at the beginning.

File:

selectionsort.py

Time Complexity:

Best Case       : O(n²)
Average Case    : O(n²)
Worst Case      : O(n²)

Space Complexity:

O(1)


--------------------------------------------------
4. MERGE SORT
--------------------------------------------------

Merge Sort uses the Divide and Conquer technique. It divides the array into smaller parts, sorts them, and then merges them.

File:

mergesort.py

Time Complexity:

Best Case       : O(n log n)
Average Case    : O(n log n)
Worst Case      : O(n log n)

Space Complexity:

O(n)


--------------------------------------------------
5. QUICK SORT
--------------------------------------------------

Quick Sort uses the Divide and Conquer technique. It selects a pivot and partitions the array around the pivot.

File:

quicksort.py

Time Complexity:

Best Case       : O(n log n)
Average Case    : O(n log n)
Worst Case      : O(n²)

Space Complexity:

O(log n) average case due to recursion.


--------------------------------------------------
6. MAX HEAP SORT
--------------------------------------------------

Max Heap Sort is a comparison-based sorting algorithm that uses a Max Heap data structure.

The algorithm first builds a Max Heap and then repeatedly moves the largest element to the end of the array.

File:

maxheapsort.py

Time Complexity:

Best Case       : O(n log n)
Average Case    : O(n log n)
Worst Case      : O(n log n)

Space Complexity:

O(log n) due to recursive max_heapify().


==================================================
SEARCHING ALGORITHMS
==================================================

7. LINEAR SEARCH
--------------------------------------------------

Linear Search checks each element of the array one by one until the required element is found or the end of the array is reached.

File:

linear search.py

Time Complexity:

Best Case       : O(1)
Average Case    : O(n)
Worst Case      : O(n)

Space Complexity:

O(1)

Features:

* Takes the number of elements as input.
* Takes array elements from the user.
* Takes the element to be searched.
* Displays the position of the element if found.
* Displays the time complexity.
* Measures execution time.


--------------------------------------------------
8. BINARY SEARCH
--------------------------------------------------

Binary Search is an efficient searching algorithm that repeatedly divides the search range into two halves.

The program sorts the input array before performing Binary Search.

File:

binary search.py

Time Complexity:

Best Case       : O(1)
Average Case    : O(log n)
Worst Case      : O(log n)

Space Complexity:

O(1)

Features:

* Takes the number of elements as input.
* Takes array elements from the user.
* Sorts the array before searching.
* Takes the element to be searched.
* Displays the sorted array.
* Displays the position of the element if found.
* Displays the time complexity.
* Measures execution time.


==================================================
FACTORIAL ALGORITHMS
==================================================

9. FACTORIAL USING ITERATIVE METHOD
--------------------------------------------------

The iterative method calculates the factorial using a for loop.

File:

factorial_iterative.py

Example:

For n = 5:

5! = 5 × 4 × 3 × 2 × 1 = 120

Time Complexity:

Best Case       : O(n)
Average Case    : O(n)
Worst Case      : O(n)

Space Complexity:

O(1)

The iterative method uses less memory because it does not require recursive function calls.


--------------------------------------------------
10. FACTORIAL USING RECURSIVE METHOD
--------------------------------------------------

The recursive method calculates the factorial by calling the same function repeatedly until the base condition is reached.

File:

factorial_recursive.py

Example:

For n = 5:

5! = 5 × 4 × 3 × 2 × 1 = 120

Time Complexity:

Best Case       : O(n)
Average Case    : O(n)
Worst Case      : O(n)

Space Complexity:

O(n)

The recursive method requires additional stack space for each recursive function call.


==================================================
MAKING CHANGE USING DYNAMIC PROGRAMMING
==================================================

11. MAKING CHANGE PROBLEM
--------------------------------------------------

The Making Change Problem finds the minimum number of coins required to make a given amount using the available coin denominations.

The problem is solved using the Dynamic Programming approach.

File:

making_change.py


--------------------------------------------------
PROBLEM DESCRIPTION
--------------------------------------------------

Given a set of coin denominations and a target amount, find the minimum number of coins required to make the target amount.

Example:

Coin Denominations: 1, 2, 5
Amount: 11

Solution:

5 + 5 + 1 = 11

Minimum Number of Coins = 3


--------------------------------------------------
HOW THE ALGORITHM WORKS
--------------------------------------------------

1. Create a DP array of size amount + 1.
2. Initialize all values with infinity.
3. Set dp[0] = 0 because zero coins are needed to make amount 0.
4. For every amount from 1 to the target amount:
   - Check every available coin.
   - If the coin value is less than or equal to the current amount, calculate the minimum number of coins.
5. The final value dp[amount] gives the minimum number of coins required.


--------------------------------------------------
COMPLEXITY
--------------------------------------------------

Let:

n = Number of coin denominations
amount = Target amount

Best Case       : O(n * amount)
Average Case    : O(n * amount)
Worst Case      : O(n * amount)

Space Complexity:

O(amount)


==================================================
ALGORITHMS COMPARISON
==================================================

SORTING ALGORITHMS

Algorithm       Best Case    Average Case    Worst Case    Space

Bubble Sort     O(n)         O(n²)           O(n²)         O(1)
Insertion Sort  O(n)         O(n²)           O(n²)         O(1)
Selection Sort  O(n²)        O(n²)           O(n²)         O(1)
Merge Sort      O(n log n)   O(n log n)      O(n log n)    O(n)
Quick Sort      O(n log n)   O(n log n)      O(n²)         O(log n) Average
Max Heap Sort   O(n log n)   O(n log n)      O(n log n)    O(log n)


SEARCHING ALGORITHMS

Algorithm       Best Case    Average Case    Worst Case    Space

Linear Search   O(1)         O(n)            O(n)          O(1)
Binary Search   O(1)         O(log n)        O(log n)      O(1)


FACTORIAL ALGORITHMS

Algorithm       Best Case    Average Case    Worst Case    Space

Iterative       O(n)         O(n)            O(n)          O(1)
Recursive       O(n)         O(n)            O(n)          O(n)


DYNAMIC PROGRAMMING

Algorithm       Best Case       Average Case       Worst Case       Space

Making Change   O(n * amount)   O(n * amount)      O(n * amount)    O(amount)


==================================================
PROJECT STRUCTURE
==================================================

DAA-Algorithms-Python/
│
├── Sorting Algorithms/
│   ├── bubblesort.py
│   ├── insertionsort.py
│   ├── selectionsort.py
│   ├── mergesort.py
│   ├── quicksort.py
│   └── maxheapsort.py
│
├── Searching Algorithms/
│   ├── linear search.py
│   └── binary search.py
│
├── Factorial/
│   ├── factorial_iterative.py
│   └── factorial_recursive.py
│
├── Dynamic Programming/
│   └── making_change.py
│
└── README.md


==================================================
FEATURES
==================================================

* Implements fundamental DAA algorithms in Python.
* Includes sorting algorithms.
* Includes searching algorithms.
* Includes iterative and recursive factorial programs.
* Includes Making Change using Dynamic Programming.
* Accepts user input.
* Displays the result.
* Displays Best, Average, and Worst Case Time Complexity.
* Displays Space Complexity.
* Measures execution time using time.perf_counter().
* Easy to understand and suitable for DAA laboratory practice.


==================================================
REQUIREMENTS
==================================================

* Python 3.x
* No external libraries are required.

The programs use Python's built-in time module to measure execution time.


==================================================
HOW TO RUN
==================================================

Sorting Algorithms:

python bubblesort.py

python insertionsort.py

python selectionsort.py

python mergesort.py

python quicksort.py

python maxheapsort.py


Searching Algorithms:

python "linear search.py"

python "binary search.py"


Factorial Programs:

python factorial_iterative.py

python factorial_recursive.py


Dynamic Programming:

python making_change.py


==================================================
SAMPLE OUTPUT - ITERATIVE FACTORIAL
==================================================

Enter a number: 5

--- Iterative Method ---
Factorial = 120
Execution Time = 0.000002 seconds

Time Complexity:
Best Case    : O(n)
Average Case : O(n)
Worst Case   : O(n)
Space Complexity: O(1)


==================================================
SAMPLE OUTPUT - RECURSIVE FACTORIAL
==================================================

Enter a number: 5

--- Recursive Method ---
Factorial = 120
Execution Time = 0.000002 seconds

Time Complexity:
Best Case    : O(n)
Average Case : O(n)
Worst Case   : O(n)
Space Complexity: O(n)


==================================================
SAMPLE OUTPUT - MAKING CHANGE
==================================================

Enter coin denominations: 1 2 5
Enter the amount: 11

--- Making Change Using Dynamic Programming ---
Minimum number of coins = 3
Execution Time = 0.000003 seconds

Time Complexity:
Best Case    : O(n * amount)
Average Case : O(n * amount)
Worst Case   : O(n * amount)
Space Complexity: O(amount)


==================================================
LEARNING OBJECTIVES
==================================================

This project helps in understanding:

* Bubble Sort
* Insertion Sort
* Selection Sort
* Merge Sort
* Quick Sort
* Max Heap Sort
* Linear Search
* Binary Search
* Factorial using Iterative Method
* Factorial using Recursive Method
* Making Change using Dynamic Programming
* Max Heap and Heapify
* Divide and Conquer
* Dynamic Programming
* Time Complexity Analysis
* Space Complexity Analysis
* Execution Time Measurement in Python
* Comparison of Sorting and Searching Algorithms


==================================================
CONCLUSION
==================================================

This project demonstrates different algorithmic techniques used in Design and Analysis of Algorithms.

Sorting algorithms are used to arrange data efficiently, searching algorithms are used to find elements, factorial programs demonstrate iterative and recursive approaches, and Dynamic Programming is used to solve the Making Change Problem efficiently.

The project also provides time and space complexity analysis for each algorithm, making it useful for understanding algorithm performance.


==================================================
CONTRIBUTING
==================================================

Contributions are welcome!

Feel free to fork this repository, make improvements, and submit a pull request.


==================================================
LICENSE
==================================================

This project is open-source and available under the MIT License.


⭐ If you found this project useful, consider giving it a star on GitHub!
