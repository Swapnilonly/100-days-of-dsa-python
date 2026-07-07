# Two Sum

## Problem
Given an integer array `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

## Concept
- Hash Map (Dictionary)
- One Pass Traversal
- Complement Lookup

## Approach
- Create an empty dictionary to store previously visited numbers and their indices.
- Traverse the array once.
- For each element:
  - Calculate its complement:
    ```
    complement = target - nums[i]
    ```
  - Check if the complement already exists in the dictionary.
    - If it exists, return the stored index and the current index.
    - Otherwise, store the current element and its index in the dictionary.
- Since the problem guarantees exactly one solution, the pair will always be found.

## Time Complexity
- **O(n)**
  - Single traversal of the array.
  - Dictionary lookup and insertion take **O(1)** on average.

## Space Complexity
- **O(n)**
  - In the worst case, all elements are stored in the dictionary.

## Key Learning
### A complement is the value you need to complete the target.
- A Hash Map provides constant-time lookup, making it ideal for searching previously seen elements.
- Instead of checking every pair (**O(n²)**), calculate the required complement and search for it in the dictionary.
- Store elements **after** checking for the complement to avoid using the same element twice.
- This is a classic example of the **Complement Pattern** using a Hash Map.
- Dictionary operations (`in`, insertion, lookup) are **O(1)** on average, resulting in an overall **O(n)** solution.