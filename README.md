# DAA - Sorting, Searching, Factorial and Dynamic Programming Algorithms in Python

This repository contains Python implementations of fundamental **Sorting, Searching, Factorial, and Dynamic Programming Algorithms** as part of the **Design and Analysis of Algorithms (DAA) Laboratory**.

Each program:

* Takes input from the user
* Performs the required operation
* Displays the result
* Displays Best, Average, and Worst Case Time Complexity
* Displays Space Complexity
* Measures execution time

---

# ALGORITHMS INCLUDED

## Sorting Algorithms

1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Merge Sort
5. Quick Sort
6. Max Heap Sort

## Searching Algorithms

7. Linear Search
8. Binary Search

## Factorial Algorithms

9. Factorial using Iterative Method
10. Factorial using Recursive Method

## Dynamic Programming

11. Making Change Problem
12. Matrix Chain Multiplication
13. 0/1 Knapsack Problem

---

# SORTING ALGORITHMS

## 1. BUBBLE SORT

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

### File

`bubblesort.py`

### Time Complexity

* Best Case: O(n)
* Average Case: O(n²)
* Worst Case: O(n²)

### Space Complexity

`O(1)`

---

## 2. INSERTION SORT

Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

### File

`insertionsort.py`

### Time Complexity

* Best Case: O(n)
* Average Case: O(n²)
* Worst Case: O(n²)

### Space Complexity

`O(1)`

---

## 3. SELECTION SORT

Selection Sort repeatedly finds the smallest element from the unsorted part and places it at the beginning.

### File

`selectionsort.py`

### Time Complexity

* Best Case: O(n²)
* Average Case: O(n²)
* Worst Case: O(n²)

### Space Complexity

`O(1)`

---

## 4. MERGE SORT

Merge Sort uses the Divide and Conquer technique. It divides the array into smaller parts, sorts them, and then merges them.

### File

`mergesort.py`

### Time Complexity

* Best Case: O(n log n)
* Average Case: O(n log n)
* Worst Case: O(n log n)

### Space Complexity

`O(n)`

---

## 5. QUICK SORT

Quick Sort uses the Divide and Conquer technique. It selects a pivot and partitions the array around the pivot.

### File

`quicksort.py`

### Time Complexity

* Best Case: O(n log n)
* Average Case: O(n log n)
* Worst Case: O(n²)

### Space Complexity

`O(log n)` average case due to recursion.

---

## 6. MAX HEAP SORT

Max Heap Sort is a comparison-based sorting algorithm that uses a Max Heap data structure.

The algorithm first builds a Max Heap and then repeatedly moves the largest element to the end of the array.

### File

`maxheapsort.py`

### Time Complexity

* Best Case: O(n log n)
* Average Case: O(n log n)
* Worst Case: O(n log n)

### Space Complexity

`O(log n)` due to recursive `max_heapify()`.

---

# SEARCHING ALGORITHMS

## 7. LINEAR SEARCH

Linear Search checks each element of the array one by one until the required element is found or the end of the array is reached.

### File

`linear search.py`

### Time Complexity

* Best Case: O(1)
* Average Case: O(n)
* Worst Case: O(n)

### Space Complexity

`O(1)`

### Features

* Takes the number of elements as input.
* Takes array elements from the user.
* Takes the element to be searched.
* Displays the position of the element if found.
* Displays the time complexity.
* Measures execution time.

---

## 8. BINARY SEARCH

Binary Search is an efficient searching algorithm that repeatedly divides the search range into two halves.

The program sorts the input array before performing Binary Search.

### File

`binary search.py`

### Time Complexity

* Best Case: O(1)
* Average Case: O(log n)
* Worst Case: O(log n)

### Space Complexity

`O(1)`

### Features

* Takes the number of elements as input.
* Takes array elements from the user.
* Sorts the array before searching.
* Takes the element to be searched.
* Displays the sorted array.
* Displays the position of the element if found.
* Displays the time complexity.
* Measures execution time.

---

# FACTORIAL ALGORITHMS

## 9. FACTORIAL USING ITERATIVE METHOD

The iterative method calculates the factorial using a `for` loop.

### File

`factorial_iterative.py`

### Example

For `n = 5`:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### Time Complexity

* Best Case: O(n)
* Average Case: O(n)
* Worst Case: O(n)

### Space Complexity

`O(1)`

The iterative method uses less memory because it does not require recursive function calls.

---

## 10. FACTORIAL USING RECURSIVE METHOD

The recursive method calculates the factorial by calling the same function repeatedly until the base condition is reached.

### File

`factorial_recursive.py`

### Example

For `n = 5`:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### Time Complexity

* Best Case: O(n)
* Average Case: O(n)
* Worst Case: O(n)

### Space Complexity

`O(n)`

The recursive method requires additional stack space for each recursive function call.

---

# DYNAMIC PROGRAMMING

