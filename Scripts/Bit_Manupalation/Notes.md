# Data Structures & Algorithms in Python
## Bit Manipulation — Part 1

> A comprehensive introduction to Bit Manipulation. Understanding these fundamental core concepts is essential for solving optimized binary-related problems in competitive programming and technical interviews.

---

## Table of Contents
1. [Number Conversions](#1-number-conversions)
2. [Low-Level Memory Representation](#2-low-level-memory-representation)
3. [Bitwise Operators](#3-bitwise-operators)
4. [Shift Operations](#4-shift-operations)
5. [The Bitwise NOT Operator](#5-the-bitwise-not-operator)

---

## 1. Number Conversions

Computers operate natively in **binary** (base-2, `0`s and `1`s), whereas humans typically use the **decimal** system (base-10). Converting between the two is a foundational skill.

---

### A. Decimal → Binary Conversion

**Method:** Repeatedly divide the integer by `2` and track the remainder until the quotient becomes `0`. The binary sequence is then read from **bottom to top**.

**Example: Convert 9 to Binary**

| Step | Division | Quotient | Remainder |
|------|----------|----------|-----------|
| 1    | 9 ÷ 2    | 4        | **1**     |
| 2    | 4 ÷ 2    | 2        | **0**     |
| 3    | 2 ÷ 2    | 1        | **0**     |
| 4    | 1 ÷ 2    | 0        | **1**     |

Reading remainders bottom-to-top: **`1001`**

#### Python Implementation

```python
def convert_to_binary(num: int) -> str:
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num //= 2  # Integer division

    # Reverse: remainders are collected bottom-to-top
    return result[::-1]
```

| Complexity | Value | Reason |
|---|---|---|
| **Time** | O(log₂ n) | Input size halves each iteration |
| **Space** | O(log₂ n) | Stores bits inside a string |

---

### B. Binary → Decimal Conversion

**Method:** Move from **right to left** (index 0 up to n−1). Multiply each bit by `2^index` and sum all results.

**Example: Convert `1101` to Decimal**

```
Bit positions (right to left):
  Index:  3   2   1   0
  Bit:    1   1   0   1

Calculation:
  (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)
=  8  +  4  +  0  +  1
= 13
```

#### Python Implementation

```python
def convert_to_decimal(binary_str: str) -> int:
    decimal_num = 0
    power = 0
    index = len(binary_str) - 1

    while index >= 0:
        bit = int(binary_str[index])
        decimal_num += bit * (2 ** power)
        index -= 1
        power += 1

    return decimal_num
```

| Complexity | Value | Reason |
|---|---|---|
| **Time** | O(n) | Iterates once over each bit in the string |
| **Space** | O(1) | No extra data structures used |

---

## 2. Low-Level Memory Representation

### Integer Memory Architecture

In lower-level languages like **C++** and **Java**, an integer uses **32 bits** of memory.

- Storing the number `13` (`1101`) fills the first 4 bit positions; the remaining **28 leading positions are padded with `0`**.
- The **31st bit** (leftmost) is designated as the **Sign Bit**:
  - `0` → **Positive** number
  - `1` → **Negative** number

```
 31  30  29  ...  3   2   1   0    ← Bit Index
[ 0 | 0 | 0 | ... | 1 | 1 | 0 | 1 ]   ← Represents 13
  ↑
Sign Bit
```

| Boundary | Value | Formula |
|---|---|---|
| **Largest positive** 32-bit int | `2,147,483,647` | 2³¹ − 1 |
| **Smallest negative** 32-bit int | `-2,147,483,648` | −2³¹ |

---

### 1's and 2's Complement

> Negative numbers are **not** stored simply by flipping the sign bit. The computer uses **2's Complement** representation.

#### 1's Complement
Invert every bit: `0` → `1`, `1` → `0`.

```
13  =  0000...1101
1's complement  =  1111...0010
```

#### 2's Complement
Take the 1's Complement and **add 1**.

**Example: Representing −13 in memory**

```
Step 1 — Write +13 in binary:     0000 0000 0000 0000 0000 0000 0000 1101
Step 2 — Flip all bits (1's C):   1111 1111 1111 1111 1111 1111 1111 0010
Step 3 — Add 1 (2's C = −13):     1111 1111 1111 1111 1111 1111 1111 0011
```

---

## 3. Bitwise Operators

Bitwise operators work directly on individual **bits** rather than full numeric values.

---

### A. Bitwise AND (`&`)

Returns `1` **only if both** corresponding bits are `1`.

```
  1101   (13)
& 0111   ( 7)
  ----
  0101   → 5
```

**Truth Table:**

| A | B | A & B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

---

### B. Bitwise OR (`|`)

Returns `1` if **at least one** corresponding bit is `1`.

```
  1101   (13)
| 0111   ( 7)
  ----
  1111   → 15
```

**Truth Table:**

| A | B | A \| B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

---

### C. Bitwise XOR (`^`)

Returns `1` if the corresponding bits are **different**. Easy rule: if the count of `1`s across both positions is **odd** → `1`; if **even** → `0`.

```
  1101   (13)
^ 0111   ( 7)
  ----
  1010   → 10
```

**Truth Table:**

| A | B | A ^ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

---

## 4. Shift Operations

### A. Right Shift (`>>`)

Shifts all bits **to the right** by `k` positions. The rightmost bits are **dropped**.

**Formula:** `x >> k` = ⌊ x / 2ᵏ ⌋

**Example: `13 >> 1`**
```
Before:  1 1 0 1
After:     1 1 0   [rightmost 1 is dropped]
Result:  0110  →  6
```

**Example: `13 >> 2`**
```
13 ÷ 2² = 13 ÷ 4 = 3
```

---

### B. Left Shift (`<<`)

Shifts all bits **to the left** by `k` positions. Empty right-side slots are **padded with `0`**.

**Formula:** `x << k` = x × 2ᵏ

**Example: `13 << 1`**
```
Before:  1 1 0 1
After:   1 1 0 1 0   [0 appended on right]
Result:  11010  →  26
```

---

## 5. The Bitwise NOT Operator (`~`)

Flips **every bit** of the number, including the sign bit.

### Process for Calculating `~x`

1. Write the number in 32-bit binary.
2. Flip all bits.
3. **Check the sign bit** of the result:
   - If sign bit = `1` (negative): apply 2's complement to find the magnitude, then make it negative.
   - If sign bit = `0` (positive): read the value directly.

---

#### Example 1: `~13`

```
13 in 32-bit:        0000...1101
Flip all bits:       1111...0010   ← sign bit = 1 (negative)

Apply 2's complement to find magnitude:
  Flip again:        0000...1101
  Add 1:             0000...1110   = 14

Result: -14
```

---

#### Example 2: `~(-13)`

```
-13 in 32-bit:       1111...0011   (2's complement of 13)
Flip all bits:       0000...1100   ← sign bit = 0 (positive)

Read value directly: 8 + 4 = 12

Result: 12
```

---

### Short Rule

> **`~x` always equals `-(x + 1)`**

| x   | ~x  |
|-----|-----|
| 13  | -14 |
| -13 | 12  |
| 0   | -1  |
| -1  | 0   |

---

## Quick Reference: All Operators

| Operator | Symbol | Rule | Example |
|----------|--------|------|---------|
| AND | `&` | 1 only if both bits are 1 | `13 & 7 = 5` |
| OR | `\|` | 1 if at least one bit is 1 | `13 \| 7 = 15` |
| XOR | `^` | 1 if bits differ | `13 ^ 7 = 10` |
| NOT | `~` | Flip all bits | `~13 = -14` |
| Right Shift | `>>` | Divide by 2ᵏ (floor) | `13 >> 1 = 6` |
| Left Shift | `<<` | Multiply by 2ᵏ | `13 << 1 = 26` |

---

## What's Coming in Part 2

The next session will cover **coding solutions** for bit manipulation problems, including:

- Bit swapping
- Extracting specific bits
- Setting specific bits
- Clearing specific bits
- Toggling specific bit positions

---