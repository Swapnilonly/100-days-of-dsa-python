# Arrays

## What I learned

- Array traversal
- Prefix Sum
- Two Pointer
- Sliding Window

## Mistakes



# 31. Next Permutation

- **LeetCode:** [Next Permutation](https://leetcode.com/problems/next-permutation/)
- **Difficulty:** Medium
- **Topic:** Array, Two Pointers, Greedy

## Problem
Rearrange the array into its next lexicographically greater permutation. If no greater permutation exists, rearrange it into ascending order.

Modify the array in-place without returning anything.

## Approach
Find the pivot from the right, swap it with the next greater element, and reverse the remaining suffix to get the next permutation.

## Steps
1. **Find the pivot:** Traverse from right to left and find the first index `i` where `nums[i] < nums[i + 1]`.
2. **Find the successor:** If a pivot exists, traverse from the right to find the first element greater than `nums[i]`.
3. **Swap:** Exchange the pivot and successor.
4. **Reverse the suffix:** Reverse all elements after the pivot to arrange them in ascending order.
5. **No pivot found:** Reverse the entire array to obtain the smallest permutation.

## Complexity
- **Time:** \(O(n)\)
- **Space:** \(O(1)\) auxiliary space when reversing the suffix in-place using two pointers.

## Key Takeaway
The pivot makes the permutation greater than the original, while reversing the suffix makes it the smallest possible greater permutation.

**Pattern:** Greedy + Two Pointers