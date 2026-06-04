---
title: Complexity Analysis
date: 2026-06-03
tags: [dsa, algorithms, complexity]
---

# Complexity Analysis (Big O)

**Summary**: A mathematical framework used to describe the execution time or space requirements of an algorithm relative to the input size $N$.

**Sources**: [lesson_1_binary_search_and_complexity_analysis.ipynb](../raw/lesson_1_binary_search_and_complexity_analysis.ipynb)

---

## 1. What is Complexity Analysis?

When designing algorithms, execution speed and memory usage depend on the hardware, operating system, and current CPU load. To evaluate the algorithm itself, we use **Complexity Analysis**, expressing performance as a function of the input size $N$ using **Big O Notation**.

Big O notation focuses on:
- **Worst-case scenario**: The maximum number of operations an algorithm can take.
- **Asymptotic behavior**: How the run time scales as $N$ grows to infinity.
- **Dropping constants & lower-order terms**: For example, $O(3N^2 + 5N + 10)$ simplifies to $O(N^2)$ because as $N$ becomes extremely large, the $N^2$ term dominates the growth.

---

## 2. Derivation of Binary Search Complexity: $O(\log N)$

Let's mathematically derive why Binary Search runs in logarithmic time.

1. We start with an array of size $N$.
2. In each iteration of the loop, the search space is divided in half:
   - **Iteration 0**: $N$ elements
   - **Iteration 1**: $N/2$ elements
   - **Iteration 2**: $N/4$ (or $N / 2^2$) elements
   - **Iteration 3**: $N/8$ (or $N / 2^3$) elements
   - ...
   - **Iteration $k$**: $N / 2^k$ elements
3. The search terminates when the search space reduces to a single element:
   $$\frac{N}{2^k} = 1 \implies N = 2^k$$
4. Taking the base-2 logarithm of both sides:
   $$k = \log_2 N$$

Thus, the maximum number of iterations (worst-case time complexity) is **$\lceil \log_2 N \rceil$**, which is written as **$O(\log N)$**.

---

## 3. Performance Scaling: Linear vs. Logarithmic

To see the massive difference between $O(N)$ (Linear Search) and $O(\log N)$ (Binary Search), consider the following table showing the number of operations required in the worst-case:

| Input Size ($N$) | Linear Search Operations ($O(N)$) | Binary Search Operations ($O(\log N)$) | Difference / Speedup |
|---|---|---|---|
| **10** | 10 | 4 | 2.5x |
| **100** | 100 | 7 | 14x |
| **10,000** | 10,000 | 14 | 714x |
| **1,000,000** | 1,000,000 | 20 | 50,000x |
| **10,000,000** | 10,000,000 | 24 | 416,666x |

### Scaling Rule
- **Linear Search**: If the input size increases by 10x, the execution time increases by **10x** (10 times more operations).
- **Binary Search**: If the input size increases by 10x, the algorithm requires only **$\approx 3.3$ additional operations** ($\log_2(10) \approx 3.32$).

---

## 4. Common Complexity Classes

Here are the standard Big O complexity classes ordered from most efficient to least efficient:

| Notation | Name | Typical Example | Scaling Behavior |
|---|---|---|---|
| **$O(1)$** | Constant | Accessing array element by index | Time is independent of $N$. |
| **$O(\log N)$** | Logarithmic | Binary search | Time grows very slowly. |
| **$O(N)$** | Linear | Linear search, finding minimum in unsorted array | Time grows proportionally to $N$. |
| **$O(N \log N)$** | Linearithmic | Merge Sort, Quick Sort (average) | Standard sorting runtime. |
| **$O(N^2)$** | Quadratic | Nested loops (e.g., Bubble Sort) | Time quadruples when $N$ doubles. |
| **$O(2^N)$** | Exponential | Recursive Fibonacci, generating subsets | Doubling $N$ squares the runtime. |
| **$O(N!)$** | Factorial | Generating all permutations (TSP brute-force) | Impractical for $N > 12$. |

---

## Related Concepts
- [[binary-search]]
- [[dsa-in-python]]
