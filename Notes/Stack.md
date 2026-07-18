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
