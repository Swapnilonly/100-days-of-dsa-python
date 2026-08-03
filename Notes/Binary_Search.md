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

