# Binary Search

## 🧠 Idea
- Works only on a **sorted array**.
- Repeatedly divide the search space into two halves.

---

## 📝 Pointer Updates

```python
if nums[mid] == target:
    return mid

elif nums[mid] < target:
    left = mid + 1      # Search Right Half

else:
    right = mid - 1     # Search Left Half
```

---

## 📌 Rules

- `nums[mid] < target` → Move `left` to `mid + 1`
- `nums[mid] > target` → Move `right` to `mid - 1`
- `nums[mid] == target` → Target Found

---

## ⚠️ Common Mistakes

❌

```python
left = mid
right = mid
```

✅

```python
left = mid + 1
right = mid - 1
```

---

## ⏱️ Complexity

- **Time:** `O(log n)`
- **Space:** `O(1)` (Iterative)



# 35. Search Insert Position

## Problem
Given a sorted array of distinct integers and a target value, return the index if the target exists. Otherwise, return the index where it should be inserted.

## Approach
- Use **Binary Search** to efficiently find the target.
- If the target is found, return its index.
- If not found, return the `left` pointer after the search ends, which represents the correct insertion position.

## Algorithm
1. Initialize `left = 0` and `right = n - 1`.
2. Find the middle element.
3. If target equals the middle element, return its index.
4. If target is greater, search the right half.
5. Otherwise, search the left half.
6. When the loop ends, return `left`.

## Complexity
- **Time:** `O(log n)`
- **Space:** `O(1)`

## Key Concepts
- Binary Search
- Sorted Array
- Divide and Conquer



# 69. Sqrt(x)

## Problem
Given a non-negative integer `x`, return the integer square root of `x`.

The integer square root is the largest integer `y` such that:


Do **not** use built-in square root or exponent functions.

---

## Approach - Binary Search

The square root of a number lies between:

- `1` and `x // 2` (for `x >= 2`)

Use Binary Search to find the largest value whose square is less than or equal to `x`.

### Steps

1. Handle edge case (`x < 2`).
2. Apply Binary Search on the range `[1, x // 2]`.
3. Calculate `mid`.
4. If `mid² == x`, return `mid`.
5. If `mid² < x`, store `mid` as a possible answer and search right.
6. Otherwise, search left.
7. Return the last valid answer.


# 33. Search in Rotated Sorted Array

## Problem

Given a rotated sorted array of **unique** integers `nums` and an integer `target`, return the index of `target` if it exists; otherwise, return `-1`.

---

## Intuition

A rotated sorted array is not fully sorted, so a normal Binary Search cannot be applied directly.

**Key Observation:**

> At every step, **at least one half of the array is always sorted**.

The idea is to:

1. Identify the sorted half.
2. Check whether the target lies inside the sorted half.
3. If yes, search in that half.
4. Otherwise, search in the other half.

---

## Algorithm

1. Initialize two pointers:
   - `left = 0`
   - `right = len(nums) - 1`
2. Find the middle index.
3. If `nums[mid] == target`, return `mid`.
4. Determine which half is sorted.
5. Check if the target belongs to the sorted half.
6. Move the search boundaries accordingly.
7. Repeat until the search space becomes empty.

---

## Conditions

### Case 1: Left Half is Sorted

```python
nums[left] <= nums[mid]
```

Target lies in left half:

```python
nums[left] <= target < nums[mid]
```

- Search Left

Otherwise:

- Search Right

---

### Case 2: Right Half is Sorted

```python
nums[left] > nums[mid]
```

Target lies in right half:

```python
nums[mid] < target <= nums[right]
```

- Search Right

Otherwise:

- Search Left

---

## Decision Tree

```text
                 nums[mid] == target
                        │
                 Yes → Return

                        │
                       No
                        │
         nums[left] <= nums[mid] ?
               /                 \
            Yes                   No
             │                     │
     Left Half Sorted      Right Half Sorted
             │                     │
Target in Left Half?      Target in Right Half?
        /      \                /       \
      Yes      No             Yes       No
       │        │              │         │
 Search Left Search Right Search Right Search Left
```


## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(log n)** |
| Space | **O(1)** |

---

## Key Takeaways

- A rotated sorted array is not fully sorted.
- At least one half is always sorted.
- Identify the sorted half first.
- Check whether the target belongs to that half.
- Eliminate half of the search space in every iteration.
- Binary Search still works in **O(log n)**.

---

## Related Problems

- 81. Search in Rotated Sorted Array II
- 153. Find Minimum in Rotated Sorted Array
- 154. Find Minimum in Rotated Sorted Array II
- 189. Rotate Array


# 875. Koko Eating Bananas

**Difficulty:** Medium  
**Pattern:** Binary Search on Answer

---

# Problem Statement

Koko has `n` piles of bananas, where `piles[i]` represents the number of bananas in the `i-th` pile.

She chooses a fixed eating speed `k` (bananas/hour). Every hour, she eats bananas from **only one pile**:

- If the pile has at least `k` bananas, she eats exactly `k` bananas.
- If the pile has fewer than `k` bananas, she eats the entire pile and cannot start another pile during the same hour.

Return the **minimum** integer `k` such that Koko can finish all bananas within `h` hours.

---

# Intuition

- A smaller eating speed requires more hours.
- A larger eating speed requires fewer hours.
- We need to find the **minimum valid speed**.

Since the required hours decrease as the eating speed increases, the search space is **monotonic**, making it suitable for **Binary Search on Answer**.

---

# Approach

1. Set the search range:
   - Minimum speed = `1`
   - Maximum speed = `max(piles)`

2. Perform Binary Search on the eating speed.

3. For each candidate speed:
   - Calculate the total hours required to finish all piles.
   - Hours required for one pile:
     ```
     ceil(pile / speed)
     ```
     Integer implementation:
     ```python
     (pile + speed - 1) // speed
     ```

4. If the total hours are within `h`:
   - Store the current speed as a possible answer.
   - Try to find a smaller valid speed.

5. Otherwise:
   - Increase the eating speed.

6. Return the minimum valid speed.

---

# Algorithm

1. Initialize the search range:
   - `left = 1`
   - `right = max(piles)`

2. While `left <= right`:
   - Find the middle speed.
   - Calculate the total hours required for all piles.
   - If the required hours are less than or equal to `h`:
     - Save the current speed as the answer.
     - Search the left half for a smaller valid speed.
   - Otherwise:
     - Search the right half by increasing the speed.

3. Return the minimum valid speed.

---

# Complexity Analysis

### Time Complexity

- Binary Search: **O(log(max(piles)))**
- Checking all piles for each candidate speed: **O(n)**

**Overall:**

```text
O(n × log(max(piles)))
```

### Space Complexity

```text
O(1)
```

---

# Key Observations

- Binary Search is performed on the **answer**, not on the array.
- The search range is from **1** to **max(piles)**.
- The hours required for one pile are calculated using:
  ```python
  (pile + speed - 1) // speed
  ```
- If a particular eating speed is valid, every larger speed will also be valid.
- The objective is to find the **smallest** valid eating speed.

---

# Pattern Recognition

Use **Binary Search on Answer** when:

- The answer lies within a search range.
- You can efficiently determine whether a candidate answer is valid.
- The validity follows a monotonic property (False → True or True → False).

### Similar Problems

- 875. Koko Eating Bananas
- 1011. Capacity To Ship Packages Within D Days
- 410. Split Array Largest Sum
- 1482. Minimum Number of Days to Make m Bouquets
- Aggressive Cows