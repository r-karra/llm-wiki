---
title: Binary Search
date: 2026-06-03
tags: [dsa, algorithms, search]
---

# Binary Search

**Summary**: An efficient algorithm for finding an item from a sorted list of items by repeatedly dividing in half the portion of the list that could contain the item.

**Sources**: [lesson_1_binary_search_and_complexity_analysis.ipynb](../raw/lesson_1_binary_search_and_complexity_analysis.ipynb)

---

Binary search works on sorted arrays. It compares the target value to the middle element of the array.

## Algorithm Steps
1. Find the middle element.
2. If middle == target, return index.
3. If middle > target, search the left half.
4. If middle < target, search the right half.

## Time Complexity
- **Worst-case**: $O(\log n)$
- **Best-case**: $O(1)$

## Related Concepts
- [[complexity-analysis]]
- [[algorithms]]
