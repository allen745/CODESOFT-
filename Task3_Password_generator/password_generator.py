"""
Password Generator
Generates strong, random passwords based on user-specified length and complexity.
No external libraries required — pure Python 3.
"""

import random
import string
import re


# ── Character pools ──────────────────────────────────────────────────────────
LOWERCASE  = string.ascii_lowercase          # a-z
UPPERCASE  = string.ascii_uppercase          # A-Z
DIGITS     = string.digits                   # 0-9
SYMBOLS    = "!@#$%^&*()-_=+[]{}|;:,.<>?"   # special characters

# Ambiguous characters that are easy to confuse visually
AMBIGUOUS  = "0O1lI"


# ── Helpers ───────────────────────────────────────────────────────────────────
def build_charset(use_upper, use_digits, use_symbols, exclude_ambiguous):
    """Assemble the character pool from the user's complexity choices."""
    pool = LOWERCASE
    if use_upper:
        pool += UPPERCASE
    if use_digits:
        pool += DIGITS
    if use_symbols:
        pool += SYMBOLS
    if exclude_ambiguous:
        pool = "".join(c for c in pool if c not in AMBIGUOUS)
    return pool


def generate_password(length, use_upper, use_digits, use_symbols,
                      exclude_ambiguous):
    """
    Generate a password that:
      - Uses only characters from the selected pool
      - Guarantees at least one character from each enabled category
    """
    pool = build_charset(use_upper, use_digits, use_symbols, exclude_ambiguous)

    if len(pool) < 2:
        raise ValueError("Character pool is too small. Enable more character types.")

    # Build mandatory characters so every enabled type is represented
    mandatory = [random.choice(LOWERCASE)]
    if use_upper:
        src = "".join(c for c in UPPERCASE if c not in (AMBIGUOUS if exclude_ambiguous else ""))
        if src:
            mandatory.append(random.choice(src))
    if use_digits:
        src = "".join(c for c in DIGITS if c not in (AMBIGUOUS if exclude_ambiguous else ""))
        if src:
            mandatory.append(random.choice(src))
    if use_symbols:
        mandatory.append(random.choice(SYMBOLS))

    # Fill the rest with random characters from the full pool
    remaining = length - len(mandatory)
    if remaining < 0:
        remaining = 0
    filler = [random.choice(pool) for _ in range(remaining)]

    # Combine and shuffle to avoid predictable positions
    password_chars = mandatory + filler
    random.shuffle(password_chars)

    # If length was less than mandatory count, just return shuffled mandatory
    return "".join(password_chars[:length])


def password_strength(password, use_upper, use_digits, use_symbols):
    """
    Return a (score 0–5, label, bar) tuple for a simple strength assessment.
    """
    score = 0
    length = len(password)

    if length >= 8:   score += 1
    if length >= 12:  score += 1
    if length >= 16:  score += 1
    if use_upper and re.search(r"[A-Z]", password):   score += 1
    if use_digits and re.search(r"\d", password):      score += 0.5
    if use_symbols and re.search(r"[^a-zA-Z0-9]", password): score += 0.5

    score = min(int(score), 5)

    labels = {0: "Very Weak", 1: "Weak", 2: "Fair", 3: "Good",
              4: "Strong", 5: "Very Strong"}
    bars   = {0: "█░░░░", 1: "██░░░", 2: "███░░", 3: "████░", 4: "█████",
              5: "█████"}
    return score, labels[score], bars[score]


def ask_yes_no(prompt, default="y"):
    """Ask a yes/no question; return True for yes, False for no."""
    hint = " [Y/n]" if default == "y" else " [y/N]"
    while True:
        answer = input(prompt + hint + ": ").strip().lower()
        if answer == "":
            return default == "y"
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  ⚠  Please enter y or n.\n")


def get_length():
    """Prompt until the user enters a valid integer length (4–128)."""
    while True:
        raw = input("  Desired password length (4–128): ").strip()
        try:
            length = int(raw)
            if 4 <= length <= 128:
                return length
            print("  ⚠  Please enter a number between 4 and 128.\n")
        except ValueError:
            print("  ⚠  Invalid input. Enter a whole number.\n")


def get_count():
    """Prompt until the user enters a valid count (1–20)."""
    while True:
        raw = input("  How many passwords to generate? (1–20): ").strip()
        try:
            count = int(raw)
            if 1 <= count <= 20:
                return count
            print("  ⚠  Please enter a number between 1 and 20.\n")
        except ValueError:
            print("  ⚠  Invalid input. Enter a whole number.\n")


# ── Display ───────────────────────────────────────────────────────────────────
def display_header():
    print("\n" + "═" * 50)
    print("          🔐  PASSWORD GENERATOR  🔐")
    print("═" * 50)


def display_passwords(passwords, use_upper, use_digits, use_symbols):
    print("\n" + "─" * 50)
    if len(passwords) == 1:
        pw = passwords[0]
        score, label, bar = password_strength(pw, use_upper, use_digits, use_symbols)
        print(f"  Generated Password:\n")
        print(f"  ➤  {pw}\n")
        print(f"  Strength : {bar}  {label}")
    else:
        print(f"  Generated Passwords:\n")
        for i, pw in enumerate(passwords, 1):
            score, label, bar = password_strength(pw, use_upper, use_digits, use_symbols)
            print(f"  {i:>2}.  {pw}")
            print(f"        {bar}  {label}\n")
    print("─" * 50)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    display_header()

    while True:
        print("\n  ── Configuration ──────────────────────────")

        length = get_length()
        count  = get_count()

        print()
        use_upper         = ask_yes_no("  Include uppercase letters (A–Z)?")
        use_digits        = ask_yes_no("  Include digits (0–9)?")
        use_symbols       = ask_yes_no("  Include symbols (!@#$…)?")
        exclude_ambiguous = ask_yes_no("  Exclude ambiguous characters (0/O, 1/l/I)?",
                                       default="n")

        print()

        # Validate that the pool is not empty
        pool = build_charset(use_upper, use_digits, use_symbols, exclude_ambiguous)
        if not pool:
            print("  ✖  No characters available with these settings. "
                  "Please enable at least one character type.\n")
            continue

        # Generate the requested passwords
        try:
            passwords = [
                generate_password(length, use_upper, use_digits,
                                  use_symbols, exclude_ambiguous)
                for _ in range(count)
            ]
        except ValueError as e:
            print(f"  ✖  Error: {e}\n")
            continue

        display_passwords(passwords, use_upper, use_digits, use_symbols)

        print()
        again = ask_yes_no("  Generate more passwords?", default="y")
        if not again:
            print("\n  Stay secure! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()
