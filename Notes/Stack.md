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



# 503. Next Greater Element II

## Problem Statement

Given a **circular integer array** `nums`, return an array `answer` where `answer[i]` is the **first greater element** to the right of `nums[i]`. If no greater element exists, return `-1`.

A circular array means that after the last element, traversal continues from the first element.

---

## Example

**Input**

```text
nums = [1,2,1]
```

**Output**

```text
[2,-1,2]
```

**Explanation**

- Next greater of `1` is `2`.
- `2` has no greater element.
- The last `1` wraps around and finds `2`.

---

## Intuition

A normal **Next Greater Element** problem can be solved using a **Monotonic Decreasing Stack**.

Since the array is **circular**, every element should also be able to search beyond the last index.

Instead of physically duplicating the array, we simulate a second traversal by iterating **2 × n** times and using modulo (`%`) to wrap around.

---

## Approach

- Maintain a **Monotonic Decreasing Stack**.
- Traverse the array from **right to left**.
- Iterate from `2 * n - 1` down to `0`.
- Compute the actual index using:

```python
i = j % n
```

- Remove all elements from the stack that are **smaller than or equal to** the current element.
- If the stack is not empty, its top is the next greater element.
- Push the current element onto the stack.

---

## Algorithm

1. Initialize an empty stack.
2. Create a result array filled with `-1`.
3. Traverse from `2 * n - 1` to `0`.
4. Convert the virtual index into the actual index using `% n`.
5. Remove all elements from the stack that are less than or equal to the current element.
6. If the stack is not empty, store the top element as the next greater element.
7. Push the current element onto the stack.
8. Return the result array.

---

## Why `2 × n` Traversal?

A circular array allows traversal to continue from the beginning after reaching the last element.

Instead of creating a duplicate array, we simulate circular traversal using:

```python
i = j % n
```

This ensures every element gets one complete circular search while keeping the solution efficient.

---

## Time Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

---

## Key Takeaways

- Use a **Monotonic Decreasing Stack**.
- Simulate the circular array using `% n`.
- Traverse **2 × n** times.
- Each element is pushed and popped at most once.
- Store answers using **indices**, not values.

---

## Pattern

- Monotonic Stack
- Circular Array
- Next Greater Element

---

## Related Problems

- **496.** Next Greater Element I
- **739.** Daily Temperatures
- **84.** Largest Rectangle in Histogram
- **901.** Online Stock Span
- **42.** Trapping Rain Water



# 225. Implement Stack using Queues

## Problem Statement

Implement a **Last In First Out (LIFO)** stack using only the standard operations of a queue.

Implement the following functions:

- `push(x)` – Push element `x` onto the stack.
- `pop()` – Removes the element on the top of the stack and returns it.
- `top()` – Returns the top element.
- `empty()` – Returns `true` if the stack is empty, otherwise `false`.

**Queue operations allowed:**

- `push to back`
- `peek/pop from front`
- `size`
- `is empty`

---

## Example

**Input**

```text
["MyStack","push","push","top","pop","empty"]
[[],[1],[2],[],[],[]]
```

**Output**

```text
[null,null,null,2,2,false]
```

---

## Intuition

A queue follows **FIFO (First In First Out)**, while a stack follows **LIFO (Last In First Out)**.

To make a queue behave like a stack, every newly inserted element is moved to the **front** of the queue by rotating the existing elements.

As a result:

- The newest element is always at the front.
- `pop()` simply removes the front element.
- `top()` simply returns the front element.

---

## Approach (Single Queue)

1. Insert the new element at the rear of the queue.
2. Rotate the queue `size - 1` times.
3. After rotation, the newly inserted element becomes the front.
4. `pop()` removes the front element.
5. `top()` returns the front element.
6. `empty()` checks whether the queue is empty.

---

## Algorithm

For **push(x)**

- Insert `x` into the queue.
- Rotate the queue `current_size - 1` times.

For **pop()**

- Remove and return the front element.

For **top()**

- Return the front element.

For **empty()**

- Return whether the queue is empty.

---

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Push | **O(n)** | O(1) |
| Pop | **O(1)** | O(1) |
| Top | **O(1)** | O(1) |
| Empty | **O(1)** | O(1) |

Overall Auxiliary Space: **O(1)**

---

## Key Takeaways

- Queue is **FIFO**, Stack is **LIFO**.
- Rotate the queue after every push so that the newest element reaches the front.
- After rotation:
  - Front = Stack Top
  - `popleft()` = Stack Pop
- Push becomes expensive (**O(n)**), while Pop and Top become **O(1)**.

---

## Pattern

- Queue
- Stack Simulation
- Data Structure Design

---

