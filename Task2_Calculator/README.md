# 🧮 Simple Python Calculator

A clean, interactive command-line calculator built in Python that supports six basic arithmetic operations. No external libraries required — pure Python 3.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Operations](#operations)
- [Example Session](#example-session)
- [Project Structure](#project-structure)
- [Error Handling](#error-handling)

---

## ✨ Features

- Six arithmetic operations: addition, subtraction, multiplication, division, modulus, and exponentiation
- Interactive menu-driven interface
- Continuous calculation loop — perform multiple calculations in one session
- Robust input validation — gracefully handles non-numeric input
- Division and modulus by zero protection
- Clean result formatting — whole numbers display as integers (e.g., `5.0` → `5`)

---

## ✅ Requirements

- Python 3.6 or higher
- No third-party packages needed

---

## ⚙️ Installation

1. **Clone or download** this repository:

   ```bash
   git clone https://github.com/your-username/simple-calculator.git
   cd simple-calculator
   ```

2. **Verify Python is installed:**

   ```bash
   python --version
   # or
   python3 --version
   ```

That's it — no `pip install` needed.

---

## ▶️ Usage

Run the script from your terminal:

```bash
python calculator.py
```

or on some systems:

```bash
python3 calculator.py
```

You will be greeted with a menu. Enter the number corresponding to your desired operation, then provide two numbers when prompted.

---

## ➕ Operations

| Choice | Symbol | Operation      | Example            |
|:------:|:------:|----------------|--------------------|
| 1      | `+`    | Addition       | 10 + 5 = **15**    |
| 2      | `-`    | Subtraction    | 10 − 3 = **7**     |
| 3      | `*`    | Multiplication | 4 × 6 = **24**     |
| 4      | `/`    | Division       | 20 ÷ 4 = **5**     |
| 5      | `%`    | Modulus        | 17 % 5 = **2**     |
| 6      | `**`   | Exponentiation | 3 ** 4 = **81**    |
| 0      | —      | Exit           | Quit the program   |

---

## 💻 Example Session

```
Welcome to the Simple Calculator!

========================================
         SIMPLE CALCULATOR
========================================
  1.  +    Addition
  2.  -    Subtraction
  3.  *    Multiplication
  4.  /    Division
  5.  %    Modulus
  6.  **   Exponentiation
  0.  Exit
========================================
  Choose an operation (0–6): 6

  [Exponentiation]
  Enter first number  : 3
  Enter second number : 4

  ✔  3 ** 4 = 81

  Perform another calculation? (y/n): y

========================================
  Choose an operation (0–6): 4

  [Division]
  Enter first number  : 10
  Enter second number : 0

  ✖  Error: Division by zero is not allowed.

  Perform another calculation? (y/n): n

  Goodbye! 👋
```

---

## 📁 Project Structure

```
simple-calculator/
│
├── calculator.py   # Main script — all logic lives here
└── README.md       # This file
```

**Inside `calculator.py`:**

| Function         | Purpose                                              |
|------------------|------------------------------------------------------|
| `add(a, b)`      | Returns `a + b`                                      |
| `subtract(a, b)` | Returns `a - b`                                      |
| `multiply(a, b)` | Returns `a * b`                                      |
| `divide(a, b)`   | Returns `a / b`; raises error if `b == 0`            |
| `modulus(a, b)`  | Returns `a % b`; raises error if `b == 0`            |
| `power(a, b)`    | Returns `a ** b`                                     |
| `get_number()`   | Validates and returns a float from user input        |
| `display_menu()` | Prints the operation menu                            |
| `format_result()`| Formats and prints the expression and result         |
| `main()`         | Main loop — drives the entire interactive session    |

---

## 🛡️ Error Handling

| Scenario                    | Behaviour                                              |
|-----------------------------|--------------------------------------------------------|
| Non-numeric input           | Prints a warning and re-prompts for a valid number     |
| Invalid menu choice         | Prints a warning and re-displays the menu              |
| Division by zero            | Raises `ValueError` with a descriptive message        |
| Modulus by zero             | Raises `ValueError` with a descriptive message        |

---

## 📄 License

This project is open source and free to use under the [MIT License](LICENSE).

---
## 🔗 Connect With Me

MADE BY Allen Stivanson Christian || Patent holder

MADE for CODESOFT :- https://www.linkedin.com/company/codsoft/posts/?feedView=all    

- 💼 LinkedIn: [https://in.linkedin.com/in/your-profile ](https://www.linkedin.com/in/allen-christian-708545409/) 
- 💻 GitHub: https://github.com/allen745  
-  portfolio  https://allen745.github.io

> Built with ❤️ using pure Python 3.
