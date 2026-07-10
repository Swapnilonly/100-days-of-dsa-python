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



# Valid Anagram

## Problem
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, otherwise return `false`.

An **anagram** is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

---

## Concept
- Hash Map (Dictionary)
- Frequency Counting
- One Pass Traversal
- Simultaneous Increment & Decrement

---

## Approach
- If the lengths of the two strings are different, return `False` immediately because they cannot be anagrams.
- Create an empty dictionary `freq` to store character frequencies.
- Traverse both strings simultaneously.
- For each index:
  - Increment the count of the character from `s`.
    ```python
    freq[s[i]] = freq.get(s[i], 0) + 1
    ```
  - Decrement the count of the character from `t`.
    ```python
    freq[t[i]] = freq.get(t[i], 0) - 1
    ```
- After processing all characters:
  - If every value in the dictionary is `0`, both strings contain the same characters with the same frequencies.
  - Otherwise, they are not anagrams.

---

## Time Complexity
- **O(n)**
  - Single traversal through both strings.
  - Checking all dictionary values takes **O(n)** in the worst case.

---

## Space Complexity
- **O(k)**
  - Where `k` is the number of unique characters.
  - In the worst case, `k = n`, so the space complexity becomes **O(n)**.

---

## Key Learning

### Frequency Counting Pattern
- Anagrams always have the **same characters with the same frequencies**.
- Instead of maintaining two separate frequency maps, use **one dictionary**:
  - Increment for characters in `s`.
  - Decrement for characters in `t`.
- If every frequency becomes `0`, the strings are anagrams.
- Checking the string lengths first is an important optimization because strings of different lengths can never be anagrams.
- The expression:
  ```python
  all(value == 0 for value in freq.values())
  ```
  confirms that every character count is balanced.
- Dictionary operations (`get`, insertion, update, lookup) take **O(1)** on average, resulting in an overall **O(n)** solution.

---

## Pattern
**Hash Map + Frequency Counting**

This pattern is commonly used in:
- Valid Anagram
- Group Anagrams
- Ransom Note
- Find All Anagrams in a String
- Permutation in String
- Sliding Window with Character Frequencies





# Majority Element II

## Problem
Find **all elements** that appear **more than ⌊n/3⌋ times** in the given array.

If no such element exists, return an empty list.

## Concept
- Boyer-Moore Voting Algorithm (Extended Version)
- Candidate Elimination
- Frequency Verification

## Approach
- Since an element must appear more than `⌊n/3⌋` times, there can be **at most two majority elements**.
- Maintain two candidates (`candidate1`, `candidate2`) and their counts (`count1`, `count2`).
- Traverse the array once:
  - If the current number matches a candidate, increment its count.
  - If a candidate's count becomes `0`, replace it with the current number.
  - Otherwise, decrement both counts.
- After the first pass, the remaining candidates are only **possible** majority elements.
- Traverse the array again to count their actual frequencies.
- Return the candidates whose frequency is greater than `⌊n/3⌋`.

## Time Complexity
- **O(n)**
  - `O(n)` for selecting possible candidates.
  - `O(n)` for verifying their frequencies.
  - Overall: **O(n)**

## Space Complexity
- **O(1)**

## Key Learning
- There can be **at most two** elements occurring more than `⌊n/3⌋` times.
- The first pass finds only **potential candidates**, not guaranteed answers.
- A second pass is required to verify the actual frequencies.
- The algorithm uses **candidate elimination**, where counts are decreased when encountering a third distinct element.
- This is the **Extended Boyer-Moore Voting Algorithm**, achieving **O(n)** time and **O(1)** extra space.