# Minimum Size Subarray Sum

## Problem
Given an array of **positive integers** `nums` and a positive integer `target`, return the **minimum length** of a contiguous subarray whose sum is **greater than or equal to** `target`.

If there is no such subarray, return `0`.

---

## Concept
- Variable Sliding Window
- Two Pointers (`left` and `right`)
- Running Sum

---

## Approach
- Initialize two pointers:
  - `left` → Start of the window.
  - `right` → End of the window.
- Maintain a running sum (`curr_sum`) of the current window.
- Expand the window by moving the `right` pointer and adding the current element to `curr_sum`.
- Once `curr_sum >= target`:
  - Update the minimum window length.
  - Shrink the window from the left by subtracting `nums[left]` from `curr_sum`.
  - Move `left` forward.
- Continue shrinking until the window becomes invalid (`curr_sum < target`).
- Repeat until the entire array has been processed.
- If no valid window is found, return `0`.

---

## Dry Run

```text
target = 7
nums = [2,3,1,2,4,3]


## Time Complexity
- **O(n)**
  - Each element enters the window once.
  - Each element leaves the window once.
  - Both pointers together traverse the array only once.

---

## Space Complexity
- **O(1)**
  - Only a few variables are used.
  - No extra data structures are required.

---

## Key Learning

### Variable Sliding Window Pattern
- Use this pattern when the **window size is not fixed**.
- Expand the window until it satisfies the required condition.
- Once the condition is satisfied, shrink the window to find the optimal answer.
- Every element is:
  - Added to the window **once**.
  - Removed from the window **once**.
- This makes the overall time complexity **O(n)**.


The window **slides**, it never **restarts**.

---

## Pattern Recognition

Use **Variable Sliding Window** when you see:

- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Fruits Into Baskets
- Minimum Window Substring
- Permutation in String

Common keywords:
- **Smallest**
- **Longest**
- **Minimum Length**
- **Maximum Length**
- **At least**
- **At most**
- **Contiguous Subarray / Substring**

---

## Generic Template

```python
left = 0

for right in range(len(nums)):
    # Expand the window
    add(nums[right])

    while window_is_valid:
        # Update answer
        # Shrink the window
        remove(nums[left])
        left += 1
```

---

## Key Takeaway

Remember these two rules:

```text
Need a larger sum?
→ Move Right (Expand Window)
```

```text
Already have a valid window?
→ Move Left (Shrink Window)
```

The window **never restarts**.
It only **expands** and **shrinks**.