# 📒 Contact Book

A full-featured, interactive command-line Contact Book built with pure Python 3. Store, search, update, and delete contacts — all saved automatically to a local JSON file so your data is never lost between sessions.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Contact Fields](#contact-fields)
- [Example Session](#example-session)
- [Data Storage](#data-storage)
- [Project Structure](#project-structure)
- [Function Reference](#function-reference)
- [Error Handling](#error-handling)
- [License](#license)

---

## ✨ Features

- ➕ **Add contacts** with name, phone, email, and address
- 📋 **View all contacts** sorted alphabetically with a detail view
- 🔍 **Search** by name or phone number (partial match supported)
- ✏️ **Update** any field — leave blank to keep the current value
- 🗑️ **Delete** contacts with a confirmation prompt before removal
- 💾 **Auto-save** to `contacts.json` — data persists between sessions
- 🔢 **Auto-incrementing IDs** for each contact
- 📅 **Timestamps** — records when each contact was added
- ⚠️ **Duplicate phone detection** — warns if the number already exists
- ✅ **Input validation** — phone format and email format checked
- 🛡️ **Robust error handling** — re-prompts on all invalid input
- 📦 **Zero dependencies** — pure Python standard library only

---

## ✅ Requirements

- Python **3.6** or higher
- No third-party packages needed

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/contact-book.git
   cd contact-book
   ```

2. **Verify Python is installed:**

   ```bash
   python --version
   # or
   python3 --version
   ```

No `pip install` needed — the project uses only Python's built-in `json`, `os`, `re`, `sys`, and `datetime` modules.

---

## ▶️ Usage

Run the script from your terminal:

```bash
python contact_book.py
```

or on some systems:

```bash
python3 contact_book.py
```

A `contacts.json` file will be automatically created in the same directory to store your contacts permanently.

---

## 🗂️ Menu Options

```
════════════════════════════════════════════════════════
          📒  CONTACT BOOK  📒
════════════════════════════════════════════════════════

  ────────────────────────────────────────────────────────
  MENU
  ────────────────────────────────────────────────────────
  1.  ➕  Add new contact
  2.  📋  View all contacts
  3.  🔍  Search contacts
  4.  ✏️   Update a contact
  5.  🗑️   Delete a contact
  0.  🚪  Exit
  ────────────────────────────────────────────────────────
```

| Option | Action |
|:------:|--------|
| 1 | Add a new contact with all details |
| 2 | View all contacts sorted A–Z; enter an ID for full details |
| 3 | Search by name or phone number; enter an ID for full details |
| 4 | Update any field of an existing contact by ID |
| 5 | Delete a contact by ID (with confirmation) |
| 0 | Exit the program |

---

## 📇 Contact Fields

| Field | Required | Validation |
|-------|:--------:|-----------|
| Name | ✅ Yes | Non-empty string |
| Phone | ✅ Yes | Min. 7 digits; allows `+`, `-`, `()`, spaces |
| Email | ❌ Optional | Must follow `user@domain.tld` format |
| Address | ❌ Optional | Free-text string |
| ID | Auto | Auto-incremented integer |
| Added | Auto | Timestamp set at creation |

---

## 💻 Example Session

```
════════════════════════════════════════════════════════
          📒  CONTACT BOOK  📒
════════════════════════════════════════════════════════

  Welcome to your Contact Book!
  0 contact(s) loaded.

  ── ADD NEW CONTACT ──
  Name: Alice Johnson
  Phone (e.g. +91 98765 43210): +91 98765 43210
  Email (optional): alice@example.com
  Address (optional): 123 MG Road, Mumbai

  ✔  Contact 'Alice Johnson' added successfully! (ID: 1)

  ── ALL CONTACTS ──

  #      Name                       Phone
  ─────  ─────────────────────────  ───────────────
  1.     Alice Johnson              +91 98765 43210

  Total: 1 contact(s)

  Enter a contact ID for full details (or press Enter to go back): 1

  ──────────────────────────────────────────────────────
  ID     : 1
  Name   : Alice Johnson
  Phone  : +91 98765 43210
  Email  : alice@example.com
  Address: 123 MG Road, Mumbai
  Added  : 2026-05-30 14:35
  ──────────────────────────────────────────────────────

  ── SEARCH CONTACTS ──
  Search by name or phone number: alice

  Found 1 result(s) for 'alice':
  #1     Alice Johnson              +91 98765 43210

  ── DELETE CONTACT ──
  Enter the contact ID to delete: 1
  Are you sure you want to delete 'Alice Johnson'? (y/n): n
  Deletion cancelled.

  Goodbye! Your contacts are saved. 👋
```

---

## 💾 Data Storage

Contacts are saved automatically to `contacts.json` in the same directory as the script. The file is created on first use and updated after every add, update, or delete operation.

**Sample `contacts.json` structure:**

```json
{
  "1": {
    "name": "Alice Johnson",
    "phone": "+91 98765 43210",
    "email": "alice@example.com",
    "address": "123 MG Road, Mumbai",
    "created": "2026-05-30 14:35"
  },
  "2": {
    "name": "Bob Smith",
    "phone": "+1 555-234-5678",
    "email": "bob@gmail.com",
    "address": "456 Park Ave, New York",
    "created": "2026-05-30 14:36"
  }
}
```

---

## 📁 Project Structure

```
contact-book/
│
├── contact_book.py    ← Main script — all logic lives here
├── contacts.json      ← Auto-created data file (do not delete)
└── README.md          ← This file
```

---

## 🔧 Function Reference

| Function | Purpose |
|----------|---------|
| `load_contacts()` | Loads contacts from `contacts.json` on startup |
| `save_contacts()` | Writes the contacts dict to `contacts.json` |
| `next_id()` | Generates the next auto-increment contact ID |
| `validate_phone()` | Checks phone has at least 7 digits |
| `validate_email()` | Checks email matches `user@domain.tld` pattern |
| `prompt()` | Generic input prompt with optional validation |
| `confirm()` | Yes/no confirmation prompt |
| `clear()` | Clears the terminal screen (cross-platform) |
| `banner()` | Prints the app title banner |
| `print_menu()` | Displays the main menu |
| `format_contact()` | Returns a formatted contact card string |
| `print_contact_row()` | Prints a compact one-line contact summary |
| `add_contact()` | Collects input and adds a new contact |
| `view_all()` | Lists all contacts A–Z with optional detail view |
| `search_contacts()` | Searches contacts by name or phone |
| `update_contact()` | Updates any fields of an existing contact |
| `delete_contact()` | Deletes a contact after confirmation |
| `main()` | Entry point — loads data and runs the menu loop |

---

## 🛡️ Error Handling

| Scenario | Behaviour |
|----------|-----------|
| Empty required field | Warns and re-prompts |
| Invalid phone format | Warns and re-prompts |
| Invalid email format | Warns and re-prompts |
| Duplicate phone number | Warns and asks to confirm before adding |
| Contact ID not found | Prints a clear error message |
| Invalid menu choice | Warns and re-displays the menu |
| Corrupted `contacts.json` | Falls back to empty state gracefully |
| File write failure | Prints an error without crashing |
| Delete without confirmation | Cancels the operation safely |

---

## 📄 License

This project is open source and free to use under the [MIT License](LICENSE).

---

> Built with ❤️ using pure Python 3. Keep your contacts organised! 📒
> 
MADE BY Allen Stivanson Christian || Patent holder

MADE for CODESOFT :- https://www.linkedin.com/company/codsoft/posts/?feedView=all    

- 💼 LinkedIn: [https://in.linkedin.com/in/your-profile ](https://www.linkedin.com/in/allen-christian-708545409/) 
- 💻 GitHub: https://github.com/allen745  
-  portfolio  https://allen745.github.io
