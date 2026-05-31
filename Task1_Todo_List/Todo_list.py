"""
To-Do List Application
A full-featured CLI task manager with JSON persistence.
Supports: Add, View, Update, Complete, Delete tasks with priorities,
          due dates, categories, and filtering.
Pure Python 3 — no external libraries required.
"""

import json
import os
import sys
from datetime import datetime, date


# ── Storage ───────────────────────────────────────────────────────────────────
DATA_FILE = "todo_list.json"


def load_tasks():
    """Load tasks from JSON file. Returns a dict keyed by task ID."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("  ⚠  Could not read tasks file. Starting fresh.")
        return {}


def save_tasks(tasks):
    """Persist tasks dict to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"  ✖  Failed to save tasks: {e}")


def next_id(tasks):
    """Generate the next integer task ID as a string."""
    if not tasks:
        return "1"
    return str(max(int(k) for k in tasks.keys()) + 1)


# ── Constants ─────────────────────────────────────────────────────────────────
PRIORITIES   = {"1": "🔴 High", "2": "🟡 Medium", "3": "🟢 Low"}
PRIORITY_MAP = {"high": "🔴 High", "medium": "🟡 Medium", "low": "🟢 Low",
                "1": "🔴 High", "2": "🟡 Medium", "3": "🟢 Low"}
STATUS_DONE  = "✅ Done"
STATUS_PEND  = "⏳ Pending"
DIVIDER      = "═" * 58
THIN_DIV     = "─" * 58


# ── Helpers ───────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def today_str():
    return date.today().strftime("%Y-%m-%d")


def is_overdue(due_date, status):
    """Return True if task is past due and not completed."""
    if not due_date or status == STATUS_DONE:
        return False
    try:
        return date.fromisoformat(due_date) < date.today()
    except ValueError:
        return False


def validate_date(date_str):
    """Validate YYYY-MM-DD format and ensure it's today or future."""
    try:
        d = date.fromisoformat(date_str)
        return True, d
    except ValueError:
        return False, None


def get_priority_label(raw):
    """Convert user input to a priority label."""
    return PRIORITY_MAP.get(raw.lower(), "🟡 Medium")


def prompt(label, required=True, hint="", default=""):
    """Generic input prompt. Returns stripped input or default."""
    hint_str  = f" ({hint})" if hint else ""
    deflt_str = f" [{default}]" if default else ""
    while True:
        val = input(f"  {label}{hint_str}{deflt_str}: ").strip()
        if not val:
            if default:
                return default
            if required:
                print(f"  ⚠  {label} is required.\n")
                continue
            return ""
        return val


