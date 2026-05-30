"""
Contact Book
A full-featured CLI contact manager with JSON persistence.
Supports: Add, View, Search, Update, Delete contacts.
Pure Python 3 — no external libraries required.
"""

import json
import os
import re
import sys
from datetime import datetime


# ── Storage ───────────────────────────────────────────────────────────────────
DATA_FILE = "contacts.json"


def load_contacts():
    """Load contacts from the JSON file. Returns a dict keyed by contact ID."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("  ⚠  Could not read contacts file. Starting fresh.")
        return {}


def save_contacts(contacts):
    """Persist contacts dict to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"  ✖  Failed to save contacts: {e}")


def next_id(contacts):
    """Generate the next integer contact ID as a string."""
    if not contacts:
        return "1"
    return str(max(int(k) for k in contacts.keys()) + 1)


# ── Validation ────────────────────────────────────────────────────────────────
def validate_phone(phone):
    """Accept digits, spaces, +, -, (), dots. Min 7 digits."""
    digits = re.sub(r"\D", "", phone)
    return len(digits) >= 7


def validate_email(email):
    """Basic email format check."""
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))


# ── Input helpers ─────────────────────────────────────────────────────────────
def prompt(label, required=True, validator=None, hint=""):
    """
    Prompt for a value, optionally validating it.
    If not required, pressing Enter returns an empty string.
    """
    hint_str = f"  ({hint})" if hint else ""
    while True:
        val = input(f"  {label}{hint_str}: ").strip()
        if not val:
            if required:
                print(f"  ⚠  {label} is required.\n")
                continue
            return ""
        if validator and not validator(val):
            print(f"  ⚠  Invalid {label.lower()}. Please try again.\n")
            continue
        return val