Dynamic Programming is a technique used to solve problems by breaking them into smaller overlapping subproblems and storing the results of previously solved subproblems.

The Dynamic Programming algorithms included in this repository are:

11. Making Change Problem
12. Matrix Chain Multiplication
13. 0/1 Knapsack Problem

---

## 11. MAKING CHANGE PROBLEM

The Making Change Problem finds the minimum number of coins required to make a given amount using the available coin denominations.

The problem is solved using the Dynamic Programming approach.

### File

`making_change.py`

### Problem Description

Given a set of coin denominations and a target amount, find the minimum number of coins required to make the target amount.

### Example

Coin Denominations:

```text
1, 2, 5
```

Amount:

```text
11
```

Solution:

```text
5 + 5 + 1 = 11
```

Minimum Number of Coins:

```text
3
```

### How the Algorithm Works

1. Create a DP array of size `amount + 1`.
2. Initialize all values with infinity.
3. Set `dp[0] = 0` because zero coins are needed to make amount 0.
4. For every amount from 1 to the target amount:

   * Check every available coin.
   * If the coin value is less than or equal to the current amount, calculate the minimum number of coins.
5. The final value `dp[amount]` gives the minimum number of coins required.

### Time Complexity

* Best Case: O(n × amount)
* Average Case: O(n × amount)
* Worst Case: O(n × amount)

Where:

* `n` = Number of coin denominations
* `amount` = Target amount

### Space Complexity

`O(amount)`

---

## 12. MATRIX CHAIN MULTIPLICATION

Matrix Chain Multiplication is an optimization problem in which the objective is to find the most efficient way to multiply a sequence of matrices.

The order of matrix multiplication can affect the total number of scalar multiplications. Dynamic Programming is used to find the multiplication order requiring the minimum number of scalar multiplications.

### File

`matrix_chain.py`

### Problem Description

Given a sequence of matrices, determine the best order of multiplication so that the total number of scalar multiplications is minimized.

### Example

Consider the following matrices:

```text
A1 = 10 × 20
A2 = 20 × 30
A3 = 30 × 40
```

The program calculates the most efficient multiplication order and finds the minimum number of scalar multiplications required.

### How the Algorithm Works

1. Take the number of matrices as input.
2. Take the dimensions of the matrices.
3. Create a Dynamic Programming table.
4. Calculate the multiplication cost for different matrix chains.
5. Store the minimum multiplication cost in the DP table.
6. Find the minimum number of scalar multiplications.
7. Display the result, complexity, and execution time.

### Time Complexity

* Best Case: O(n³)
* Average Case: O(n³)
* Worst Case: O(n³)

### Space Complexity

`O(n²)`

---

## 13. 0/1 KNAPSACK PROBLEM

The **0/1 Knapsack Problem** is an optimization problem in which each item has a weight and a value.

The objective is to select items such that the total weight does not exceed the knapsack capacity while the total value is maximized.

Each item can either be selected once or not selected.

### File

`knapsack.py`

### Problem Description

Given a set of items with their weights and values, and a maximum knapsack capacity, find the maximum value that can be obtained without exceeding the capacity.

### Example

Consider the following items:

| Item | Weight | Value |
| ---- | -----: | ----: |
| 1    |     10 |    60 |
| 2    |     20 |   100 |
| 3    |     30 |   120 |

Knapsack Capacity:

```text
50
```

Optimal Selection:

```text
Item 2 + Item 3
```

Total Weight:

```text
20 + 30 = 50
```

Maximum Value:

```text
100 + 120 = 220
```

### How the Algorithm Works

1. Take the number of items as input.
2. Take the weight and value of each item.
3. Take the knapsack capacity.
4. Create a Dynamic Programming table.
5. For each item, decide whether to include or exclude it.
6. Store the maximum value for each possible capacity.
7. The final DP table value gives the maximum possible value.

### Time Complexity

* Best Case: O(n × W)
* Average Case: O(n × W)
* Worst Case: O(n × W)

Where:

* `n` = Number of items
* `W` = Knapsack capacity

### Space Complexity

`O(n × W)`

---

# ALGORITHMS COMPARISON

## SORTING ALGORITHMS

| Algorithm      | Best Case  | Average Case | Worst Case | Space            |
| -------------- | ---------- | ------------ | ---------- | ---------------- |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)             |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)             |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)             |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)             |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n) Average |
| Max Heap Sort  | O(n log n) | O(n log n)   | O(n log n) | O(log n)         |

## SEARCHING ALGORITHMS

| Algorithm     | Best Case | Average Case | Worst Case | Space |
| ------------- | --------- | ------------ | ---------- | ----- |
| Linear Search | O(1)      | O(n)         | O(n)       | O(1)  |
| Binary Search | O(1)      | O(log n)     | O(log n)   | O(1)  |

## FACTORIAL ALGORITHMS

