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











# Sliding Window

## What is Sliding Window?

Sliding Window is an optimization technique used for solving problems involving **contiguous (continuous)** subarrays or substrings.

Instead of generating every possible subarray (`O(n²)`), we reuse the previous window by adding one element and removing one element, reducing the complexity to **O(n)**.

---

# When to Think About Sliding Window?

Whenever you see these words:

- Continuous
- Contiguous
- Subarray
- Substring
- Window
- Longest
- Shortest
- Maximum
- Minimum

Always ask yourself:

> **Can I maintain a moving window instead of recalculating everything?**

---

# Types of Sliding Window

```
Sliding Window
│
├── Fixed Size Window
│
├── Variable Size Window
│      ├── Longest Window
│      ├── Smallest Window
│      ├── At Most K
│      ├── Exactly K
│      └── Frequency Based
│
└── Kadane's Algorithm
```

---

# 1. Fixed Size Sliding Window

## Pattern

The size of the window is already given.

Example

```
Find maximum sum of subarray of size k

Find average of every window of size k

Maximum vowels in substring of length k
```

Keywords

```
size = k
window of k
length k
substring of size k
subarray of size k
```

---

## Visualization

```
nums = [2,1,5,1,3,2]

k = 3

[2 1 5] 1 3 2

2 [1 5 1] 3 2

2 1 [5 1 3] 2

2 1 5 [1 3 2]
```

Window size never changes.

---

## Steps

```
1. Expand right
2. Add current element
3. If window becomes larger than k
      Remove left element
      Move left
4. When window size == k
      Calculate answer
```

---

## Template

```python
left = 0
window_sum = 0

for right in range(len(nums)):

    window_sum += nums[right]

    if right - left + 1 > k:
        window_sum -= nums[left]
        left += 1

    if right - left + 1 == k:
        answer = max(answer, window_sum)
```

---

## Time Complexity

```
O(n)
```

---

## Problems

- Maximum Sum Subarray of Size K
- Maximum Average Subarray
- Maximum Number of Vowels
- Grumpy Bookstore Owner

---

# 2. Variable Size Sliding Window

Window size is NOT fixed.

It expands and shrinks according to a condition.

---

## Keywords

```
Longest

Smallest

Minimum

Maximum

At most

At least

Exactly

Distinct
```

---

## General Template

```python
left = 0

for right in range(len(nums)):

    # include nums[right]

    while condition_invalid:

        # remove nums[left]
        left += 1

    # update answer
```

---

# 3. Longest Window Pattern

Question asks

```
Longest Substring

Longest Subarray

Maximum Length
```

---

## Idea

```
Expand

Condition satisfied?

YES

Update answer

NO

Shrink from left
```

---

## Example

Longest Substring Without Repeating Characters

```
abcabcbb

a

ab

abc

abca ❌ duplicate

Shrink

bca
```

---

## Template

```python
left = 0
freq = {}

answer = 0

for right in range(len(s)):

    freq[s[right]] = freq.get(s[right],0)+1

    while freq[s[right]] > 1:

        freq[s[left]] -= 1
        left += 1

    answer = max(answer,right-left+1)
```

---

## Problems

- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Fruit Into Baskets
- Max Consecutive Ones III

---

# 4. Smallest Window Pattern

Question asks

```
Minimum

Smallest

Shortest
```

---

## Example

Minimum Size Subarray Sum

```
target = 7

2 3 1 2 4 3

Expand

2

5

6

8 ✅

Shrink

6

Expand

10

Shrink

...
```

---

## Template

```python
left = 0
current = 0

answer = float("inf")

for right in range(len(nums)):

    current += nums[right]

    while current >= target:

        answer = min(answer,right-left+1)

        current -= nums[left]
        left += 1
```

---

## Problems

- Minimum Window Substring
- Minimum Size Subarray Sum

---

# 5. At Most K Pattern

Question says

```
At most K

At most two

At most three

At most k distinct
```

---

## Template

```python
left = 0
freq = {}

for right in range(len(nums)):

    freq[nums[right]] = freq.get(nums[right],0)+1

    while len(freq) > k:

        freq[nums[left]] -= 1

        if freq[nums[left]] == 0:
            del freq[nums[left]]

        left += 1
```

---

## Problems

- Fruit Into Baskets
- Longest Substring with K Distinct
- Max Consecutive Ones III

---

# 6. Exactly K Pattern

Very common interview trick.

Instead of solving directly,

Use

```
Exactly(K)

=

AtMost(K)

-

AtMost(K-1)
```

---

## Why?

Suppose

```
AtMost(3)

contains

1 distinct

2 distinct

3 distinct
```

