# 🔐 Password Generator

A simple yet powerful command-line password generator built with pure Python 3. Instantly create strong, random passwords with full control over length, complexity, and character types — no installs required.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration Options](#configuration-options)
- [Strength Meter](#strength-meter)
- [Example Session](#example-session)
- [Project Structure](#project-structure)
- [Function Reference](#function-reference)
- [Error Handling](#error-handling)
- [License](#license)

---

## ✨ Features

- 🔡 Choose password **length** from 4 to 128 characters
- 🔢 Generate **1 to 20 passwords** in a single run
- 🔠 Toggle **uppercase**, **digits**, and **symbols** independently
- 🚫 Optionally **exclude ambiguous characters** (`0/O`, `1/l/I`) to avoid visual confusion
- ✅ **Guaranteed coverage** — at least one character from every enabled category
- 📊 Built-in **strength meter** with a 5-level visual bar
- ♻️ **Loop-friendly** — generate more without restarting the program
- 🛡️ Robust **input validation** on all prompts
- 📦 **Zero dependencies** — uses Python standard library only

---

## ✅ Requirements

- Python **3.6** or higher
- No third-party packages needed

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```

2. **Verify Python is installed:**

   ```bash
   python --version
   # or
   python3 --version
   ```

No `pip install` needed — the project uses only Python's built-in `random`, `string`, and `re` modules.

---

## ▶️ Usage

Run the script from your terminal:

```bash
python password_generator.py
```

or on some systems:

```bash
python3 password_generator.py
```

Follow the interactive prompts to configure and generate your password(s).

---

## ⚙️ Configuration Options

At each run you will be asked:

| Prompt | Input | Default |
|--------|-------|---------|
| Password length | Integer, 4–128 | — |
| Number of passwords | Integer, 1–20 | — |
| Include uppercase (A–Z) | y / n | Yes |
| Include digits (0–9) | y / n | Yes |
| Include symbols (!@#$…) | y / n | Yes |
| Exclude ambiguous chars | y / n | No |

**Character pools used:**

| Type | Characters |
|------|-----------|
| Lowercase | `a–z` |
| Uppercase | `A–Z` |
| Digits | `0–9` |
| Symbols | `!@#$%^&*()-_=+[]{}|;:,.<>?` |
| Ambiguous (excluded optionally) | `0 O 1 l I` |

---

## 📊 Strength Meter

Every generated password is scored on a **0–5 scale** and shown with a visual bar:

| Bar | Label | Criteria |
|-----|-------|---------|
| `█░░░░` | Very Weak | Length < 8 |
| `██░░░` | Weak | Length ≥ 8 |
| `███░░` | Fair | Length ≥ 12 |
| `████░` | Good | Length ≥ 16 |
| `█████` | Strong | Length ≥ 16 + uppercase |
| `█████` | Very Strong | Length ≥ 16 + uppercase + digits/symbols |

---

## 💻 Example Session

```
══════════════════════════════════════════════════
          🔐  PASSWORD GENERATOR  🔐
══════════════════════════════════════════════════

  ── Configuration ──────────────────────────
  Desired password length (4–128): 16
  How many passwords to generate? (1–20): 1

  Include uppercase letters (A–Z)? [Y/n]: y
  Include digits (0–9)? [Y/n]: y
  Include symbols (!@#$…)? [Y/n]: y
  Exclude ambiguous characters (0/O, 1/l/I)? [y/N]: n

──────────────────────────────────────────────────
  Generated Password:

  ➤  _bP99wZ<P-_Me=K?

  Strength : █████  Very Strong
──────────────────────────────────────────────────

  Generate more passwords? [Y/n]: y

  ── Configuration ──────────────────────────
  Desired password length (4–128): 12
  How many passwords to generate? (1–20): 3

  Include uppercase letters (A–Z)? [Y/n]: y
  Include digits (0–9)? [Y/n]: y
  Include symbols (!@#$…)? [Y/n]: n
  Exclude ambiguous characters (0/O, 1/l/I)? [y/N]: y

──────────────────────────────────────────────────
  Generated Passwords:

   1.  B65P9vqRmkSn
        ████░  Good

   2.  m2aVJkkStnPr
        ████░  Good

   3.  T7gNwkZ4xmPq
        ████░  Good

──────────────────────────────────────────────────

  Generate more passwords? [Y/n]: n

  Stay secure! Goodbye. 👋
```

---

## 📁 Project Structure

```
password-generator/
│
├── password_generator.py   ← Main script — all logic lives here
└── README.md               ← This file
```

---

## 🔧 Function Reference

| Function | Purpose |
|----------|---------|
| `build_charset()` | Assembles the character pool from selected options |
| `generate_password()` | Generates a single password with guaranteed category coverage |
| `password_strength()` | Scores a password and returns a label + visual bar |
| `ask_yes_no()` | Prompts for a yes/no answer with a default fallback |
| `get_length()` | Validates and returns a password length (4–128) |
| `get_count()` | Validates and returns a password count (1–20) |
| `display_header()` | Prints the app banner |
| `display_passwords()` | Prints passwords with strength indicators |
| `main()` | Entry point — drives the interactive loop |

---

## 🛡️ Error Handling

| Scenario | Behaviour |
|----------|-----------|
| Non-numeric length input | Warns and re-prompts |
| Length out of range (< 4 or > 128) | Warns and re-prompts |
| Non-numeric count input | Warns and re-prompts |
| Count out of range (< 1 or > 20) | Warns and re-prompts |
| Invalid yes/no input | Warns and re-prompts |
| All character types disabled | Warns and returns to configuration |
| Character pool too small | Raises descriptive `ValueError` |




---

## 📄 License

This project is open source and free to use under the [MIT License](LICENSE).

---

> Built with ❤️ using pure Python 3. Stay safe, stay secure. 🔐
