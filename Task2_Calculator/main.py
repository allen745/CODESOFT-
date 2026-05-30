"""
Simple Calculator — Basic Arithmetic Operations
Supports: Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation
"""

def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
def modulus(a, b):
    if b == 0:
        raise ValueError("Modulus by zero is not allowed.")
    return a % b
def power(a, b):      return a ** b


OPERATIONS = {
    "1": ("+",  "Addition",        add),
    "2": ("-",  "Subtraction",     subtract),
    "3": ("*",  "Multiplication",  multiply),
    "4": ("/",  "Division",        divide),
    "5": ("%",  "Modulus",         modulus),
    "6": ("**", "Exponentiation",  power),
}


def get_number(prompt):
    """Prompt the user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric value.\n")


def display_menu():
    print("\n" + "=" * 40)
    print("         SIMPLE CALCULATOR")
    print("=" * 40)
    for key, (symbol, name, _) in OPERATIONS.items():
        print(f"  {key}.  {symbol:<3}  {name}")
    print("  0.  Exit")
    print("=" * 40)


def format_result(a, symbol, b, result):
    """Pretty-print the expression and result."""
    # Use int display when the value is a whole number
    def fmt(n):
        return int(n) if isinstance(n, float) and n.is_integer() else n

    print(f"\n  ✔  {fmt(a)} {symbol} {fmt(b)} = {fmt(result)}\n")


def main():
    print("\nWelcome to the Simple Calculator!")

    while True:
        display_menu()

        choice = input("  Choose an operation (0–6): ").strip()

        if choice == "0":
            print("\n  Goodbye! 👋\n")
            break

        if choice not in OPERATIONS:
            print("  ⚠  Invalid choice. Please select a number from 0 to 6.")
            continue

        symbol, name, func = OPERATIONS[choice]

        print(f"\n  [{name}]")
        a = get_number("  Enter first number  : ")
        b = get_number("  Enter second number : ")

        try:
            result = func(a, b)
            format_result(a, symbol, b, result)
        except ValueError as e:
            print(f"\n  ✖  Error: {e}\n")

        again = input("  Perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Goodbye! 👋\n")
            break


if __name__ == "__main__":
    main()
