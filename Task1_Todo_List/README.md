# ✅ To-Do List Application

A full-featured, interactive command-line To-Do List manager built with pure Python 3. Create, update, complete, and delete tasks with priorities, due dates, categories, and progress tracking — all saved automatically to a local JSON file.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Task Fields](#task-fields)
- [Priority Levels](#priority-levels)
- [Search & Filter Options](#search--filter-options)
- [Example Session](#example-session)
- [Data Storage](#data-storage)
- [Project Structure](#project-structure)
- [Function Reference](#function-reference)
- [Error Handling](#error-handling)
- [License](#license)

---

## ✨ Features

- ➕ **Add tasks** with title, priority, category, due date, and notes
- 📋 **View all tasks** sorted by priority and due date with a detail view
- 🔍 **Search & Filter** by keyword, priority, category, status, or overdue
- ✏️ **Update** any field of an existing task — blank = keep current value
- ✅ **Mark tasks complete** with a dedicated completion menu
- 🗑️ **Delete tasks** with a confirmation prompt before removal
- 📊 **Summary & Statistics** with progress bar, completion rate, and category breakdown
- ‼️ **Overdue detection** — tasks past their due date are flagged automatically
- 💾 **Auto-save** to `todo_list.json` — data persists between sessions
- 📅 **Timestamps** — created and last updated time recorded for every task
- 🔢 **Auto-incrementing IDs** for each task
- 🛡️ **Robust input validation** — re-prompts on all invalid entries
- 📦 **Zero dependencies** — pure Python standard library only

---

## ✅ Requirements

- Python **3.6** or higher
- No third-party packages needed

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/todo-list.git
   cd todo-list
   ```

2. **Verify Python is installed:**

   ```bash
   python --version
   # or
   python3 --version
   ```

No `pip install` needed — uses only Python's built-in `json`, `os`, `sys`, and `datetime` modules.

---

## ▶️ Usage

Run the script from your terminal:

```bash
python todo_list.py
```

or on some systems:

```bash
python3 todo_list.py
```

A `todo_list.json` file will be automatically created in the same directory to store your tasks permanently.

---

## 🗂️ Menu Options

```
══════════════════════════════════════════════════════════
          ✅  TO-DO LIST APPLICATION  ✅
══════════════════════════════════════════════════════════

  ──────────────────────────────────────────────────────
  MAIN MENU
  ──────────────────────────────────────────────────────
  1.  ➕  Add new task
  2.  📋  View all tasks
  3.  🔍  Search / Filter tasks
  4.  ✏️   Update a task
  5.  ✅  Mark task as complete
  6.  🗑️   Delete a task
  7.  📊  View summary / stats
  0.  🚪  Exit
  ──────────────────────────────────────────────────────
```

| Option | Action |
|:------:|--------|
| 1 | Add a new task with full details |
| 2 | View all tasks sorted by priority and due date |
| 3 | Search by keyword, filter by priority / category / status / overdue |
| 4 | Update any field of an existing task by ID |
| 5 | Mark a pending task as complete |
| 6 | Delete a task by ID (with confirmation) |
| 7 | View statistics — totals, progress bar, category breakdown |
| 0 | Exit the program |

---

## 📝 Task Fields

| Field | Required | Details |
|-------|:--------:|---------|
| Title | ✅ Yes | Short description of the task |
| Priority | ✅ Yes | 🔴 High / 🟡 Medium / 🟢 Low |
| Category | ❌ Optional | e.g. Work, Personal, Study |
| Due Date | ❌ Optional | Format: `YYYY-MM-DD` |
| Notes | ❌ Optional | Additional details or description |
| ID | Auto | Auto-incremented integer |
| Status | Auto | ⏳ Pending → ✅ Done |
| Created | Auto | Timestamp set at creation |
| Updated | Auto | Timestamp updated on every edit |

---

## 🎯 Priority Levels

| Input | Label | Meaning |
|:-----:|-------|---------|
| `1` or `high` | 🔴 High | Urgent — must do soon |
| `2` or `medium` | 🟡 Medium | Important but not urgent |
| `3` or `low` | 🟢 Low | Nice to do when time allows |

---

## 🔍 Search & Filter Options

| Filter | How it works |
|--------|-------------|
| 🔎 Keyword | Searches task title and notes (partial match) |
| 🔴 Priority | Shows all tasks of a selected priority level |
| 📁 Category | Filters by exact category name |
| ✅ Status | Shows only `pending` or `done` tasks |
| 📅 Overdue | Lists all pending tasks past their due date |

---

## 💻 Example Session

```
══════════════════════════════════════════════════════════
          ✅  TO-DO LIST APPLICATION  ✅
══════════════════════════════════════════════════════════

  Welcome to your To-Do List! 📋
  3 task(s) loaded  |  ✅ 1 done  |  ⏳ 2 pending

  ── ADD NEW TASK ──
  Task title: Finish Python project
  Priority (1/2/3): 1
  Category: Work
  Due date (YYYY-MM-DD): 2026-06-10
  Notes: Complete the to-do list app

  ✔  Task 'Finish Python project' added successfully! (ID: 1)

  ── ALL TASKS ──

  #     St  Title                        Priority     Due Date
  ───── ─── ──────────────────────────── ──────────── ──────────
  1.    ⏳  Finish Python project        🔴 High      📅 2026-06-10  [Work]
  2.    ⏳  Buy groceries                🟢 Low       📅 2026-06-05  [Personal]
  3.    ✅  Read a book                  🟡 Medium    📅 2026-06-20

  Total: 3  |  ✅ Done: 1  |  ⏳ Pending: 2

  ── SUMMARY & STATISTICS ──

  📌 Total tasks     : 3
  ✅ Completed       : 1  (33.3%)
  ⏳ Pending         : 2
  ‼️  Overdue         : 0

  Pending by Priority:
    🔴 High          : 1
    🟡 Medium        : 0
    🟢 Low           : 1

  Tasks by Category:
    📁 Work                 1 task(s)
    📁 Personal             1 task(s)
    📁 Uncategorized        1 task(s)

  Progress: [██████████░░░░░░░░░░░░░░░░░░░░] 33.3%

  Goodbye! Stay productive! 👋
```

---

## 💾 Data Storage

Tasks are saved automatically to `todo_list.json` in the same directory as the script. The file is created on first use and updated after every add, update, complete, or delete operation.

**Sample `todo_list.json` structure:**

```json
{
  "1": {
    "title": "Finish Python project",
    "status": "⏳ Pending",
    "priority": "🔴 High",
    "category": "Work",
    "due_date": "2026-06-10",
    "notes": "Complete the to-do list app",
    "created": "2026-05-31 10:00",
    "updated": ""
  },
  "2": {
    "title": "Buy groceries",
    "status": "✅ Done",
    "priority": "🟢 Low",
    "category": "Personal",
    "due_date": "2026-06-05",
    "notes": "Milk, eggs, bread",
    "created": "2026-05-31 10:05",
    "updated": "2026-05-31 11:30"
  }
}
```

---

## 📁 Project Structure

```
todo-list/
│
├── todo_list.py      ← Main script — all logic lives here
├── todo_list.json    ← Auto-created data file (do not delete)
└── README.md         ← This file
```

---

## 🔧 Function Reference

| Function | Purpose |
|----------|---------|
| `load_tasks()` | Loads tasks from `todo_list.json` on startup |
| `save_tasks()` | Writes tasks dict to `todo_list.json` |
| `next_id()` | Generates the next auto-increment task ID |
| `is_overdue()` | Checks if a pending task is past its due date |
| `validate_date()` | Validates YYYY-MM-DD date format |
| `get_priority_label()` | Converts user input to a priority emoji label |
| `prompt()` | Generic input prompt with optional default value |
| `confirm()` | Yes/no confirmation prompt |
| `clear()` | Clears the terminal screen (cross-platform) |
| `banner()` | Prints the app title banner |
| `print_menu()` | Displays the main menu |
| `status_icon()` | Returns ✅, ⏳, or 🔴 icon based on task state |
| `print_task_row()` | Prints a compact one-line task summary |
| `format_task_detail()` | Returns a full formatted task card |
| `sort_tasks()` | Sorts tasks: pending first, then by priority and due date |
| `add_task()` | Collects input and adds a new task |
| `view_all()` | Lists all (or filtered) tasks with optional detail view |
| `search_filter()` | Presents 5 filter options and displays matching tasks |
| `update_task()` | Updates any fields of an existing task |
| `mark_complete()` | Lists pending tasks and marks the chosen one as done |
| `delete_task()` | Deletes a task after confirmation |
| `view_summary()` | Displays statistics, category breakdown, and progress bar |
| `main()` | Entry point — loads data and drives the menu loop |

---

## 🛡️ Error Handling

| Scenario | Behaviour |
|----------|-----------|
| Empty required field | Warns and re-prompts |
| Invalid date format | Warns and re-prompts with correct format hint |
| Task ID not found | Prints a clear not-found message |
| Invalid menu choice | Warns and re-displays the menu |
| Invalid filter option | Prints a warning message |
| Already completed task | Warns that it is already done |
| No pending tasks to complete | Shows a celebration message |
| Delete without confirmation | Cancels the operation safely |
| Corrupted `todo_list.json` | Falls back to empty state gracefully |
| File write failure | Prints an error without crashing |

---

## 📄 License

This project is open source and free to use under the [MIT License](LICENSE).

---

> Built with ❤️ using pure Python 3. Stay organised, stay productive! ✅