def confirm(question):
    """Yes/no confirmation. Returns True for yes."""
    while True:
        ans = input(f"  {question} (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("  ⚠  Please enter y or n.")


# ── Display ───────────────────────────────────────────────────────────────────
def banner():
    print(f"\n{DIVIDER}")
    print("          ✅  TO-DO LIST APPLICATION  ✅")
    print(DIVIDER)


def print_menu():
    print(f"\n  {THIN_DIV}")
    print("  MAIN MENU")
    print(f"  {THIN_DIV}")
    print("  1.  ➕  Add new task")
    print("  2.  📋  View all tasks")
    print("  3.  🔍  Search / Filter tasks")
    print("  4.  ✏️   Update a task")
    print("  5.  ✅  Mark task as complete")
    print("  6.  🗑️   Delete a task")
    print("  7.  📊  View summary / stats")
    print("  0.  🚪  Exit")
    print(f"  {THIN_DIV}")


def status_icon(status, due_date):
    if status == STATUS_DONE:
        return "✅"
    if is_overdue(due_date, status):
        return "🔴"
    return "⏳"


def print_task_row(tid, t, index=None):
    """Print a compact one-line task summary."""
    idx      = f"{index}." if index is not None else f"#{tid}"
    icon     = status_icon(t["status"], t.get("due_date", ""))
    due      = f"  📅 {t['due_date']}" if t.get("due_date") else ""
    overdue  = " ‼️ OVERDUE" if is_overdue(t.get("due_date", ""), t["status"]) else ""
    priority = t.get("priority", "🟡 Medium")
    cat      = f"  [{t['category']}]" if t.get("category") else ""
    print(f"  {idx:<5} {icon}  {t['title']:<28} {priority}{due}{overdue}{cat}")


def format_task_detail(tid, t):
    """Return a detailed formatted task card."""
    overdue = " ‼️  OVERDUE!" if is_overdue(t.get("due_date", ""), t["status"]) else ""
    lines = [
        f"\n  {THIN_DIV}",
        f"  ID       : {tid}",
        f"  Title    : {t['title']}",
        f"  Status   : {t['status']}{overdue}",
        f"  Priority : {t.get('priority', '🟡 Medium')}",
        f"  Category : {t.get('category') or '—'}",
        f"  Due Date : {t.get('due_date') or '—'}",
        f"  Notes    : {t.get('notes') or '—'}",
        f"  Created  : {t.get('created', '—')}",
        f"  Updated  : {t.get('updated') or '—'}",
        f"  {THIN_DIV}",
    ]
    return "\n".join(lines)


def sort_tasks(tasks):
    """Sort tasks: pending first, then by priority, then by due date."""
    priority_order = {"🔴 High": 0, "🟡 Medium": 1, "🟢 Low": 2}
    def sort_key(item):
        tid, t = item
        done     = 1 if t["status"] == STATUS_DONE else 0
        prio     = priority_order.get(t.get("priority", "🟡 Medium"), 1)
        due      = t.get("due_date") or "9999-12-31"
        return (done, prio, due)
    return sorted(tasks.items(), key=sort_key)


# ── Core Operations ───────────────────────────────────────────────────────────
def add_task(tasks):
    print(f"\n  {THIN_DIV}")
    print("  ➕  ADD NEW TASK")
    print(f"  {THIN_DIV}")

    title = prompt("Task title")

    # Priority
    print("\n  Priority:")
    print("    1. 🔴 High   2. 🟡 Medium   3. 🟢 Low")
    praw     = prompt("Choose priority", hint="1/2/3 or high/medium/low", default="2")
    priority = get_priority_label(praw)

    # Category
    category = prompt("Category", required=False, hint="e.g. Work, Personal, Study")

    # Due date
    due_date = ""
    while True:
        due_raw = prompt("Due date", required=False, hint="YYYY-MM-DD, or press Enter to skip")
        if not due_raw:
            break
        valid, _ = validate_date(due_raw)
        if valid:
            due_date = due_raw
            break
        print("  ⚠  Invalid date format. Use YYYY-MM-DD (e.g. 2026-06-15).\n")

    notes = prompt("Notes / description", required=False)

    tid = next_id(tasks)
    tasks[tid] = {
        "title":    title,
        "status":   STATUS_PEND,
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "notes":    notes,
        "created":  datetime.now().strftime("%Y-%m-%d %H:%M"),
        "updated":  "",
    }
    save_tasks(tasks)
    print(f"\n  ✔  Task '{title}' added successfully! (ID: {tid})")


def view_all(tasks, filtered=None, label="ALL TASKS"):
    print(f"\n  {THIN_DIV}")
    print(f"  📋  {label}")
    print(f"  {THIN_DIV}")

    source = filtered if filtered is not None else tasks
    if not source:
        print("  No tasks found. Add one with option 1!")
        return

    sorted_tasks = sort_tasks(source)

    print(f"\n  {'#':<5} {'St':<3} {'Title':<28} {'Priority':<12} Due Date")
    print(f"  {'─'*5} {'─'*3} {'─'*28} {'─'*12} {'─'*10}")
    for i, (tid, t) in enumerate(sorted_tasks, 1):
        print_task_row(tid, t, index=i)

    total   = len(source)
    done    = sum(1 for t in source.values() if t["status"] == STATUS_DONE)
    pending = total - done
    print(f"\n  Total: {total}  |  ✅ Done: {done}  |  ⏳ Pending: {pending}")

    # Detail view
    print()
    choice = input("  Enter task ID for full details (or press Enter to go back): ").strip()
    if choice in source:
        print(format_task_detail(choice, source[choice]))
    elif choice:
        print("  ⚠  Task ID not found.")


def search_filter(tasks):
    print(f"\n  {THIN_DIV}")
    print("  🔍  SEARCH / FILTER TASKS")
    print(f"  {THIN_DIV}")

    if not tasks:
        print("  No tasks available.")
        return

    print("\n  Filter by:")
    print("  1. 🔎 Search by keyword (title/notes)")
    print("  2. 🔴 Priority")
    print("  3. 📁 Category")
    print("  4. ✅ Status (pending / done)")
    print("  5. 📅 Overdue tasks")

    opt = input("\n  Choose filter (1–5): ").strip()

    if opt == "1":
        query = input("  Enter keyword: ").strip().lower()
        result = {
            tid: t for tid, t in tasks.items()
            if query in t["title"].lower() or query in (t.get("notes") or "").lower()
        }
        view_all(tasks, filtered=result, label=f"RESULTS FOR '{query.upper()}'")

    elif opt == "2":
        print("  Priority: 1=🔴 High  2=🟡 Medium  3=🟢 Low")
        praw  = input("  Choose: ").strip()
        plabel = get_priority_label(praw)
        result = {tid: t for tid, t in tasks.items() if t.get("priority") == plabel}
        view_all(tasks, filtered=result, label=f"{plabel} PRIORITY TASKS")

    elif opt == "3":
        cats = sorted(set(t.get("category", "") for t in tasks.values() if t.get("category")))
        if not cats:
            print("  No categories found.")
            return
        print("  Available categories: " + ", ".join(cats))
        cat = input("  Enter category: ").strip()
        result = {tid: t for tid, t in tasks.items()
                  if (t.get("category") or "").lower() == cat.lower()}
        view_all(tasks, filtered=result, label=f"CATEGORY: {cat.upper()}")

    elif opt == "4":
        sv = input("  Status (pending/done): ").strip().lower()
        target = STATUS_DONE if sv == "done" else STATUS_PEND
        result = {tid: t for tid, t in tasks.items() if t["status"] == target}
        view_all(tasks, filtered=result, label=f"{sv.upper()} TASKS")

    elif opt == "5":
        result = {tid: t for tid, t in tasks.items()
                  if is_overdue(t.get("due_date", ""), t["status"])}
        view_all(tasks, filtered=result, label="OVERDUE TASKS")

    else:
        print("  ⚠  Invalid option.")


def update_task(tasks):
    print(f"\n  {THIN_DIV}")
    print("  ✏️   UPDATE TASK")
    print(f"  {THIN_DIV}")

    if not tasks:
        print("  No tasks to update.")
        return

    tid = input("\n  Enter task ID to update: ").strip()
    if tid not in tasks:
        print("  ⚠  Task not found.")
        return

    t = tasks[tid]
    print(format_task_detail(tid, t))
    print("  Leave a field blank to keep the current value.\n")

    new_title    = input(f"  Title [{t['title']}]: ").strip()
    print(f"  Priority options: 1=🔴High  2=🟡Medium  3=🟢Low")
    new_praw     = input(f"  Priority [{t.get('priority', '🟡 Medium')}]: ").strip()
    new_category = input(f"  Category [{t.get('category') or '—'}]: ").strip()

    new_due = ""
    while True:
        new_due_raw = input(f"  Due date [{t.get('due_date') or '—'}] (YYYY-MM-DD): ").strip()
        if not new_due_raw:
            break
        if new_due_raw.lower() in ("none", "clear", "-"):
            new_due = "__clear__"
            break
        valid, _ = validate_date(new_due_raw)
        if valid:
            new_due = new_due_raw
            break
        print("  ⚠  Invalid date. Use YYYY-MM-DD or type 'clear' to remove.\n")

    new_notes = input(f"  Notes [{t.get('notes') or '—'}]: ").strip()

    if new_title:    t["title"]    = new_title
    if new_praw:     t["priority"] = get_priority_label(new_praw)
    if new_category: t["category"] = new_category
    if new_due == "__clear__": t["due_date"] = ""
    elif new_due:    t["due_date"] = new_due
    if new_notes:    t["notes"]    = new_notes

    t["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    tasks[tid]   = t
    save_tasks(tasks)
    print(f"\n  ✔  Task '{t['title']}' updated successfully!")


def mark_complete(tasks):
    print(f"\n  {THIN_DIV}")
    print("  ✅  MARK TASK AS COMPLETE")
    print(f"  {THIN_DIV}")

    if not tasks:
        print("  No tasks available.")
        return

    pending = {tid: t for tid, t in tasks.items() if t["status"] == STATUS_PEND}
    if not pending:
        print("  🎉 All tasks are already completed!")
        return

    print(f"\n  {'ID':<5} {'Title':<30} Priority")
    print(f"  {'─'*5} {'─'*30} {'─'*12}")
    for tid, t in sort_tasks(pending):
        print(f"  #{tid:<4} {t['title']:<30} {t.get('priority', '🟡 Medium')}")

    print()
    tid = input("  Enter task ID to mark as complete: ").strip()
    if tid not in tasks:
        print("  ⚠  Task not found.")
        return
    if tasks[tid]["status"] == STATUS_DONE:
        print(f"  ⚠  Task '{tasks[tid]['title']}' is already completed.")
        return

    tasks[tid]["status"]  = STATUS_DONE
    tasks[tid]["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_tasks(tasks)
    print(f"\n  🎉 Task '{tasks[tid]['title']}' marked as complete!")


def delete_task(tasks):
    print(f"\n  {THIN_DIV}")
    print("  🗑️   DELETE TASK")
    print(f"  {THIN_DIV}")

    if not tasks:
        print("  No tasks to delete.")
        return

    tid = input("\n  Enter task ID to delete: ").strip()
    if tid not in tasks:
        print("  ⚠  Task not found.")
        return

    t = tasks[tid]
    print(format_task_detail(tid, t))

    if confirm(f"Delete '{t['title']}'? This cannot be undone."):
        del tasks[tid]
        save_tasks(tasks)
        print(f"\n  ✔  Task '{t['title']}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


def view_summary(tasks):
    print(f"\n  {THIN_DIV}")
    print("  📊  SUMMARY & STATISTICS")
    print(f"  {THIN_DIV}")

    if not tasks:
        print("  No tasks yet. Start by adding one!")
        return

    total    = len(tasks)
    done     = sum(1 for t in tasks.values() if t["status"] == STATUS_DONE)
    pending  = total - done
    overdue  = sum(1 for t in tasks.values()
                   if is_overdue(t.get("due_date", ""), t["status"]))
    high     = sum(1 for t in tasks.values() if t.get("priority") == "🔴 High" and t["status"] != STATUS_DONE)
    medium   = sum(1 for t in tasks.values() if t.get("priority") == "🟡 Medium" and t["status"] != STATUS_DONE)
    low      = sum(1 for t in tasks.values() if t.get("priority") == "🟢 Low" and t["status"] != STATUS_DONE)
    pct      = f"{done / total * 100:.1f}%" if total else "0%"

    # Categories
    cats = {}
    for t in tasks.values():
        c = t.get("category") or "Uncategorized"
        cats[c] = cats.get(c, 0) + 1

    print(f"\n  📌 Total tasks     : {total}")
    print(f"  ✅ Completed       : {done}  ({pct})")
    print(f"  ⏳ Pending         : {pending}")
    print(f"  ‼️  Overdue         : {overdue}")
    print(f"\n  Pending by Priority:")
    print(f"    🔴 High          : {high}")
    print(f"    🟡 Medium        : {medium}")
    print(f"    🟢 Low           : {low}")

    if cats:
        print(f"\n  Tasks by Category:")
        for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
            print(f"    📁 {cat:<20} {count} task(s)")

    # Progress bar
    bar_len  = 30
    filled   = int(bar_len * done / total) if total else 0
    bar      = "█" * filled + "░" * (bar_len - filled)
    print(f"\n  Progress: [{bar}] {pct}")
    print(f"\n  {THIN_DIV}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    tasks = load_tasks()
    clear()
    banner()

    total   = len(tasks)
    done    = sum(1 for t in tasks.values() if t["status"] == STATUS_DONE)
    overdue = sum(1 for t in tasks.values()
                  if is_overdue(t.get("due_date", ""), t["status"]))

    print(f"\n  Welcome to your To-Do List! 📋")
    print(f"  {total} task(s) loaded  |  ✅ {done} done  |  ⏳ {total-done} pending", end="")
    print(f"  |  ‼️  {overdue} overdue" if overdue else "")

    while True:
        print_menu()
        choice = input("  Choose an option (0–7): ").strip()

        if   choice == "1": add_task(tasks)
        elif choice == "2": view_all(tasks)
        elif choice == "3": search_filter(tasks)
        elif choice == "4": update_task(tasks)
        elif choice == "5": mark_complete(tasks)
        elif choice == "6": delete_task(tasks)
        elif choice == "7": view_summary(tasks)
        elif choice == "0":
            print(f"\n  Goodbye! Stay productive! 👋\n")
            sys.exit(0)
        else:
            print("  ⚠  Invalid option. Please choose 0–7.")


if __name__ == "__main__":
    main()
