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