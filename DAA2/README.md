# DAA2 - Searching Algorithms in Python

This repository contains Python implementations of fundamental searching
algorithms as part of the Design and Analysis of Algorithms (DAA) laboratory.

## Algorithms Included

1. Linear Search
2. Binary Search

---

## 1. Linear Search

Linear Search checks each element of the array one by one until the required
element is found or the end of the array is reached.

### File
`linear search.py`

### Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |

### Space Complexity

`O(1)`

### Features

- Takes the number of elements as input.
- Takes array elements from the user.
- Takes the element to be searched.
- Displays the position of the element if found.
- Displays the time complexity.
- Measures execution time in microseconds.

---

## 2. Binary Search

Binary Search is an efficient searching algorithm that repeatedly divides
the search range into two halves.

The program sorts the input array before performing the Binary Search.

### File
`binary search.py`

### Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

### Space Complexity

`O(1)`

### Features

- Takes the number of elements as input.
- Takes array elements from the user.
- Sorts the array before searching.
- Takes the element to be searched.
- Displays the sorted array.
- Displays the position of the element if found.
- Displays the time complexity.
- Measures execution time in microseconds.

---

## Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

---

## Requirements

- Python 3.x
- No external libraries are required.

The programs use Python's built-in `time` module to measure execution time.

---

## How to Run

### Linear Search

```bash
python "linear search.py"
python "binary search.py"
Enter number of elements: 5
Enter elements:
10 20 30 40 50
Enter element to search: 30

Search Result:
Element found at position: 3

Time Complexity:
Best Case : O(1)
Average Case : O(n)
Worst Case : O(n)
Execution Time: 2.50 microseconds
Enter number of elements: 5
Enter elements:
50 20 40 10 30

Sorted Array:
10 20 30 40 50

Enter element to search: 30

Search Result:
Element found at position: 3

Time Complexity:
Best Case    : O(1)
Average Case : O(log n)
Worst Case   : O(log n)
Space Complexity: O(1)
Execution Time: 2.30 microseconds