## Related Problems

- 232. Implement Queue using Stacks
- 155. Min Stack
- 622. Design Circular Queue
- 641. Design Circular Deque




# 901. Online Stock Span

## Problem Statement

Design a data structure that collects daily stock prices and returns the span of the current day's stock price.

The span of the stock’s price is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

---

## Intuition

A previous stock price greater than the current price acts as a boundary. All consecutive prices less than or equal to the current price contribute to its span.

To avoid scanning previous prices repeatedly, maintain a Monotonic Decreasing Stack.

---

## Approach

- Use a Monotonic Decreasing Stack.
- Store `(price, span)` instead of only prices.
- Initialize `span = 1` for every new price.
- While the top of the stack has a price less than or equal to the current price:
  - Add the stored span to the current span.
  - Pop the top element.
- Push the current `(price, span)` onto the stack.
- Return the calculated span.

---

## Algorithm

1. Initialize an empty stack.
2. For every incoming stock price:
   - Set `span = 1`.
   - While the stack is not empty and the top price is less than or equal to the current price:
     - Add the top element's span to `span`.
     - Pop the top element.
   - Push `(currentPrice, span)` onto the stack.
   - Return `span`.

---

## Complexity Analysis

- **Time Complexity:** `O(1)` Amortized
- **Worst Case (Single Call):** `O(n)`
- **Space Complexity:** `O(n)`

---

## Key Takeaways

- Monotonic Decreasing Stack is the optimal choice.
- Store `(price, span)` instead of only prices.
- Every stock price is pushed exactly once.
- Every stock price is popped at most once.
- The total number of push and pop operations is linear, giving an amortized `O(1)` solution.

---

## Pattern

- Monotonic Stack
- Stack
- Amortized Analysis

---

## Related Problems

- 496. Next Greater Element I
- 503. Next Greater Element II
- 739. Daily Temperatures
- 84. Largest Rectangle in Histogram
- 1475. Final Prices With a Special Discount in a Shop
- 402. Remove K Digits



# 735. Asteroid Collision

## Problem Statement

We are given an array of integers representing asteroids in a row.

- Positive value (`> 0`) → Asteroid moves to the **right**.
- Negative value (`< 0`) → Asteroid moves to the **left**.

When two asteroids moving in opposite directions collide:

- The smaller asteroid explodes.
- If both have the same size, both explode.
- Asteroids moving in the same direction never collide.

Return the state of the asteroids after all collisions.

---

## Approach (Stack)

Use a stack to keep track of the asteroids that have survived so far.

For each asteroid:

1. Assume the current asteroid is alive.
2. A collision is possible **only when**:
   - Top of the stack is moving right (`> 0`)
   - Current asteroid is moving left (`< 0`)
3. Compare the sizes of both asteroids:
   - If the current asteroid is larger, remove the top asteroid and continue checking.
   - If the top asteroid is larger, the current asteroid is destroyed.
   - If both are equal, both are destroyed.
4. If the current asteroid survives all possible collisions, push it onto the stack.

---

## Collision Conditions

| Stack Top | Current | Collision |
|-----------|---------|-----------|
| + | + | ❌ No |
| - | - | ❌ No |
| - | + | ❌ No |
| + | - | ✅ Yes |

Only this condition causes a collision:

```python
stack[-1] > 0 and asteroid < 0
```

---

## Algorithm

1. Initialize an empty stack.
2. Iterate through each asteroid.
3. Assume the asteroid is alive.
4. While collision is possible:
   - If current asteroid is larger, pop the stack.
   - If stack top is larger, current asteroid is destroyed.
   - If both are equal, destroy both.
5. If the current asteroid survives, push it onto the stack.
6. Return the stack.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Key Takeaways

- Stack is used to maintain the surviving asteroids.
- Only one collision direction is possible:
  - Right-moving asteroid followed by a left-moving asteroid.
- Each asteroid is pushed and popped at most once, giving an overall `O(n)` time complexity.
- Repeated collisions are handled naturally using a `while` loop.

---

## Related Problems

- 20. Valid Parentheses
- 155. Min Stack
- 496. Next Greater Element I
- 503. Next Greater Element II
- 739. Daily Temperatures
- 901. Online Stock Span




# 402. Remove K Digits

## Problem Statement

Given a non-negative integer `num` represented as a string and an integer `k`, remove `k` digits from the number so that the new number is the smallest possible.

Return the resulting number as a string.

**Note:**
- The input number does not contain leading zeros except for the number `"0"`.
- The output should not contain leading zeros unless the answer is `"0"`.

---

## Approach (Monotonic Increasing Stack)

Use a **Monotonic Increasing Stack** to construct the smallest possible number.