```
AtMost(2)

contains

1 distinct

2 distinct
```

Subtract them

Only

```
Exactly 3
```

remains.

---

## Problems

- Subarrays With K Different Integers
- Count Nice Subarrays
- Count Complete Subarrays

---

# 7. Frequency Based Window

Used when characters or numbers repeat.

Data structures

```
Dictionary

HashMap

Counter

Frequency Array
```

---

## Used In

- Anagrams
- Permutations
- Distinct characters
- Character replacement

---

# Kadane's Algorithm

## Used For

Maximum Sum Contiguous Subarray

---

## Keywords

```
Maximum Sum

Largest Sum

Contiguous

Maximum Profit
```

---

## Intuition

Negative running sum can never help future answers.

So,

```
Current Sum < 0

↓

Discard it

↓

Start fresh
```

---

## Dry Run

```
nums

-2

1

-3

4

-1

2

1

-5

4
```

```
current

-2

1

-2

4

3

5

6

1

5
```

Maximum

```
6
```

Subarray

```
[4,-1,2,1]
```

---

## Template

```python
current = nums[0]
best = nums[0]

for i in range(1,len(nums)):

    current = max(nums[i], current + nums[i])

    best = max(best,current)

return best
```

---

# Pattern Identification Table

| Question Says | Pattern |
|---------------|----------|
| Window size = k | Fixed Window |
| Longest | Variable Window |
| Minimum Length | Variable Window |
| At Most K | Variable Window |
| Exactly K | AtMost(K)-AtMost(K-1) |
| Distinct | Frequency + Window |
| Character Count | HashMap |
| Contiguous Maximum Sum | Kadane |
| Continuous Positive Numbers | Sliding Window |
| Negative Numbers + Sum | Prefix Sum / Kadane |

---

# Sliding Window Decision Tree

```
Question
      │
      │
Continuous / Contiguous ?
      │
     YES
      │
Length Fixed ?
   ┌──┴──┐
   │     │
 YES     NO
 │       │
Fixed   Variable
Window  Window
          │
   Longest or Smallest ?
          │
      Shrink Window
          │
Distinct / Frequency ?
          │
     HashMap Needed
          │
Exactly K ?
          │
AtMost(K)-AtMost(K-1)
```

---

# Common Mistakes

## ❌ Mistake 1

Using Sliding Window on non-contiguous problems.

---

## ❌ Mistake 2

Forgetting to remove the left element while shrinking.

---

## ❌ Mistake 3

Updating the answer before the window becomes valid.

---

## ❌ Mistake 4

Confusing "At Most K" with "Exactly K".

Remember

```
Exactly(K)

=

AtMost(K)

-

AtMost(K-1)
```

---

## ❌ Mistake 5

Trying to use Sliding Window for arrays containing negative numbers when the window condition depends on the sum.

Example

```
[-2, 5, -1, 4]
```

Here, shrinking or expanding greedily may not work correctly because negative numbers can increase or decrease the sum unpredictably. In such cases, consider **Prefix Sum**, **HashMap**, or **Kadane's Algorithm**, depending on the problem.

---

# Complexity

| Pattern | Time | Space |
|----------|------|--------|
| Fixed Window | O(n) | O(1) |
| Variable Window | O(n) | O(1) |
| Frequency Window | O(n) | O(k) |
| Kadane | O(n) | O(1) |

---

# Must-Do LeetCode Problems

## Easy

- Maximum Average Subarray I
- Maximum Number of Vowels
- Max Consecutive Ones III
- Best Time to Buy and Sell Stock

---

## Medium

- Longest Substring Without Repeating Characters
- Fruit Into Baskets
- Longest Repeating Character Replacement
- Permutation in String
- Find All Anagrams
- Minimum Window Substring
- Minimum Size Subarray Sum

---

## Hard

- Subarrays With K Different Integers
- Minimum Window Substring

---

# Revision Checklist

- [ ] Understand Fixed Window
- [ ] Understand Variable Window
- [ ] Learn Shrink Condition
- [ ] Learn Frequency Map
- [ ] Learn At Most K
- [ ] Learn Exactly K
- [ ] Learn Kadane
- [ ] Solve 15+ Problems
- [ ] Identify Pattern Without Seeing Solution

---

# Golden Rule

```
Contiguous + Fixed Length
        ↓
Fixed Sliding Window

Contiguous + Longest / Smallest
        ↓
Variable Sliding Window

Exactly K
        ↓
AtMost(K) - AtMost(K-1)

Maximum Contiguous Sum
        ↓
Kadane

Negative Numbers + Sum Constraint
        ↓
Think Prefix Sum / Kadane instead of Sliding Window
```