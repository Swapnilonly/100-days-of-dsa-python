# Valid Parentheses

## Problem

Given a string `s` containing only the characters:

```text
( ) { } [ ]
```

Return `True` if the string is valid, otherwise return `False`.

A string is valid if:

* Every opening bracket has a corresponding closing bracket.
* Brackets are closed in the correct order.
* Every closing bracket matches the correct opening bracket.

---

## Concept

This problem is solved using a **Stack** because it follows the **LIFO (Last In, First Out)** principle.

### Why Stack?

Whenever we encounter an opening bracket, we don't know when it will be closed.

So, we temporarily store it in a stack.

When a closing bracket appears, it must match the **most recently opened** bracket, which is exactly what the **top of the stack** represents.

---

## Approach

### Step 1: Create a Mapping

Store the relationship between closing and opening brackets.

```python
check = {
    ")": "(",
    "]": "[",
    "}": "{"
}
```

Keys → Closing brackets

Values → Opening brackets

---

### Step 2: Create an Empty Stack

```python
stack = []
```

The stack stores only opening brackets.

---

### Step 3: Traverse the String

For every character:

### Case 1: Opening Bracket

If the character is **not** present in `check`, it is an opening bracket.

```python
if ch not in check:
    stack.append(ch)
```

Push it onto the stack.

---

### Case 2: Closing Bracket

If the character is a closing bracket:

#### Check 1

If the stack is empty,

```python
if not stack:
    return False
```

there is no opening bracket to match.

---

#### Check 2

Compare the top element of the stack with the expected opening bracket.

```python
if stack[-1] != check[ch]:
    return False
```

If they don't match, the string is invalid.

---

#### Check 3

If they match,

```python
stack.pop()
```

remove the opening bracket since it has been successfully matched.

---

### Step 4: Final Check

After processing every character,

```python
return len(stack) == 0
```

If the stack is empty,

* Every opening bracket found its matching closing bracket.
* Return `True`.

Otherwise,

Some opening brackets remain unmatched.

Return `False`.

---

## Time Complexity

* **O(n)**

Each character is pushed and popped at most once.

---

## Space Complexity

* **O(n)**

In the worst case, all characters are opening brackets and remain in the stack.

---

## Key Learning

* Stack is the best choice whenever we need to match the **most recent** element first.
* Dictionary provides an efficient way to map closing brackets to their corresponding opening brackets.
* `if ch not in check` checks **dictionary keys**, not values.
* Always check `if not stack` before accessing `stack[-1]` or calling `stack.pop()` to avoid errors.
* The stack must be **empty at the end** for the string to be valid.




# 155. Min Stack

## Problem

Design a stack that supports the following operations in **O(1)** time.

- `push(x)` → Push element onto the stack.
- `pop()` → Remove the top element.
- `top()` → Return the top element.
- `getMin()` → Retrieve the minimum element in the stack.

---

## Concept

A normal stack allows us to perform **push**, **pop**, and **top** in **O(1)** time.

However, finding the minimum using `min(stack)` takes **O(n)** because we have to scan the entire stack.

To solve this efficiently, we maintain an **auxiliary stack (min_stack)**.

The `min_stack` stores the minimum element seen so far after every push operation.

This allows `getMin()` to return the minimum element in **O(1)** time.

---

## Approach

- Maintain two stacks:
  - `stack` → Stores all elements.
  - `min_stack` → Stores the minimum element corresponding to each position.

### Push

- Push the value into the main stack.
- If `min_stack` is empty, push the value.
- Otherwise, push:

```python
min(current_value, min_stack[-1])
```

This ensures the top of `min_stack` always contains the current minimum.

### Pop

- Remove the top element from both stacks.

### Top

- Return the top element of the main stack.

### Get Minimum

- Return the top element of `min_stack`.

---

## Time Complexity

- **Push:** O(1)
- **Pop:** O(1)
- **Top:** O(1)
- **Get Minimum:** O(1)

---

## Space Complexity

- **O(n)**

An extra stack is maintained to store the minimum value at every position.

---

## Key Learning

- A normal stack cannot return the minimum element in **O(1)**.
- Using an auxiliary stack allows all operations to remain **O(1)**.
- `min_stack` stores the minimum value up to the current position, not just newly inserted minimum values.
- Duplicating minimum values avoids recalculating the minimum after a `pop()` operation.
- This is one of the most common stack interview questions and demonstrates how an extra data structure can optimize query operations.


# 844. Backspace String Compare

## Problem

Given two strings `s` and `t` containing lowercase letters and the `'#'` character, determine if they are equal after processing all backspaces.

- `'#'` represents a backspace character.
- A backspace deletes the character immediately before it.
- Return `true` if both processed strings are equal; otherwise, return `false`.

---

## Concept

Instead of building the final strings using a stack, we can process both strings **from right to left**.

Why?

- A `'#'` always deletes the character to its left.
- While traversing backwards, we already know how many characters need to be skipped.
- Maintain a **skip counter** to keep track of pending deletions.
- This eliminates the need for an extra stack and achieves **O(1)** space.