### Key Idea

Whenever the current digit is **smaller** than the top of the stack, removing the larger digit from the stack results in a smaller overall number.

Continue removing digits while:

- The stack is not empty.
- `k > 0`
- Top of the stack is greater than the current digit.

If removals are still left after processing all digits, remove digits from the **end** of the stack since they are the largest remaining digits.

Finally:

- Convert the stack into a string.
- Remove leading zeros.
- Return `"0"` if the result becomes empty.

---

## Why Monotonic Increasing Stack?

The stack is maintained in **increasing order**.

Example:

```text
Input: 1432219

Stack:

1
1 4
1 3      (4 removed)
1 2      (3 removed)
1 2 2
1 2 1    (2 removed)
1 2 1 9
```

The resulting number is the smallest possible after removing `k` digits.

---

## Algorithm

1. Initialize an empty stack.
2. Traverse each digit in the string.
3. While:
   - Stack is not empty.
   - `k > 0`
   - Top of the stack is greater than the current digit.
   - Pop the stack and decrement `k`.
4. Push the current digit into the stack.
5. If `k > 0`, remove the last `k` digits from the stack.
6. Convert the stack to a string.
7. Remove leading zeros.
8. If the string is empty, return `"0"`.
9. Otherwise, return the resulting string.

---

## Dry Run

**Input**

```text
num = "1432219"
k = 3
```

| Current Digit | Stack | Action |
|---------------|-------|--------|
| 1 | 1 | Push |
| 4 | 1 4 | Push |
| 3 | 1 3 | Pop 4, Push 3 |
| 2 | 1 2 | Pop 3, Push 2 |
| 2 | 1 2 2 | Push |
| 1 | 1 2 1 | Pop 2, Push 1 |
| 9 | 1 2 1 9 | Push |

Result:

```text
1219
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Key Takeaways

- Greedily remove larger previous digits whenever a smaller digit appears.
- Maintain a **Monotonic Increasing Stack**.
- If removals remain after traversal, remove digits from the end.
- Leading zeros should be removed before returning the answer.
- Characters `'0'` to `'9'` can be compared directly without converting them to integers.

---

## Common Mistakes

- Using `>=` instead of `>` in the comparison.
- Forgetting to remove remaining digits when `k > 0`.
- Forgetting to remove leading zeros.
- Converting characters to integers unnecessarily.
- Returning an empty string instead of `"0"`.

---

## Related Problems

- 496. Next Greater Element I
- 503. Next Greater Element II
- 739. Daily Temperatures
- 901. Online Stock Span
- 84. Largest Rectangle in Histogram
- 735. Asteroid Collision


# 394. Decode String

**Difficulty:** Medium  
**Pattern:** Stack  
**LeetCode:** https://leetcode.com/problems/decode-string/

---

# Problem Statement

Given an encoded string `s`, decode and return its original string.

Encoding Rule:

```
k[encoded_string]
```

- `k` is the number of times the substring should be repeated.
- Nested encodings are allowed.

### Example

```
Input:
s = "3[a2[c]]"

Output:
"accaccacc"
```

---

# Intuition

The encoded string can contain multiple levels of nested brackets, so we need a way to remember the previous state whenever we enter a new bracket.

Whenever we encounter `'['`, we save:
- The repeat count.
- The string built so far.

When we encounter `']'`, we:
- Restore the previous string.
- Repeat the current substring using the stored repeat count.
- Append the repeated substring to the previous string.

Since nested brackets follow a **Last In, First Out (LIFO)** order, a **stack** is the ideal data structure.

---

# Approach

1. Initialize:
   - A stack for repeat counts.
   - A stack for previously built strings.
   - Variables to store the current number and current string.

2. Traverse the string character by character.

3. If the character is a digit:
   - Build the complete repeat count (handles multi-digit numbers).

4. If the character is `'['`:
   - Store the current repeat count.
   - Store the current string.
   - Reset both values to process the new substring.

5. If the character is `']'`:
   - Retrieve the last stored repeat count.
   - Retrieve the previous string.
   - Repeat the current substring and append it to the previous string.

6. If the character is a letter:
   - Append it to the current string.

7. Continue until the entire string is processed.

8. Return the final decoded string.

---

# Complexity Analysis

### Time Complexity

```
O(n)
```

Each character is processed once.

### Space Complexity

```
O(n)
```

Additional space is used for the stacks and the decoded string.

---

# Key Points

- Use **two stacks**:
  - One for repeat counts.
  - One for previously built strings.
- Supports nested encodings naturally.
- Handles multi-digit repeat counts (e.g., `12[a]`).
- The stack helps restore the previous state after processing each nested substring.v