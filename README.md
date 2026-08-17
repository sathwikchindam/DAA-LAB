# DAA - Sorting and Searching Algorithms in Python

This repository contains Python implementations of fundamental **Sorting and Searching Algorithms** as part of the **Design and Analysis of Algorithms (DAA) Laboratory**.

Each program:

* Takes input from the user
* Performs the required sorting or searching operation
* Displays the result
* Displays Best, Average, and Worst Case Time Complexity
* Displays Space Complexity
* Measures execution time in microseconds

---

# 📂 Algorithms Included

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

---

# 🔷 SORTING ALGORITHMS

## 1. Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

### File

`bubblesort.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n)       |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

### Space Complexity

`O(1)`

---

## 2. Insertion Sort

Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

### File

`insertionsort.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n)       |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

### Space Complexity

`O(1)`

---

## 3. Selection Sort

Selection Sort repeatedly finds the smallest element from the unsorted part and places it at the beginning.

### File

`selectionsort.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n²)      |
| Average Case | O(n²)      |
| Worst Case   | O(n²)      |

### Space Complexity

`O(1)`

---

## 4. Merge Sort

Merge Sort uses the **Divide and Conquer** technique. It divides the array into smaller parts, sorts them, and then merges them.

### File

`mergesort.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n log n) |

### Space Complexity

`O(n)`

---

## 5. Quick Sort

Quick Sort uses the **Divide and Conquer** technique. It selects a pivot and partitions the array around the pivot.

### File

`quicksort.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n²)      |

### Space Complexity

`O(log n)` average case due to recursion.

---

## 6. Max Heap Sort

Max Heap Sort is a comparison-based sorting algorithm that uses a **Max Heap** data structure.

The algorithm first builds a Max Heap and then repeatedly moves the largest element to the end of the array.

### File

`maxheapsort.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n log n) |

### Space Complexity

`O(log n)` due to recursive `max_heapify()`.

---

# 🔶 SEARCHING ALGORITHMS

## 7. Linear Search

Linear Search checks each element of the array one by one until the required element is found or the end of the array is reached.

### File

`linear search.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(1)       |
| Average Case | O(n)       |
| Worst Case   | O(n)       |

### Space Complexity

`O(1)`

### Features

* Takes the number of elements as input.
* Takes array elements from the user.
* Takes the element to be searched.
* Displays the position of the element if found.
* Displays the time complexity.
* Measures execution time in microseconds.

---

## 8. Binary Search

Binary Search is an efficient searching algorithm that repeatedly divides the search range into two halves.

The program sorts the input array before performing Binary Search.

### File

`binary search.py`

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(1)       |
| Average Case | O(log n)   |
| Worst Case   | O(log n)   |

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
* Measures execution time in microseconds.

---

# 📊 Sorting Algorithms Comparison

| Algorithm      | Best Case  | Average Case | Worst Case | Space            |
| -------------- | ---------- | ------------ | ---------- | ---------------- |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)             |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)             |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)             |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)             |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n) Average |
| Max Heap Sort  | O(n log n) | O(n log n)   | O(n log n) | O(log n)         |

---

# 🔎 Searching Algorithms Comparison

| Algorithm     | Best Case | Average Case | Worst Case | Space |
| ------------- | --------- | ------------ | ---------- | ----- |
| Linear Search | O(1)      | O(n)         | O(n)       | O(1)  |
| Binary Search | O(1)      | O(log n)     | O(log n)   | O(1)  |

---

# 📁 Project Structure

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
└── README.md
```

---

# 🛠 Requirements

* Python 3.x
* No external libraries are required.

The programs use Python's built-in `time` module to measure execution time.

---

# ▶️ How to Run

## Sorting Algorithms

### Bubble Sort

```bash
python bubblesort.py
```

### Insertion Sort

```bash
python insertionsort.py
```

### Selection Sort

```bash
python selectionsort.py
```

### Merge Sort

```bash
python mergesort.py
```

### Quick Sort

```bash
python quicksort.py
```

### Max Heap Sort

```bash
python maxheapsort.py
```

---

## Searching Algorithms

### Linear Search

```bash
python "linear search.py"
```

### Binary Search

```bash
python "binary search.py"
```

---

# 📥 Sample Input - Sorting

```text
Enter number of elements:
5

Enter elements:
5 3 1 4 2
```

# 📤 Sample Output - Sorting

```text
Sorted Array:
1 2 3 4 5

Time Complexity:
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n log n)

Space Complexity:
O(log n)

Execution Time: 25.67 microseconds
```

---

# 📥 Sample Input - Linear Search

```text
Enter number of elements: 5
Enter elements:
10 20 30 40 50

Enter element to search: 30
```

# 📤 Sample Output - Linear Search

```text
Search Result:
Element found at position: 3

Time Complexity:
Best Case    : O(1)
Average Case : O(n)
Worst Case   : O(n)

Space Complexity: O(1)

Execution Time: 2.50 microseconds
```

---

# 📥 Sample Input - Binary Search

```text
Enter number of elements: 5
Enter elements:
50 20 40 10 30

Sorted Array:
10 20 30 40 50

Enter element to search: 30
```

# 📤 Sample Output - Binary Search

```text
Search Result:
Element found at position: 3

Time Complexity:
Best Case    : O(1)
Average Case : O(log n)
Worst Case   : O(log n)

Space Complexity: O(1)

Execution Time: 2.30 microseconds
```

---

# 📚 Learning Objectives

This project helps in understanding:

* Bubble Sort
* Insertion Sort
* Selection Sort
* Merge Sort
* Quick Sort
* Max Heap Sort
* Linear Search
* Binary Search
* Max Heap and Heapify
* Divide and Conquer
* Time Complexity Analysis
* Space Complexity Analysis
* Execution Time Measurement in Python
* Comparison of Sorting and Searching Algorithms

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository, make improvements, and submit a pull request.

---

# 📄 License

This project is open-source and available under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
