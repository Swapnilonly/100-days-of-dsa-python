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



# Top K Frequent Elements

## Problem
Given an integer array `nums` and an integer `k`, return the **k most frequent elements**.

You may return the answer in **any order**.

---

## Concept
- Hash Map (Frequency Counting)
- Bucket Sort
- Frequency-Based Grouping

---

## Approach
- Count the frequency of each element using a hash map.
- Create a bucket array of size `n + 1`, where each index represents a frequency.
- Store each number in the bucket corresponding to its frequency.
- Traverse the bucket from the highest frequency to the lowest.
- Collect elements until `k` elements have been added to the result.
- Return the result.

---

## Time Complexity
- **O(n)**
  - `O(n)` to count frequencies.
  - `O(n)` to place elements into buckets.
  - `O(n)` to traverse the buckets.
  - Overall: **O(n)**

---

## Space Complexity
- **O(n)**
  - Hash map stores frequencies.
  - Bucket array stores grouped elements.

---

## Key Learning
- A hash map efficiently counts the frequency of each element.
- The maximum possible frequency of any element is `n`, so a bucket array of size `n + 1` is sufficient.
- The bucket index represents the frequency, and each bucket stores all elements with that frequency.
- Traversing the bucket from the end naturally retrieves elements in decreasing order of frequency.
- This Bucket Sort approach avoids sorting the frequency map, improving the time complexity from **O(n log n)** to **O(n)**.
- This problem is a classic example of combining **Hashing + Bucket Sort** for optimal performance.




# Longest Consecutive Sequence

## Problem
Given an unsorted integer array `nums`, return the **length of the longest consecutive sequence**.

You must write an algorithm that runs in **O(n)** time.

---

## Concept
- Hash Set
- Sequence Detection
- Constant Time Lookup

---

## Approach
- Store all elements in a hash set for `O(1)` average lookup.
- Iterate through each unique element in the set.
- Check whether the current element is the **start of a sequence** by verifying that `num - 1` is **not** in the set.
- If it is the start, keep checking for the next consecutive numbers (`num + 1`, `num + 2`, ...) until the sequence ends.
- Track the length of the current sequence.
- Update the maximum sequence length found.
- Return the longest consecutive sequence length.

---

## Time Complexity
- **O(n)**
  - `O(n)` to insert all elements into the hash set.
  - Each element is visited at most once while expanding sequences.
  - Overall: **O(n)**

---

## Space Complexity
- **O(n)**
  - Hash set stores all unique elements.

---

## Key Learning
- A hash set provides **O(1)** average-time membership checks, making it ideal for this problem.
- Only begin counting from numbers that **do not have a predecessor (`num - 1`)**.
- This prevents traversing the same sequence multiple times.
- Each consecutive sequence is explored exactly once, giving an overall **O(n)** time complexity.
- Sorting the array would take **O(n log n)**, which does not satisfy the problem's requirement.
- This problem demonstrates how hashing can replace sorting to achieve linear-time solutions.



# Group Anagrams

## Problem
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Understanding `ord(ch) - ord('a')`
The `ord()` function returns the ASCII (Unicode) value of a character.

An **anagram** is a word or phrase formed by rearranging the letters of another word while using all the original letters exactly once.

## Concept
- Hash Map (Dictionary)
- String Sorting
- Grouping by Common Key

## Approach
- Create an empty dictionary to group anagrams.
- Traverse each string in the input array.
- For each string:
  - Sort its characters.
  - Convert the sorted characters back into a string to use as the dictionary key.
    ```
    key = ''.join(sorted(word))
    ```
  - If the key does not exist in the dictionary:
    - Create a new list with the current word.
  - Otherwise:
    - Append the current word to the existing list.
- After processing all words, return all the dictionary values as the final grouped anagrams.

## Time Complexity
- **O(n × k log k)**
  - `n` = Number of strings.
  - `k` = Average length of each string.
  - Sorting each string takes **O(k log k)**.

## Space Complexity
- **O(n × k)**
  - The hash map stores every string in one of the groups.
  - The sorted keys also require additional space.

## Key Learning
### The sorted string acts as a unique signature for every anagram group.
- Anagrams contain the same characters, so sorting them always produces the same result.
- Use the sorted string as the **key** and store the original strings as the **value**.
- A Hash Map efficiently groups all strings sharing the same sorted representation.
- Dictionary lookup and insertion are **O(1)** on average.
- This is a classic example of the **Grouping Pattern** using a Hash Map.
- Whenever multiple items should be grouped based on a common property, think about generating a unique key and storing them in a dictionary.


## Pattern Recognition
When you encounter problems that ask you to:
- Group similar strings
- Find anagrams
- Classify elements by a common property
- Organize data into categories

Think of:
- **Hash Map**
- **Generate a unique key**
- **Store related elements in a list**

## Optimization (Interview Follow-up)
Instead of sorting every string, count the frequency of each character.
Use the 26-character frequency array as a tuple
This tuple becomes the dictionary key.

### Complexity of Optimized Approach
- **Time Complexity:** O(n × k)
- **Space Complexity:** O(n × k)

This optimization avoids sorting and is commonly asked as a follow-up in interviews.