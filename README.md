<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<h1 align="center">🐍 Bro Python</h1>

<p align="center">
  <b>A hands-on Python learning journey — from zero to building mini-projects.</b><br>
  Each topic lives in its own folder with working examples and exercises you can run instantly.
</p>

---

## 📑 Table of Contents

| # | Topic | Folder | What You'll Learn |
|---|-------|--------|-------------------|
| 1 | [Variables & Data Types](#1--variables--data-types) | `variables/` | Strings, integers, floats, booleans, f-strings |
| 2 | [User Input](#2--user-input) | `user_input/` | `input()`, type conversion on the fly, mini exercises |
| 3 | [Typecasting](#3--typecasting) | `typecasting/` | `str()`, `int()`, `float()`, `bool()`, `type()` |
| 4 | [Arithmetic Operators](#4--arithmetic-operators) | `Arithmetic Operators/` | Math ops, augmented assignment, `math` module |
| 5 | [If / Elif / Else](#5--if--elif--else) | `if_else/` | Conditional logic, comparison operators, input validation |
| 6 | [Calculator 🧮](#6--calculator-) | `calculator/` | A working CLI calculator combining all concepts |
| 7 | [Weight Converter ⚖️](#7--weight-converter-️) | `weight_convertor/` | Real-world unit conversion |
| 8 | [Mad Libs Game 🎲](#8--mad-libs-game-) | `madlibs game/` | Fun word game using string formatting |

---

## 📂 Repository Structure

```
Bro_Python/
│
├── variables/
│   └── main.py              # Variables, data types & f-strings
│
├── user_input/
│   └── main.py              # input(), area calculator, shopping cart
│
├── typecasting/
│   └── main.py              # Type conversion between str, int, float, bool
│
├── Arithmetic Operators/
│   ├── main.py              # Augmented assignment operators
│   ├── second.py            # Built-in math functions (round, abs, pow, max, min)
│   ├── mathematics.py       # math module (pi, e, sqrt, ceil, floor)
│   ├── exercise_1.py        # 🏋️ Circumference of a circle
│   ├── exercise_2.py        # 🏋️ Area of a circle
│   └── exercise_3.py        # 🏋️ Hypotenuse (Pythagorean theorem)
│
├── if_else/
│   ├── main.py              # if / elif / else basics
│   ├── exercise_1.py        # 🏋️ Y/N food prompt
│   ├── exercise_2.py        # 🏋️ Empty-name validation
│   └── exercise_3.py        # 🏋️ Boolean flag checks
│
├── calculator/
│   └── main.py              # CLI calculator (+ - * /)
│
├── weight_convertor/
│   └── main.py              # Kg ↔ Pounds converter
│
├── madlibs game/
│   └── main.py              # Fill-in-the-blank word game
│
├── .gitignore
├── requirements.txt
└── README.md                 # ← You are here
```

---

## 🧠 Concepts Covered

### 1 · Variables & Data Types

> **File:** `variables/main.py`

Learn the four fundamental data types and how to use **f-strings** for clean output.

```python
# String
first_name = "Bro"

# Integer
age = 25

# Float
price = 12.99

# Boolean
is_student = True

# f-string (formatted string)
print(f"Hello {first_name}, you are {age} years old!")
```

**Key Takeaways:**
- Variables act as containers for values
- Python is dynamically typed — no need to declare types explicitly
- f-strings (`f"..."`) make string interpolation readable and concise

---

### 2 · User Input

> **File:** `user_input/main.py`

Capture user input from the terminal and convert types inline.

```python
name = input("What is your name?: ")
age = int(input("How old are you?: "))   # cast to int on the fly

age = age + 1
print(f"Happy Birthday {name}! You are now {age} years old.")
```

**Exercises included:**
| # | Exercise | Concept |
|---|----------|---------|
| 1 | Rectangle area calculator | `float()` conversion, multiplication |
| 2 | Shopping cart total | Multiple inputs, formatted output |

---

### 3 · Typecasting

> **File:** `typecasting/main.py`

Convert between data types using built-in casting functions.

```python
gpa = 5.6
gpa = int(gpa)        # 5   (truncates decimal)

age = 25
age = float(age)      # 25.0

name = "Bro"
name = bool(name)     # True  (empty string → False)

print(type(gpa))      # <class 'int'>
```

**Key Takeaways:**
- `type()` reveals the data type of any variable
- `bool("")` → `False` — useful for checking empty input
- Be careful: `str(25) + "1"` → `"251"` (concatenation, not addition!)

---

### 4 · Arithmetic Operators

> **Files:** `Arithmetic Operators/main.py`, `second.py`, `mathematics.py`, `exercise_1-3.py`

#### Augmented Assignment Operators

```python
x = 10
x += 3    # x = x + 3  → 13
x -= 2    # x = x - 2  → 11
x *= 4    # x = x * 4  → 44
x /= 2    # x = x / 2  → 22.0
x **= 2   # x = x ** 2 → 484.0
x %= 3    # x = x % 3  → remainder
```

#### Built-in Math Functions

```python
round(3.14)       # 3
abs(-7)           # 7
pow(4, 3)         # 64  (4³)
max(3, 7, 2)      # 7
min(3, 7, 2)      # 2
```

#### The `math` Module

```python
import math

math.pi            # 3.141592653589793
math.e             # 2.718281828459045
math.sqrt(9)       # 3.0
math.ceil(9.1)     # 10
math.floor(9.1)    # 9
```

> ⚠️ **Pro Tip:** Never name your file `math.py` — it shadows the built-in `math` module!

**Exercises included:**
| # | Exercise | Formula |
|---|----------|---------|
| 1 | Circumference of a circle | `C = 2πr` |
| 2 | Area of a circle | `A = πr²` |
| 3 | Hypotenuse (Pythagorean theorem) | `c = √(a² + b²)` |

---

### 5 · If / Elif / Else

> **Files:** `if_else/main.py`, `exercise_1-3.py`

Control the flow of your program with conditional statements.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")
```

**Exercises included:**
| # | Exercise | Concept |
|---|----------|---------|
| 1 | Food prompt (Y/N) | String comparison with `==` |
| 2 | Name validation | Checking for empty strings |
| 3 | Boolean flag checks | `if is_online:` pattern |

> 💡 **Note:** Order of `elif` matters! Conditions are evaluated top-to-bottom and the first `True` wins.

---

### 6 · Calculator 🧮

> **File:** `calculator/main.py`

A fully working **command-line calculator** combining user input, typecasting, conditionals, and arithmetic.

```python
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
elif operator == "/":
    result = num1 / num2
# ... handles all four operators
```

---

### 7 · Weight Converter ⚖️

> **File:** `weight_convertor/main.py`

Convert between **Kilograms** and **Pounds** — a practical real-world mini-project.

```python
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (Kg or P): ")

if unit == "Kg":
    weight = weight * 2.205
    print(f"Your weight in Pounds is: {weight}")
```

---

### 8 · Mad Libs Game 🎲

> **File:** `madlibs game/main.py`

A fun **word game** where the user fills in blanks with adjectives, nouns, and verbs to create a hilarious story.

```python
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
```

---

## 🗺️ Learning Roadmap

```
✅ Variables & Data Types
✅ User Input
✅ Typecasting
✅ Arithmetic Operators & Math Module
✅ If / Elif / Else (Conditionals)
✅ Mini-Projects (Calculator, Weight Converter, Mad Libs)
⬜ Loops (for, while)
⬜ Lists, Tuples & Dictionaries
⬜ Functions
⬜ File Handling
⬜ Error Handling (try/except)
⬜ OOP (Classes & Objects)
⬜ Modules & Packages
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your system → [Download Python](https://www.python.org/downloads/)
- A terminal / command prompt
- A code editor (VS Code recommended)

### Setting Up a Virtual Environment

A virtual environment keeps your project dependencies isolated from your system Python. Here's how to set one up:

#### 1. Open your terminal and navigate to the project folder

```bash
cd path/to/Bro_Python
```

#### 2. Create a virtual environment

```bash
# On Linux / macOS
python3 -m venv venv

# On Windows
python -m venv venv
```

This creates a `venv/` folder inside your project directory.

#### 3. Activate the virtual environment

```bash
# On Linux / macOS
source venv/bin/activate

# On Windows (Command Prompt)
venv\Scripts\activate

# On Windows (PowerShell)
venv\Scripts\Activate.ps1
```

Once activated, you'll see `(venv)` at the beginning of your terminal prompt.

#### 4. Install dependencies (if any)

```bash
pip install -r requirements.txt
```

#### 5. Run any Python file

```bash
# Example: Run the calculator
python calculator/main.py

# Example: Run the Mad Libs game
python "madlibs game/main.py"

# Example: Run the variables lesson
python variables/main.py
```

> 💡 **Tip:** Use quotes around folder names that contain spaces, like `"madlibs game/main.py"`.

#### 6. Deactivate the virtual environment when you're done

```bash
deactivate
```

---

## 🤝 Contributing

This is a personal learning repository, but feel free to:
- ⭐ Star the repo if you find it helpful
- 🍴 Fork it to continue the roadmap on your own
- 💬 Open an issue if you spot any bugs or want to suggest improvements

---

<p align="center">
  <b>Made with ❤️ while learning Python</b><br>
  <i>Happy Coding! 🚀</i>
</p>
