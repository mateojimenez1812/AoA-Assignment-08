# Analysis of Algorithms – Assignment 08

Yachay Tech – School of Mathematical and Computational Sciences

## Contents

| File | Exercise | Language | Description |
|---|---|---|---|
| `swap.py` | 1 | Python | Swapping two variables without extra storage (arithmetic and XOR methods) |
| `counting_sorts.py` | 2, 3 | Python | ComparisonCountingSort, DistributionCountingSort and a comparison of both |
| `hashing.cpp` | 4 | C++ | Hash table with closed hashing (open addressing, linear probing), using only arrays |

## Requirements

- Python 3.8+ (no external libraries)
- A C++ compiler (`clang++` or `g++`)

## How to run

```bash
python3 swap.py
python3 counting_sorts.py

clang++ -std=c++11 -o hashing hashing.cpp
./hashing
```

On Windows, use `python` instead of `python3`, compile with `g++ -std=c++11 -o hashing hashing.cpp` and run `hashing.exe`.

## Summary

**Exercise 1 – Swap without extra storage.** Yes, it is possible:

- Arithmetic: `u = u + v; v = u - v; u = u - v`
- XOR: `u = u ^ v; v = u ^ v; u = u ^ v`

The arithmetic method can overflow with fixed-size integers, and the XOR method only works with integers.

**Exercise 2 – ComparisonCountingSort.** For each element, it counts how many elements are smaller than it. That count is the element's position in the sorted array. It always makes n(n−1)/2 comparisons.

**Exercise 3 – DistributionCountingSort and comparison.** When the values are integers in a known range [l, u], it counts the frequency of each value, turns the frequencies into a cumulative distribution and uses it to place each element directly in its final position.

| | ComparisonCountingSort | DistributionCountingSort |
|---|---|---|
| Time complexity | Θ(n²) | Θ(n + k), with k = u − l + 1 |
| Extra space | Θ(n) (count array + output) | Θ(n + k) (frequency array + output) |
| Compares elements? | Yes | No |
| Input restriction | Any comparable values | Integers in a small known range |
| Stable? | No (equal elements end up in reverse order) | Yes (when filled right to left) |
| Implementation | Two nested loops over pairs (i, j) | Three simple linear loops: frequencies, cumulative sums, placement |

The program measures both: the comparisons of ComparisonCountingSort grow quadratically, while the operations of DistributionCountingSort grow linearly (2n + k).

**Exercise 4 – Closed hashing.** Keys are words. The hash function is h(K) = (sum of letter positions, A = 1, …, Z = 26) mod 13. When a cell is taken, the next cell is tried (linear probing, wrapping around the end of the table). Searching follows the same sequence until the key or an empty cell is found. Deletion marks the cell as DELETED (lazy deletion) so later searches are not cut short. No dictionaries, containers or string libraries are used; `<iostream>` is used only to print.
