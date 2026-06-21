# DSA Notes: Infix, Postfix & Prefix Conversions Using Stack
*Course: DSA in Python | Channel: Code and Debug | Part 90*

---

## 1. Core Definitions: Operators and Operands

### Operator
A symbol that represents a specific mathematical or logical action performed on data.

**Examples in Python:** `**` (Power/Exponentiation), `*` (Multiplication), `/` (Division), `+` (Addition), `-` (Subtraction)

### Operand
The actual data values or variables upon which the operator acts.

**Examples:** Operands are usually represented by alphabets (`A-Z`, `a-z`) or numbers (`0-9`).

**Example Expression:** In `5 ** 3`, `5` and `3` are the **operands**, and `**` is the **operator**.

---

## 2. Operator Precedence / Priority

Precedence decides the execution order of operators in an expression when multiple operators are present.

| Operator Level | Operator Symbol | Priority Score |
|---|---|---|
| **Highest** | `**` (Power) | 3 |
| **Medium** | `*` (Multiplication), `/` (Division) | 2 |
| **Lowest** | `+` (Addition), `-` (Subtraction) | 1 |
| **Default/Brackets** | `(`, `)` | 0 |

**Key idea:** A higher priority score means the operator is evaluated *first*. For example, in `A + B * C`, since `*` (score 2) has higher precedence than `+` (score 1), `B * C` is evaluated first.

---

## 3. Expression Types

There are three ways to write algebraic expressions based on the position of operators relative to operands:

| Type | Example | Operator Position | Common Usage |
|---|---|---|---|
| **Infix** | `A + B` | Between operands | Standard in Python, Java, C++ |
| **Postfix** | `A B +` | After operands | Stack-based architecture, engineering calculations (RPN) |
| **Prefix** | `+ A B` | Before operands | LISP-like architectures, expression/syntax trees |

All three notations represent the **same expression** — only the operator's position relative to the operands changes.

---

## 4. Infix to Postfix Conversion

### Logic & Rules
- Iterate through the expression from left to right.
- If an **operand** is encountered, add it directly to the output result.
- If an opening bracket `(` is encountered, push it onto the stack.
- If a closing bracket `)` is encountered, continuously pop from the stack and add to the result until an opening bracket `(` is reached. Discard the opening bracket.
- If an **operator** is encountered, pop elements from the stack and append to the result **while** the top of the stack has an operator with **greater than or equal precedence** (`>=`) to the current operator. Then, push the current operator onto the stack.
- After the loop ends, pop all remaining stack elements to the result.

### Python Code

```python
def precedence(char):
    if char == '**' or char == '^':
        return 3
    elif char in ('*', '/'):
        return 2
    elif char in ('+', '-'):
        return 1
    return 0

def infix_to_postfix(expression):
    stack = []
    result = []

    for char in expression:
        if char.isalnum():  # Operand check
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Discard '('
        else:  # Operator check
            while stack and precedence(stack[-1]) >= precedence(char):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return "".join(result)
```

**Time Complexity:** O(N)
**Space Complexity:** O(N) (due to the auxiliary stack and result storage)

### Worked Example: `A + B * C` → `A B C * +`

| Step | Char | Action Taken | Stack (bottom → top) | Result so far |
|---|---|---|---|---|
| 1 | A | Operand → append to result | (empty) | A |
| 2 | + | Operator, stack empty → push onto stack | `+` | A |
| 3 | B | Operand → append to result | `+` | A B |
| 4 | * | prec(`*`)=2 > prec(top `+`)=1 → don't pop; push `*` | `+ *` | A B |
| 5 | C | Operand → append to result | `+ *` | A B C |
| End | - | Input ends → pop all remaining: `*` then `+` | (empty) | **A B C * +** |

---

## 5. Infix to Prefix Conversion