| Algorithm | Best Case | Average Case | Worst Case | Space |
| --------- | --------- | ------------ | ---------- | ----- |
| Iterative | O(n)      | O(n)         | O(n)       | O(1)  |
| Recursive | O(n)      | O(n)         | O(n)       | O(n)  |

## DYNAMIC PROGRAMMING

| Algorithm                   | Best Case     | Average Case  | Worst Case    | Space     |
| --------------------------- | ------------- | ------------- | ------------- | --------- |
| Making Change               | O(n × amount) | O(n × amount) | O(n × amount) | O(amount) |
| Matrix Chain Multiplication | O(n³)         | O(n³)         | O(n³)         | O(n²)     |
| 0/1 Knapsack                | O(n × W)      | O(n × W)      | O(n × W)      | O(n × W)  |

---

# PROJECT STRUCTURE

```text
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
│   ├── making_change.py
│   ├── matrix_chain.py
│   └── knapsack.py
│
└── README.md
```

---

# FEATURES

* Implements fundamental DAA algorithms in Python.
* Includes sorting algorithms.
* Includes searching algorithms.
* Includes iterative and recursive factorial programs.
* Includes Making Change using Dynamic Programming.
* Includes Matrix Chain Multiplication using Dynamic Programming.
* Includes 0/1 Knapsack using Dynamic Programming.
* Accepts user input.
* Displays the result.
* Displays Best, Average, and Worst Case Time Complexity.
* Displays Space Complexity.
* Measures execution time using `time.perf_counter()`.
* Easy to understand and suitable for DAA laboratory practice.

---

# REQUIREMENTS

* Python 3.x
* No external libraries are required.

The programs use Python's built-in `time` module to measure execution time.

---

# HOW TO RUN

## Sorting Algorithms

```bash
python bubblesort.py
python insertionsort.py
python selectionsort.py
python mergesort.py
python quicksort.py
python maxheapsort.py
```

## Searching Algorithms

```bash
python "linear search.py"
python "binary search.py"
```

## Factorial Programs

```bash
python factorial_iterative.py
python factorial_recursive.py
```

## Dynamic Programming

```bash
python making_change.py
python matrix_chain.py
python knapsack.py
```

---

# SAMPLE OUTPUT - ITERATIVE FACTORIAL

```text
Enter a number: 5

--- Iterative Method ---
Factorial = 120
Execution Time = 0.000002 seconds

Time Complexity:
Best Case    : O(n)
Average Case : O(n)
Worst Case   : O(n)
Space Complexity: O(1)
```

---

# SAMPLE OUTPUT - RECURSIVE FACTORIAL

```text
Enter a number: 5

--- Recursive Method ---
Factorial = 120
Execution Time = 0.000002 seconds

Time Complexity:
Best Case    : O(n)
Average Case : O(n)
Worst Case   : O(n)
Space Complexity: O(n)
```

---

# SAMPLE OUTPUT - MAKING CHANGE

```text
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
```

---

# SAMPLE OUTPUT - MATRIX CHAIN MULTIPLICATION

```text
Enter number of matrices: 3
Enter dimensions: 10 20 30 40

--- Matrix Chain Multiplication ---
Minimum number of scalar multiplications = 18000
Execution Time = 0.000003 seconds

Time Complexity:
Best Case    : O(n³)
Average Case : O(n³)
Worst Case   : O(n³)
Space Complexity: O(n²)
```

---

# SAMPLE OUTPUT - 0/1 KNAPSACK

```text
Enter number of items: 3
Enter weight of item 1: 10
Enter value of item 1: 60
Enter weight of item 2: 20
Enter value of item 2: 100
Enter weight of item 3: 30
Enter value of item 3: 120
Enter knapsack capacity: 50

--- 0/1 Knapsack Using Dynamic Programming ---
Maximum Value = 220
Execution Time = 0.000003 seconds

Time Complexity:
Best Case    : O(n × W)
Average Case : O(n × W)
Worst Case   : O(n × W)
Space Complexity: O(n × W)
```

---

# LEARNING OBJECTIVES

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
* Matrix Chain Multiplication
* 0/1 Knapsack
* Max Heap and Heapify
* Divide and Conquer
* Dynamic Programming
* Time Complexity Analysis
* Space Complexity Analysis
* Execution Time Measurement in Python
* Comparison of Sorting and Searching Algorithms

---

# CONCLUSION

This project demonstrates different algorithmic techniques used in **Design and Analysis of Algorithms**.

Sorting algorithms are used to arrange data efficiently, searching algorithms are used to find elements, factorial programs demonstrate iterative and recursive approaches, and Dynamic Programming is used to solve optimization problems such as **Making Change, Matrix Chain Multiplication, and 0/1 Knapsack**.

The project also provides time and space complexity analysis for each algorithm, making it useful for understanding algorithm performance.

---

# CONTRIBUTING

Contributions are welcome!

Feel free to fork this repository, make improvements, and submit a pull request.

---

# LICENSE

This project is open-source and available under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub!

