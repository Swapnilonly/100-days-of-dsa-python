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
