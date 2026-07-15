## Problem
Move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

## Concept
- Two Pointers
- In-place Array Manipulation

## Approach
- Use the Two Pointer technique.
- `i` traverses the entire array.
- `j` keeps track of the position where the next non-zero element should be placed.
- Whenever a non-zero element is found:
  - Swap it with `nums[j]` (only if `i != j` to avoid unnecessary swaps).
  - Increment both `i` and `j`.
- If the current element is `0`, only increment `i`.

## Time Complexity
- **O(n)**

## Space Complexity
- **O(1)**


## Key Learning
- Two pointers can perform in-place array modifications efficiently.
- Avoid unnecessary swaps by checking `i != j`.
- Always ensure pointers are updated correctly to prevent infinite loops.
- Two different types of swapping tuple unpacking and swapping with extra variable temp
- temp = nums[j]
- nums[j] = nums[i]
- nums[i] = temp
- nums[i], nums[j] = nums[j], nums[i]


# Remove Duplicates from Sorted Array

## Problem
Remove duplicates from a sorted array in-place such that each unique element appears only once.
Return the number of unique elements (`k`). The first `k` elements of the array should contain the unique values.

## Concept
- Two Pointers
- In-place Array Manipulation
- Sorted Array

## Approach
- Use the Two Pointer technique.
- `i` keeps track of the last unique element.
- `j` scans the array to find new unique elements.
- If `nums[i] != nums[j]`:
  - Increment `i`.
  - Copy the new unique element (`nums[j]`) to `nums[i]`.
- Continue until the end of the array.
- Return `i + 1` as the count of unique elements.

## Time Complexity
- **O(n)**

## Space Complexity
- **O(1)**

## Key Learning
- In a sorted array, duplicate elements are always adjacent.
- Two pointers help overwrite duplicates without using extra space.
- `i` always points to the last unique element.
- `j` is responsible for traversing the entire array.
- No swapping is required; only overwrite the next unique position.
- The returned value is the number of unique elements (`i + 1`), not the modified array.
- This is a classic in-place array modification problem.


## Common Mistakes
- Forgetting to increment `j` in every iteration can cause an infinite loop.
- Returning `i` instead of `i + 1`.
- Applying this approach to an unsorted array (it only works because the array is sorted).
- Confusing the roles of `i` and `j`.

## Pattern Recognition
- Whenever a problem says:
  - "Sorted Array"
  - "Remove Duplicates"
  - "Modify In-place"
  - "Constant Extra Space"

  → Think **Two Pointers**.

## Related Problems
- Move Zeroes
- Remove Element
- Merge Sorted Array
- Squares of a Sorted Array



## Problem
Given a string `s`, return `true` if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters. Otherwise, return `false`.

## Concept
- String Manipulation
- String Preprocessing
- Character Filtering
- String Reversal

## Approach
- Traverse each character in the string.
- Keep only alphanumeric characters using `isalnum()`.
- Convert uppercase letters to lowercase using `lower()`.
- Merge all valid characters into a new string using `"".join()`.
- Compare the processed string with its reversed version using `[::-1]`.
- If both strings are equal, return `True`; otherwise, return `False`.

## Time Complexity
- **O(n)**

## Space Complexity
- **O(n)**



## Problem
Given `n` non-negative integers representing the heights of vertical lines, find two lines that together with the x-axis form a container that holds the maximum amount of water.

Return the maximum amount of water the container can store.

## Concept
- Two Pointers
- Greedy Approach
- Width × Height Calculation

## Approach
- Place one pointer at the beginning (`left`) and the other at the end (`right`) of the array.
- Calculate the width as `right - left`.
- Calculate the height as the minimum of the two boundary heights.
- Compute the current area using `width × height`.
- Update the maximum area found so far.
- Move the pointer pointing to the shorter line inward.
- If both heights are equal, move either pointer (or both); the optimal solution usually moves one pointer.
- Continue until both pointers meet.

## Time Complexity
- **O(n)**

## Space Complexity
- **O(1)**

## Key Learning
- The container's height is always limited by the shorter of the two lines.
- The width decreases after every pointer movement, so a larger area is only possible by finding a taller line.
- Always move the pointer with the smaller height, as moving the taller one cannot increase the current container height.
- Width is calculated as `right - left`, **not** `right - left + 1`.
- Area is calculated using:
  - `width = right - left`
  - `height = min(height[left], height[right])`
  - `area = width * height`
- Two Pointers reduce the brute-force solution from **O(n²)** to **O(n)**.





## Problem
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much rainwater can be trapped after raining.

## Concept
- Two Pointers
- Prefix Maximum & Suffix Maximum
- Greedy
- Water Level Calculation

## Approach
- Initialize two pointers: `left` at the beginning and `right` at the end.
- Maintain two variables:
  - `left_max` → Maximum height seen from the left.
  - `right_max` → Maximum height seen from the right.
- If `height[left] < height[right]`:
  - Update `left_max` if the current height is greater.
  - Otherwise, trapped water at this index is `left_max - height[left]`.
  - Move the `left` pointer.
- Otherwise:
  - Update `right_max` if the current height is greater.
  - Otherwise, trapped water at this index is `right_max - height[right]`.
  - Move the `right` pointer.
- Continue until both pointers meet.
- Return the total trapped water.

## Time Complexity
- **O(n)**

## Space Complexity
- **O(1)**

## Key Learning
- Water trapped at an index depends on the **smaller** of the tallest bars on its left and right.
- Water at an index is calculated as:
  - `min(left_max, right_max) - current_height`
- If the calculated water is negative, treat it as **0**.
- The shorter boundary determines the maximum water level.
- Two Pointers eliminate the need for Prefix and Suffix arrays, reducing space complexity from **O(n)** to **O(1)**.
- This problem is different from **Container With Most Water**:
  - **Container With Most Water:** `Area = Width × Min(Left Height, Right Height)`
  - **Trapping Rain Water:** `Water = Min(Left Max, Right Max) - Current Height`




# 3Sum

## Problem
Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`

and

```
nums[i] + nums[j] + nums[k] == 0
```

The solution set must **not contain duplicate triplets**.

---

## Concept

- Sorting
- Two Pointers
- Duplicate Handling
- Greedy Pointer Movement

---

## Intuition

After sorting the array:

- Fix one element (`i`).
- Search for the remaining two numbers using the **Two Pointer** technique.
- Since the array is sorted:
  - If the sum is too small, move the **left** pointer.
  - If the sum is too large, move the **right** pointer.
  - If the sum is zero, store the triplet and skip duplicates.

Sorting helps efficiently eliminate duplicate triplets.


## Time Complexity

- Sorting → **O(n log n)**
- Outer Loop → **O(n)**
- Two Pointers → **O(n)**

Overall:

**O(n²)**

---

## Space Complexity

- **O(1)** (excluding the output list)

---

## Key Learning

- Sort the array before applying Two Pointers.
- Fix one element and solve the remaining problem as **2Sum**.
- Skip duplicate values of:
  - `i`
  - `left`
  - `right`
- After finding a valid triplet:
  - Move both pointers.
  - Then skip duplicates.
- Since the array is sorted:
  - Move `left` when the sum is too small.
  - Move `right` when the sum is too large.
- This is the optimal solution with **O(n²)** time complexity and is the standard interview approach.