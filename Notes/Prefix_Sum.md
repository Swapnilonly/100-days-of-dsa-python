# Pivot Index

## Problem
Find the **pivot index** of an array such that the sum of all the elements to the left of the index is equal to the sum of all the elements to the right.

If no such index exists, return `-1`.

## Concept
- Prefix Sum
- Running Sum
- In-place Prefix Sum (O(1) Extra Space)

## Approach
- Calculate the total sum of the array.
- Initialize `left_sum = 0`.
- Traverse the array once.
- For each index:
  - Calculate the right sum using:
    ```
    right_sum = total_sum - left_sum - nums[i]
    ```
  - Compare `left_sum` and `right_sum`.
  - If they are equal, return the current index.
  - Otherwise, update `left_sum` by adding the current element.
- If no pivot index is found, return `-1`.

## Time Complexity
- **O(n)**
  - `O(n)` to calculate the total sum.
  - `O(n)` for one traversal.
  - Overall: **O(n)**

## Space Complexity
- **O(1)**

## Key Learning
- Prefix Sum helps avoid recalculating left and right sums for every index.
- Instead of explicitly computing the right sum, derive it using:
  ```
  right_sum = total_sum - left_sum - nums[i]
  ```
- Maintain a running `left_sum` while traversing the array.
- This reduces the brute-force **O(n²)** solution to **O(n)**.
- Prefix Sum problems often require calculating a total once and updating values incrementally during traversal.    