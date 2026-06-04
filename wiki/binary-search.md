---
title: Binary Search
date: 2026-06-03
tags: [dsa, algorithms, search]
---

# Binary Search

**Summary**: An efficient $O(\log n)$ search algorithm for locating targets in sorted lists by repeatedly halving the search space.

**Sources**: [lesson_1_binary_search_and_complexity_analysis.ipynb](../raw/lesson_1_binary_search_and_complexity_analysis.ipynb)

---

## 1. Introduction & The Setup

Binary search is one of the most fundamental algorithms in computer science. While simple in theory, implementing it correctly for all edge cases (such as lists with duplicates, empty inputs, or elements at boundaries) requires precision.

A common example problem is:
> Given a list of numbers sorted in **descending order** (e.g., card values from highest to lowest), find the index of a queried number. If the number appears multiple times, return its **first occurrence**.

### Test Cases & Edge Cases
When developing the algorithm, we must verify:
1. The query is in the middle of the list.
2. The query is the first or last element.
3. The list contains only one element (found/not found).
4. The query is not in the list.
5. The list is empty.
6. The list contains duplicate numbers.

---

## 2. Classic Binary Search (Descending Order)

In standard ascending binary search:
- If `cards[mid] < query`, we search the right half (`lo = mid + 1`).
- If `cards[mid] > query`, we search the left half (`hi = mid - 1`).

For a **descending** list, the logic is reversed:
- If `cards[mid] < query`, the target must lie to the **left** (larger numbers are at smaller indices): `hi = mid - 1`.
- If `cards[mid] > query`, the target must lie to the **right** (smaller numbers are at larger indices): `lo = mid + 1`.

### Handling Duplicates
If the array contains duplicate queries (e.g., `cards = [8, 8, 6, 6, 6, 6, 3]`, `query = 6`), a naive binary search might land on a middle occurrence of `6` (index 4) instead of the first occurrence (index 2). 

To fix this, when we find `cards[mid] == query`, we check if the element immediately preceding it (`mid - 1`) is also equal to the query. If so, we continue searching the left half.

Here is the complete implementation with the boundary duplicate check:

```python
def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        # Check if this is the FIRST occurrence of the query
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left' # Go left to find earlier occurrences
        else:
            return 'found'
    elif mid_number < query:
        return 'left' # Larger values are on the left
    else:
        return 'right' # Smaller values are on the right

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
            
    return -1
```

---

## 3. Generic Binary Search Template

We can generalize binary search by passing a `condition` function. This makes the binary search logic reusable for other problems (like finding boundaries, solving optimization thresholds, or finding first/last indices on LeetCode).

### The Reusable Engine
```python
def binary_search(lo, hi, condition):
    """
    Generic binary search engine.
    condition(mid) must return:
    - 'found' if mid is the correct answer
    - 'left' if the answer lies in the left half [lo, mid-1]
    - 'right' if the answer lies in the right half [mid+1, hi]
    """
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1
```

### Implementing `locate_card` Using the Generic Engine
By writing a helper closure, we can easily wrap the logic:
```python
def locate_card_generic(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid - 1 >= 0 and cards[mid - 1] == query:
                return 'left'
            return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
            
    return binary_search(0, len(cards) - 1, condition)
```

---

## 4. Key Takeaways & Practice
- **Complexity**: Time: $O(\log n)$ | Space: $O(1)$.
- **Precondition**: The input array must be sorted.
- **Problem Solving Framework**:
  1. Define inputs/outputs and write down test cases.
  2. Implement linear search first (naive baseline).
  3. Refactor to binary search to reduce complexity from $O(n)$ to $O(\log n)$.

## Related Concepts
- [[complexity-analysis]]
- [[dsa-in-python]]