---

## Approach

- Initialize two pointers:
  - `i` at the end of `s`
  - `j` at the end of `t`
- Maintain two skip counters:
  - `skipS`
  - `skipT`
- For each string:
  - If current character is `'#'`, increment the skip counter.
  - If current character is a letter and `skip > 0`, decrement the skip counter and skip the character.
  - Otherwise, the character is valid.
- Compare the valid characters of both strings.
- If they differ, return `false`.
- Continue until both strings are completely processed.
- If no mismatch is found, return `true`.

---

## Time Complexity

- **O(n + m)**

Each pointer moves from right to left only once.

---

## Space Complexity

- **O(1)**

Only a few variables (`i`, `j`, `skipS`, `skipT`) are used regardless of input size.

---

## Key Learning

- Traversing from **right to left** is an effective technique when characters affect previous elements.
- Skip counters simulate backspaces without constructing new strings.
- Using two pointers removes the need for auxiliary data structures like stacks.
- Always think about processing the input in reverse when operations modify previous elements.
- This is a classic example of optimizing **space complexity** from **O(n)** to **O(1)**.

---

## Comparison

| Approach | Time | Space |
|----------|------|-------|
| Stack | O(n + m) | O(n + m) |
| Two Pointers + Skip Count | O(n + m) | O(1) |

---

## Interview Tip

If the interviewer asks for an optimized solution, avoid building the processed strings.

Instead, explain:

- Traverse both strings from **right to left**.
- Use **skip counters** to ignore deleted characters.
- Compare only the valid characters.
- This satisfies the follow-up requirement of **O(n) time** and **O(1) extra space**.


# Daily Temperatures

**Problem Link:** https://leetcode.com/problems/daily-temperatures/

## Problem Statement

Given an array `temperatures`, return an array `answer` such that:

- `answer[i]` is the number of days to wait after the `i-th` day to get a warmer temperature.
- If there is no future warmer day, return `0`.

---

## Example

**Input**

```text
temperatures = [73,74,75,71,69,72,76,73]
```

**Output**

```text
[1,1,4,2,1,1,0,0]
```

---

# Brute Force Approach

## Intuition

For every temperature, check all temperatures to its right until a warmer temperature is found.

If found:

- Return the distance.

Otherwise:

- Return 0.

---

## Algorithm

1. Iterate through every temperature.
2. Check all elements on the right.
3. If a warmer temperature is found:
   - Store `j - i`.
4. Otherwise store `0`.

---

## Complexity

- Time Complexity: **O(n²)**
- Space Complexity: **O(1)**

---

# Optimal Approach (Monotonic Stack)

## Intuition

Instead of searching the right side repeatedly, keep the indices of temperatures that are still waiting for a warmer day.

Whenever the current temperature becomes greater than the temperature at the top of the stack, we have found the next warmer day for that index.

---

## Why Store Indices?

We need the number of days.

Formula:

```text
current_index - previous_index
```

If we only store temperatures, we cannot calculate the distance.

---

## Monotonic Decreasing Stack

The stack stores indices whose temperatures are in decreasing order.


## Algorithm

1. Create an answer array filled with `0`.
2. Create an empty stack.
3. Traverse the array from left to right.
4. While:
   - stack is not empty
   - current temperature > temperature at stack top
5. Pop the previous index.
6. Store:

```text
answer[previous_index] = current_index - previous_index
```

7. Push the current index.
8. Return the answer array.


## Complexity

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

---

# Key Takeaways

- Store **indices**, not temperatures.
- The stack keeps temperatures in **decreasing order**.
- Every index is pushed **once** and popped **once**.
- Each element is processed at most two times.
- This is a classic **Next Greater Element** pattern.

---

# Similar Problems

- Next Greater Element I
- Next Greater Element II
- Stock Span
- Largest Rectangle in Histogram
- Trapping Rain Water (Stack)
- Asteroid Collision




# 150. Evaluate Reverse Polish Notation

## Problem Statement

Evaluate the value of an arithmetic expression in **Reverse Polish Notation (RPN)**.

Valid operators:

- `+`
- `-`
- `*`
- `/`

Each operand may be an integer or another expression.

> Division between two integers should truncate toward zero.

---

## Approach

We use a **stack** to evaluate the expression.

### Algorithm

1. Traverse each token.
2. If the token is a number, push it onto the stack.
3. If the token is an operator:
   - Pop the top two elements.
   - The **first pop** is the **right operand**.
   - The **second pop** is the **left operand**.
   - Perform the operation.
   - Push the result back onto the stack.
4. After processing all tokens, the stack contains one element, which is the answer.


## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## Key Takeaways

- Use a **stack** to evaluate Reverse Polish Notation.
- Push every number onto the stack.
- For an operator:
  - First pop → Right operand
  - Second pop → Left operand
