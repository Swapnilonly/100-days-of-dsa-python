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