def confirm(question):
    """Ask a yes/no question. Returns True for yes."""
    while True:
        ans = input(f"  {question} (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("  ⚠  Please enter y or n.")


# ── Display ───────────────────────────────────────────────────────────────────
DIVIDER  = "═" * 56
THIN_DIV = "─" * 56

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(f"\n{DIVIDER}")
    print("          📒  CONTACT BOOK  📒")
    print(DIVIDER)


def print_menu():
    print(f"\n  {THIN_DIV}")
    print("  MENU")
    print(f"  {THIN_DIV}")
    print("  1.  ➕  Add new contact")
    print("  2.  📋  View all contacts")
    print("  3.  🔍  Search contacts")
    print("  4.  ✏️   Update a contact")
    print("  5.  🗑️   Delete a contact")
    print("  0.  🚪  Exit")
    print(f"  {THIN_DIV}")


def format_contact(cid, c, detail=False):
    """Return a formatted string for a contact."""
    lines = [
        f"\n  {'─'*54}",
        f"  ID     : {cid}",
        f"  Name   : {c['name']}",
        f"  Phone  : {c['phone']}",
    ]
    if detail:
        lines.append(f"  Email  : {c['email'] or '—'}")
        lines.append(f"  Address: {c['address'] or '—'}")
        lines.append(f"  Added  : {c.get('created', '—')}")
    lines.append(f"  {'─'*54}")
    return "\n".join(lines)


def print_contact_row(cid, c, index=None):
    """Print a compact single-line contact summary."""
    idx = f"{index}." if index is not None else f"#{cid}"
    print(f"  {idx:<5}  {c['name']:<25}  {c['phone']}")


# ── Core operations ───────────────────────────────────────────────────────────
def add_contact(contacts):
    print(f"\n  {'─'*54}")
    print("  ➕  ADD NEW CONTACT")
    print(f"  {'─'*54}")

    name    = prompt("Name")
    phone   = prompt("Phone", validator=validate_phone,
                     hint="e.g. +91 98765 43210")
    email   = prompt("Email (optional)", required=False,
                     validator=validate_email, hint="e.g. john@example.com")
    address = prompt("Address (optional)", required=False)

    # Check for duplicate phone
    for cid, c in contacts.items():
        if c["phone"] == phone:
            print(f"\n  ⚠  A contact with phone {phone} already exists: {c['name']}")
            if not confirm("Add anyway?"):
                print("  Contact not added.")
                return

    cid = next_id(contacts)
    contacts[cid] = {
        "name":    name,
        "phone":   phone,
        "email":   email,
        "address": address,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    save_contacts(contacts)
    print(f"\n  ✔  Contact '{name}' added successfully! (ID: {cid})")


def view_all(contacts):
    print(f"\n  {'─'*54}")
    print("  📋  ALL CONTACTS")
    print(f"  {'─'*54}")

    if not contacts:
        print("  No contacts saved yet. Add some with option 1!")
        return

    sorted_contacts = sorted(contacts.items(), key=lambda x: x[1]["name"].lower())

    print(f"\n  {'#':<5}  {'Name':<25}  Phone")
    print(f"  {'─'*5}  {'─'*25}  {'─'*15}")
    for i, (cid, c) in enumerate(sorted_contacts, 1):
        print_contact_row(cid, c, index=i)

    print(f"\n  Total: {len(contacts)} contact(s)")

    # Offer detail view
    print()
    choice = input("  Enter a contact ID for full details (or press Enter to go back): ").strip()
    if choice in contacts:
        print(format_contact(choice, contacts[choice], detail=True))
    elif choice:
        print("  ⚠  Contact ID not found.")


def search_contacts(contacts):
    print(f"\n  {'─'*54}")
    print("  🔍  SEARCH CONTACTS")
    print(f"  {'─'*54}")

    if not contacts:
        print("  No contacts to search.")
        return

    query = input("\n  Search by name or phone number: ").strip().lower()
    if not query:
        print("  ⚠  Please enter a search term.")
        return

    results = {
        cid: c for cid, c in contacts.items()
        if query in c["name"].lower() or query in c["phone"].lower()
    }

    if not results:
        print(f"\n  No contacts found matching '{query}'.")
        return

    print(f"\n  Found {len(results)} result(s) for '{query}':\n")
    print(f"  {'ID':<5}  {'Name':<25}  Phone")
    print(f"  {'─'*5}  {'─'*25}  {'─'*15}")
    for cid, c in sorted(results.items(), key=lambda x: x[1]["name"].lower()):
        print_contact_row(cid, c)

    # Offer detail view
    print()
    choice = input("  Enter a contact ID for full details (or press Enter to go back): ").strip()
    if choice in results:
        print(format_contact(choice, results[choice], detail=True))
    elif choice:
        print("  ⚠  Contact ID not found in results.")


def update_contact(contacts):
    print(f"\n  {'─'*54}")
    print("  ✏️   UPDATE CONTACT")
    print(f"  {'─'*54}")

    if not contacts:
        print("  No contacts to update.")
        return

    cid = input("\n  Enter the contact ID to update: ").strip()
    if cid not in contacts:
        print("  ⚠  Contact not found.")
        return

    c = contacts[cid]
    print(format_contact(cid, c, detail=True))
    print("\n  Leave a field blank to keep the current value.\n")

    new_name = input(f"  Name [{c['name']}]: ").strip()
    new_phone_raw = input(f"  Phone [{c['phone']}]: ").strip()
    new_email_raw = input(f"  Email [{c['email'] or '—'}]: ").strip()
    new_address_raw = input(f"  Address [{c['address'] or '—'}]: ").strip()

    # Validate only if a new value was entered
    if new_phone_raw and not validate_phone(new_phone_raw):
        print("  ⚠  Invalid phone number. Update cancelled.")
        return
    if new_email_raw and not validate_email(new_email_raw):
        print("  ⚠  Invalid email address. Update cancelled.")
        return

    # Apply changes
    if new_name:         c["name"]    = new_name
    if new_phone_raw:    c["phone"]   = new_phone_raw
    if new_email_raw:    c["email"]   = new_email_raw
    if new_address_raw:  c["address"] = new_address_raw

    contacts[cid] = c
    save_contacts(contacts)
    print(f"\n  ✔  Contact '{c['name']}' updated successfully!")


def delete_contact(contacts):
    print(f"\n  {'─'*54}")
    print("  🗑️   DELETE CONTACT")
    print(f"  {'─'*54}")

    if not contacts:
        print("  No contacts to delete.")
        return

    cid = input("\n  Enter the contact ID to delete: ").strip()
    if cid not in contacts:
        print("  ⚠  Contact not found.")
        return

    c = contacts[cid]
    print(format_contact(cid, c, detail=True))

    if confirm(f"  Are you sure you want to delete '{c['name']}'?"):
        del contacts[cid]
        save_contacts(contacts)
        print(f"\n  ✔  Contact '{c['name']}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


# ── Main loop ─────────────────────────────────────────────────────────────────
def main():
    contacts = load_contacts()
    clear()
    banner()
    print(f"\n  Welcome to your Contact Book!")
    print(f"  {len(contacts)} contact(s) loaded.\n")

    while True:
        print_menu()
        choice = input("  Choose an option (0–5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_all(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "0":
            print(f"\n  Goodbye! Your contacts are saved. 👋\n")
            sys.exit(0)
        else:
            print("  ⚠  Invalid option. Please choose 0–5.")


if __name__ == "__main__":
    main()
