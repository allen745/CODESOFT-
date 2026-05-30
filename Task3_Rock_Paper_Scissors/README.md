# 🎮 Rock · Paper · Scissors

A feature-rich, interactive Rock-Paper-Scissors game built with pure Python 3. Play unlimited rounds against the computer, track your score, monitor win streaks, and review your round history — all from the terminal.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Example Session](#example-session)
- [Project Structure](#project-structure)
- [Function Reference](#function-reference)
- [Error Handling](#error-handling)
- [License](#license)

---

## ✨ Features

- 🪨📄✂️ Classic **Rock, Paper, Scissors** gameplay
- ⌨️ Accepts **full words** (`rock`) or **shortcuts** (`r / p / s`)
- 🎲 Truly **random computer opponent** — fair every round
- 📊 **Live scoreboard** after every round — wins, ties, and win rate %
- 🔥 **Win streak tracker** — alerts at 3+ consecutive wins or losses
- ⭐ **Best streak** recorded for the entire session
- 📜 **Round history** — last 5 rounds shown with emoji and result icons
- 🏁 **Final summary** at the end — full stats and overall winner
- ♻️ **Play again loop** — as many rounds as you want
- 🖥️ **Screen clear** on start for a clean experience (Windows & Mac/Linux)
- 🛡️ **Input validation** on every prompt — no crashes on bad input
- 📦 **Zero dependencies** — pure Python standard library

---

## ✅ Requirements

- Python **3.6** or higher
- No third-party packages needed

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
   cd rock-paper-scissors
   ```

2. **Verify Python is installed:**

   ```bash
   python --version
   # or
   python3 --version
   ```

No `pip install` needed — only Python's built-in `random` and `os` modules are used.

---

## ▶️ Usage

Run the script from your terminal:

```bash
python rock_paper_scissors.py
```

or on some systems:

```bash
python3 rock_paper_scissors.py
```

---

## 🕹️ How to Play

1. The game displays the rules and starts **Round 1**
2. Enter your choice when prompted:
   - Type `rock`, `paper`, or `scissors`
   - **Or** use the shortcuts: `r`, `p`, `s`
3. The computer makes its choice randomly
4. The result is shown — win, lose, or tie
5. The **scoreboard** and **last 5 rounds** are updated
6. Choose to play again (`y`) or quit (`n`)
7. On exit, a **final summary** with full session stats is displayed

---

## 📏 Game Rules

| Your Choice | Beats | Loses To |
|:-----------:|:-----:|:--------:|
| 🪨 Rock | ✂️ Scissors | 📄 Paper |
| ✂️ Scissors | 📄 Paper | 🪨 Rock |
| 📄 Paper | 🪨 Rock | ✂️ Scissors |

---

## 💻 Example Session

```
════════════════════════════════════════════════════
       🎮  ROCK · PAPER · SCISSORS  🎮
════════════════════════════════════════════════════

  Welcome! Beat the computer at Rock · Paper · Scissors.
  First to the most wins after as many rounds as you like!

  ────────────────────────────────────────────────────
  Rules:
    🪨  Rock     beats  ✂️  Scissors
    ✂️  Scissors  beats  📄  Paper
    📄  Paper    beats  🪨  Rock
  ────────────────────────────────────────────────────

  ── Round 1 ──────────────────────────────────────────

  Your choice (rock/paper/scissors  or  r/p/s): rock

  ────────────────────────────────────────────────────
  You chose    ➤  🪨  Rock
  Computer chose  ✂️  Scissors
  ────────────────────────────────────────────────────
  🎉  Scissors loses to rock. YOU WIN!
  ────────────────────────────────────────────────────

  ────────────────────────────────────────────────────
  📊  SCOREBOARD          Round 1
  ────────────────────────────────────────────────────
  👤 You           1 wins
  💻 Computer      0 wins
  🤝 Ties          0
  🏆 Win rate       100%
  ────────────────────────────────────────────────────

  Recent rounds:
    R 1  🪨 vs ✂️  ✔  WIN

  Play another round? (y/n): n

════════════════════════════════════════════════════
            🏁  GAME OVER  🏁
════════════════════════════════════════════════════

  Rounds played : 1
  Your wins     : 1
  Computer wins : 0
  Ties          : 0
  Win rate      : 100.0%

  🏆  Overall winner: YOU! Well played!

════════════════════════════════════════════════════
  Thanks for playing. Goodbye! 👋
════════════════════════════════════════════════════
```

---

## 📁 Project Structure

```
rock-paper-scissors/
│
├── rock_paper_scissors.py   ← Main script — all logic lives here
└── README.md                ← This file
```

---

## 🔧 Function Reference

| Function | Purpose |
|----------|---------|
| `clear()` | Clears the terminal screen (cross-platform) |
| `get_player_choice()` | Prompts and validates player input (full word or shortcut) |
| `get_computer_choice()` | Returns a random choice for the computer |
| `determine_result()` | Compares choices and returns WIN, LOSE, or TIE |
| `update_streak()` | Updates current and best win streak |
| `streak_label()` | Returns a streak alert message at 3+ consecutive results |
| `display_banner()` | Prints the game title banner |
| `display_scoreboard()` | Prints the live scoreboard after each round |
| `display_round_result()` | Shows both choices and the round outcome |
| `display_history()` | Prints the last 5 rounds with emoji and result icons |
| `display_final_summary()` | Prints full session stats and overall winner on exit |
| `ask_play_again()` | Prompts the user to continue or quit |
| `play_round()` | Runs a single complete round end-to-end |
| `main()` | Entry point — shows welcome screen and drives the game loop |

---

## 🛡️ Error Handling

| Scenario | Behaviour |
|----------|-----------|
| Invalid choice (e.g. `lizard`) | Warns and re-prompts |
| Invalid shortcut (e.g. `x`) | Warns and re-prompts |
| Invalid play-again answer | Warns and re-prompts |
| Empty input on any prompt | Warns and re-prompts |

---

## 📄 License

This project is open source and free to use under the [MIT License](LICENSE).
>
> 
## 🔗 Connect With Me

MADE BY Allen Stivanson Christian || Patent holder

MADE for CODESOFT :- https://www.linkedin.com/company/codsoft/posts/?feedView=all    

- 💼 LinkedIn: [https://in.linkedin.com/in/your-profile ](https://www.linkedin.com/in/allen-christian-708545409/) 
- 💻 GitHub: https://github.com/allen745  
-  portfolio  https://allen745.github.io

> Built with ❤️ using pure Python 3. May the best hand win! 🪨📄✂️