- Perform the operation and push the result back.
- Use `int(a / b)` to truncate division toward zero.
- Every token is processed exactly once, giving **O(n)** time complexity.

---

## Related Problems

- 20. Valid Parentheses
- 155. Min Stack
- 739. Daily Temperatures
- 394. Decode String
- 224. Basic Calculator
- 227. Basic Calculator II





# 84. Largest Rectangle in Histogram

## Problem Statement

Given an array `heights` representing the height of histogram bars, where each bar has a width of **1**, return the **area of the largest rectangle** that can be formed in the histogram.

---

## Approach

We use a **Monotonic Increasing Stack** to efficiently find the largest rectangle.

### Key Idea

Treat every bar as the **height of the rectangle**.

For each bar, determine:

- **Nearest Smaller Element to the Left (NSL)**
- **Nearest Smaller Element to the Right (NSR)**

The rectangle can expand between these two smaller elements.

```text
Width = NSR - NSL - 1
Area = Height × Width
```

Instead of explicitly computing NSL and NSR arrays, we calculate the area **while popping elements from the stack**.

To ensure every bar is processed, append a **sentinel value (`0`)** at the end of the array.

---

### Algorithm

1. Append `0` to the end of `heights`.
2. Initialize an empty stack to store indices.
3. Traverse the histogram from left to right.
4. While the current height is smaller than the height at the stack top:
   - Pop the top index.
   - Current index becomes the **Nearest Smaller to Right (NSR)**.
   - New stack top becomes the **Nearest Smaller to Left (NSL)**.
   - Calculate the rectangle width.
   - Compute the area and update the maximum area.
5. Push the current index onto the stack.
6. Return the maximum area.

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## Key Takeaways

- Use a **Monotonic Increasing Stack**.
- Store **indices**, not heights.
- Treat every bar as the rectangle's height.
- Expand only through **consecutive bars** with height **>= current height**.
- Area is calculated **when an element is popped**, not when it is pushed.
- Current index acts as the **Nearest Smaller to Right (NSR)**.
- Stack top after popping acts as the **Nearest Smaller to Left (NSL)**.
- Append a **sentinel value (`0`)** to automatically process all remaining bars.
- Every index is pushed and popped at most once, resulting in **O(n)** time complexity.

---

## Related Problems

- 85. Maximal Rectangle
- 42. Trapping Rain Water
- 907. Sum of Subarray Minimums
- 496. Next Greater Element I
- 503. Next Greater Element II
- 739. Daily Temperatures
- 901. Online Stock Span



# 496. Next Greater Element I

## Problem Statement

You are given two **0-indexed** arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each element in `nums1`, find its **next greater element** in `nums2`. The next greater element is the first element to the right that is greater than the current element. If no such element exists, return `-1`.

---

## Approach

- Use a **monotonic decreasing stack** to compute the next greater element for every element in `nums2`.
- Traverse `nums2` from **right to left**.
- Remove all elements from the stack that are **smaller than or equal to** the current element.
- If the stack is not empty, its top is the next greater element.
- Store the result in a **HashMap (Dictionary)**.
- Traverse `nums1` and fetch answers directly from the HashMap.

---

## Algorithm

1. Initialize an empty stack and a HashMap.
2. Traverse `nums2` from right to left.
3. While the stack is not empty and `stack.top <= current`, pop the stack.
4. If the stack is empty, store `-1` as the next greater element.
5. Otherwise, store `stack.top` as the next greater element.
6. Push the current element onto the stack.
7. Traverse `nums1` and build the answer using the HashMap.

## Time Complexity

- Processing `nums2`: **O(n)**
- Processing `nums1`: **O(m)**

**Overall:** **O(n + m)**

> `n = len(nums2)`
>
> `m = len(nums1)`

---

## Space Complexity

- Stack: **O(n)**
- HashMap: **O(n)**
- Output List: **O(m)**

**Overall:** **O(n + m)**

> **Auxiliary Space (excluding output):** **O(n)**

---

## Key Takeaways

- Traverse **right to left**.
- Maintain a **monotonic decreasing stack**.
- Pop all elements **less than or equal to** the current element.
- The stack top is the **next greater element**.
- Push each element **exactly once**.
- Each element is **pushed once** and **popped at most once**, giving an amortized **O(n)** solution.

---

## Common Mistakes

- Traversing from left to right.
- Using the wrong pop condition (`>` instead of `<=`).
- Forgetting to push the current element after processing.
- Pushing the current element multiple times.
- Calculating the answer inside the `while` loop.
- Assuming the nested `while` loop makes the algorithm **O(n²)**.

---

## Pattern

```text
Traverse from Right to Left

while stack is not empty AND stack.top <= current
    pop()

if stack is empty
    answer = -1
else
    answer = stack.top

push(current)
```

---

## Related Problems

- 503. Next Greater Element II
- 739. Daily Temperatures
- 901. Online Stock Span
- 84. Largest Rectangle in Histogram
- 42. Trapping Rain Water (Stack Approach)



