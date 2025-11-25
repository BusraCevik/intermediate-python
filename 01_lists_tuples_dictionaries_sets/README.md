markdown
## 🧠 Python Data Structure Comparison
---
### 📌 List

- **Ordered**
- **Mutable**
- **Allows duplicates**
- Supports indexing and slicing  
**Use when:**  
You need a general-purpose sequence where order matters and the data may change.

**Example:**
```python
my_list = [10, 20, 30]
````

---

### 📌 Tuple

* **Ordered**
* **Immutable**
* **Allows duplicates**
* Memory-efficient and faster than lists
  **Use when:**
  You want a fixed collection of data that should not change.

**Example:**

```python
my_tuple = (10, 20, 30)
```

---

### 📌 Dictionary

* **Ordered (Python 3.7+)**
* **Mutable**
* **Does not allow duplicate keys**
* Stores data as `key → value` pairs
  **Use when:**
  Elements have meaningful identifiers (e.g., name, age, id).

**Example:**

```python
student = {"name": "Max", "age": 22}
```

---

### 📌 Set

* **Unordered**
* **Mutable**
* **Does not allow duplicates**

  **Use when:**
  You need to remove duplicates or perform mathematical set operations.

**Example:**

```python
my_set = {1, 2, 3}
```

---

### 📊 Quick Comparison Table

| Structure      | Ordered   | Mutable | Allows Duplicates | Typical Use Case           |
| -------------- | --------- | ------- | ----------------- | -------------------------- |
| **List**       | ✔️        | ✔️      | ✔️                | General-purpose sequence   |
| **Tuple**      | ✔️        | ❌       | ✔️                | Fixed data, performance    |
| **Dictionary** | ✔️ (3.7+) | ✔️      | Keys ❌            | Key–value data             |
| **Set**        | ❌         | ✔️      | ❌                 | Deduplication, fast lookup |

---

### 🎯 Simple Memory Hooks

* **List:** A notebook you can edit anytime
* **Tuple:** A printed book you cannot modify
* **Dictionary:** A dictionary of word → definition
* **Set:** A basket that never keeps duplicates

```