### Logic & Rules
1. **Reverse** the infix string expression.
2. **Invert the brackets:** Change every `(` to `)` and every `)` to `(`.
3. Convert this altered expression into **postfix format**, but modify the stack popping criteria: only pop operators from the stack if the top operator has **strictly greater precedence** (`>`) than the current operator (drop the equality check).
4. **Reverse** the final postfix result string to get the final prefix expression.

### Python Code

```python
def infix_to_prefix(expression):
    # Step 1 & 2: Reverse the string and invert parenthesis
    reversed_expr = []
    for char in reversed(expression):
        if char == '(':
            reversed_expr.append(')')
        elif char == ')':
            reversed_expr.append('(')
        else:
            reversed_expr.append(char)

    # Step 3: Run Postfix Logic with STRICTLY greater condition (">")
    stack = []
    result = []
    for char in reversed_expr:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) > precedence(char):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    # Step 4: Reverse the final result
    result.reverse()
    return "".join(result)
```

**Time Complexity:** O(N)
**Space Complexity:** O(N)

### Worked Example: `A + B * C` → `+ A * B C`

| Step | Description | Expression |
|---|---|---|
| Original | Infix expression | `A + B * C` |
| Step 1 & 2 | Reverse the string, invert brackets (none here) | `C * B + A` |
| Step 3 | Convert to postfix using **strict `>`** rule | `C B * A +` |
| Step 4 | Reverse the Step 3 result | **`+ A * B C`** (final prefix) |

---

## 6. Postfix to Infix Conversion

### Logic & Rules
- Read the expression from **left to right**.
- When an **operand** is encountered, push it to the stack.
- When an **operator** is encountered, pop the top two elements:
  - First popped element = Operand 2 (`op2`)
  - Second popped element = Operand 1 (`op1`)
- Combine them into a single bracketed string containing the operator in the middle: `"(" + op1 + operator + op2 + ")"` and push it back to the stack.

### Python Code

```python
def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = f"({op1}{char}{op2})"
            stack.append(new_expr)
    return stack[-1]
```

**Time Complexity:** O(N)
**Space Complexity:** O(N)

### Worked Example: `A B + C *` → `((A+B)*C)`

| Step | Token | Action Taken | Stack (bottom → top) |
|---|---|---|---|
| 1 | A | Operand → push | A |
| 2 | B | Operand → push | A, B |
| 3 | + | Operator → op2=B, op1=A → build `(A+B)` → push | (A+B) |
| 4 | C | Operand → push | (A+B), C |
| 5 | * | Operator → op2=C, op1=(A+B) → build `((A+B)*C)` → push | ((A+B)*C) |
| End | - | Stack has 1 element → final infix result | **((A+B)*C)** |

---

## 7. Prefix to Infix Conversion

### Logic & Rules
- Read the expression from **right to left** (reverse order loop).
- When an **operand** is encountered, push it to the stack.
- When an **operator** is encountered, pop the top two elements:
  - First popped element = Operand 1 (`op1`)
  - Second popped element = Operand 2 (`op2`)
- Construct the string: `"(" + op1 + operator + op2 + ")"` and push it back to the stack.

> **Note:** The op1/op2 order is swapped compared to Postfix → Infix, because the scan direction is reversed.

### Python Code

```python
def prefix_to_infix(expression):
    stack = []
    # Reverse iteration without string slicing overhead
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"({op1}{char}{op2})"
            stack.append(new_expr)
    return stack[-1]
```

**Time Complexity:** O(N)
**Space Complexity:** O(N)

### Worked Example: `* + A B C` → `((A+B)*C)`
*(Scanned right to left, so tokens are read in order: C, B, A, +, *)*

| Step | Token | Action Taken | Stack (bottom → top) |
|---|---|---|---|
| 1 | C | Operand → push | C |
| 2 | B | Operand → push | C, B |
| 3 | A | Operand → push | C, B, A |
| 4 | + | Operator → op1=A, op2=B → build `(A+B)` → push | C, (A+B) |
| 5 | * | Operator → op1=(A+B), op2=C → build `((A+B)*C)` → push | ((A+B)*C) |
| End | - | Stack has 1 element → final infix result | **((A+B)*C)** |

---

## 8. Postfix to Prefix Conversion

### Logic & Rules
- Iterate from **left to right**.
- If it is an **operand**, push to stack.
- If it is an **operator**, pop two operands:
  - First pop = `op2`
  - Second pop = `op1`
- Combine them as: `operator + op1 + op2` (no brackets) and push it back to the stack.

### Python Code

```python
def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = f"{char}{op1}{op2}"
            stack.append(new_expr)
    return stack[-1]
```

**Time Complexity:** O(N)
**Space Complexity:** O(N)

### Worked Example: `A B + C *` → `* + A B C`

| Step | Token | Action Taken | Stack (bottom → top) |
|---|---|---|---|
| 1 | A | Operand → push | A |
| 2 | B | Operand → push | A, B |
| 3 | + | Operator → op2=B, op1=A → build `+AB` → push | +AB |
| 4 | C | Operand → push | +AB, C |
| 5 | * | Operator → op2=C, op1=+AB → build `*+ABC` → push | *+ABC |
| End | - | Stack has 1 element → final prefix result | **\*+ABC** |

---

## 9. Prefix to Postfix Conversion

### Logic & Rules
- Iterate from **right to left**.
- If it is an **operand**, push to stack.
- If it is an **operator**, pop two operands:
  - First pop = `op1`
  - Second pop = `op2`
- Combine them as: `op1 + op2 + operator` (no brackets) and push back to the stack.

### Python Code

```python
def prefix_to_postfix(expression):
    stack = []
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"{op1}{op2}{char}"
            stack.append(new_expr)
    return stack[-1]
```

**Time Complexity:** O(N)
**Space Complexity:** O(N)

### Worked Example: `* + A B C` → `A B + C *`
*(Scanned right to left, so tokens are read in order: C, B, A, +, *)*

| Step | Token | Action Taken | Stack (bottom → top) |
|---|---|---|---|
| 1 | C | Operand → push | C |
| 2 | B | Operand → push | C, B |
| 3 | A | Operand → push | C, B, A |
| 4 | + | Operator → op1=A, op2=B → build `AB+` → push | C, AB+ |
| 5 | * | Operator → op1=AB+, op2=C → build `AB+C*` → push | AB+C* |
| End | - | Stack has 1 element → final postfix result | **AB+C\*** |

---

## 10. Interview Insights & Full Recap

### Are these conversions directly asked in product interviews?
Generally, **no**. These parsing algorithms require significant memorization of structural rules rather than generalized runtime logical optimization.

### Why should we learn this then?
It is a crucial practical concept to thoroughly master and test your comfort level with tracking element ordering inside **stacks** — understanding LIFO behavior, knowing when to clear/discard values (e.g. dropping `(`), and matching pointers correctly during complex reverse iterations.

### Full Recap: All 6 Conversions

| Conversion | Scan Direction | Key Technique |
|---|---|---|
| Infix → Postfix | Left to Right | Operand → output. `(` → push. `)` → pop to output until `(`. Operator → pop while precedence(top) ≥ current, then push. |
| Infix → Prefix | Reverse + invert brackets, then Left to Right | Same as Infix→Postfix but pop only while precedence(top) > current (strict `>`). Finally reverse the resulting string. |
| Postfix → Infix | Left to Right | Operand → push. Operator → pop op2, pop op1, push `(` + op1 + OP + op2 + `)`. |
| Prefix → Infix | Right to Left | Operand → push. Operator → pop op1, pop op2 (order swapped!), push `(` + op1 + OP + op2 + `)`. |
| Postfix → Prefix | Left to Right | Operand → push. Operator → pop op2, pop op1, push OP + op1 + op2 (no brackets). |
| Prefix → Postfix | Right to Left | Operand → push. Operator → pop op1, pop op2, push op1 + op2 + OP (no brackets). |
