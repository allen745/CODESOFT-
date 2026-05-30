"""
Rock - Paper - Scissors
A feature-rich CLI game with score tracking, win streaks, and round history.
Pure Python 3 — no external libraries required.
"""

import random
import os


# ── Constants ─────────────────────────────────────────────────────────────────
CHOICES   = ["rock", "paper", "scissors"]
EMOJI     = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

# What each choice beats
BEATS     = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# Result labels
WIN  = "win"
LOSE = "lose"
TIE  = "tie"


# ── Score state ───────────────────────────────────────────────────────────────
score = {"player": 0, "computer": 0, "ties": 0}
current_streak   = 0      # positive = player streak, negative = computer streak
best_streak      = 0      # player's best winning streak this session
round_number     = 0
history          = []     # list of (round, player, computer, result)


# ── Helpers ───────────────────────────────────────────────────────────────────
def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_player_choice():
    """
    Prompt the player until a valid choice is entered.
    Accepts full words or shorthand: r / p / s.
    """
    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
    while True:
        raw = input("\n  Your choice (rock/paper/scissors  or  r/p/s): ").strip().lower()
        if raw in CHOICES:
            return raw
        if raw in shortcuts:
            return shortcuts[raw]
        print("  ⚠  Invalid choice. Please type rock, paper, scissors (or r/p/s).")


def get_computer_choice():
    """Return a random computer choice."""
    return random.choice(CHOICES)


def determine_result(player, computer):
    """Return WIN, LOSE, or TIE from the player's perspective."""
    if player == computer:
        return TIE
    if BEATS[player] == computer:
        return WIN
    return LOSE


def update_streak(result):
    """Update current and best streaks based on the round result."""
    global current_streak, best_streak
    if result == WIN:
        current_streak = max(current_streak, 0) + 1
        best_streak    = max(best_streak, current_streak)
    elif result == LOSE:
        current_streak = min(current_streak, 0) - 1
    else:
        current_streak = 0


def streak_label():
    """Return a human-readable streak message."""
    if current_streak >= 3:
        return f"  🔥 You're on a {current_streak}-win streak!"
    if current_streak <= -3:
        return f"  💻 Computer is on a {abs(current_streak)}-win streak!"
    return ""


# ── Display helpers ───────────────────────────────────────────────────────────
DIVIDER  = "═" * 52
THIN_DIV = "─" * 52

def display_banner():
    print(f"\n{DIVIDER}")
    print("       🎮  ROCK · PAPER · SCISSORS  🎮")
    print(DIVIDER)


def display_scoreboard():
    p  = score["player"]
    c  = score["computer"]
    t  = score["ties"]
    total = p + c + t
    win_pct = f"{(p / total * 100):.0f}%" if total else "—"

    print(f"\n  {THIN_DIV}")
    print(f"  📊  SCOREBOARD          Round {round_number}")
    print(f"  {THIN_DIV}")
    print(f"  👤 You         {p:>3} wins")
    print(f"  💻 Computer    {c:>3} wins")
    print(f"  🤝 Ties        {t:>3}")
    print(f"  🏆 Win rate    {win_pct:>5}")
    if best_streak >= 3:
        print(f"  ⭐ Best streak  {best_streak} in a row")
    print(f"  {THIN_DIV}")


def display_round_result(player, computer, result):
    pe = EMOJI[player]
    ce = EMOJI[computer]

    print(f"\n  {THIN_DIV}")
    print(f"  You chose    ➤  {pe}  {player.capitalize()}")
    print(f"  Computer chose  {ce}  {computer.capitalize()}")
    print(f"  {THIN_DIV}")

    if result == WIN:
        print(f"  🎉  {BEATS[player].capitalize()} loses to {player}. YOU WIN!")
    elif result == LOSE:
        print(f"  😔  {player.capitalize()} loses to {computer}. COMPUTER WINS!")
    else:
        print(f"  🤝  It's a TIE!")

    streak_msg = streak_label()
    if streak_msg:
        print(streak_msg)

    print(f"  {THIN_DIV}")


def display_history():
    """Print the last 5 rounds."""
    if not history:
        return
    print(f"\n  Recent rounds:")
    for rnd, pl, comp, res in history[-5:]:
        icon = "✔" if res == WIN else ("✘" if res == LOSE else "=")
        print(f"    R{rnd:>2}  {EMOJI[pl]} vs {EMOJI[comp]}  {icon}  {res.upper()}")


def display_final_summary():
    p = score["player"]
    c = score["computer"]
    t = score["ties"]
    total = p + c + t

    print(f"\n{DIVIDER}")
    print("            🏁  GAME OVER  🏁")
    print(DIVIDER)
    print(f"\n  Rounds played : {total}")
    print(f"  Your wins     : {p}")
    print(f"  Computer wins : {c}")
    print(f"  Ties          : {t}")

    if total:
        print(f"  Win rate      : {p / total * 100:.1f}%")
    if best_streak >= 3:
        print(f"  Best streak   : {best_streak} wins in a row 🔥")

    if p > c:
        print("\n  🏆  Overall winner: YOU! Well played!")
    elif c > p:
        print("\n  💻  Overall winner: Computer. Better luck next time!")
    else:
        print("\n  🤝  Overall result: It's a draw!")

    print(f"\n{DIVIDER}")
    print("  Thanks for playing. Goodbye! 👋")
    print(f"{DIVIDER}\n")


def ask_play_again():
    """Ask the user if they want to play another round."""
    while True:
        ans = input("\n  Play another round? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("  ⚠  Please enter y or n.")


# ── Main game loop ────────────────────────────────────────────────────────────
def play_round():
    global round_number
    round_number += 1

    print(f"\n  ── Round {round_number} " + "─" * (44 - len(str(round_number))))

    player   = get_player_choice()
    computer = get_computer_choice()
    result   = determine_result(player, computer)

    # Update scores
    if result == WIN:
        score["player"]   += 1
    elif result == LOSE:
        score["computer"] += 1
    else:
        score["ties"]     += 1

    update_streak(result)
    history.append((round_number, player, computer, result))

    display_round_result(player, computer, result)
    display_scoreboard()
    display_history()


def main():
    clear()
    display_banner()
    print("\n  Welcome! Beat the computer at Rock · Paper · Scissors.")
    print("  First to the most wins after as many rounds as you like!\n")
    print(f"  {THIN_DIV}")
    print("  Rules:")
    print("    🪨  Rock     beats  ✂️  Scissors")
    print("    ✂️  Scissors  beats  📄  Paper")
    print("    📄  Paper    beats  🪨  Rock")
    print(f"  {THIN_DIV}")

    while True:
        play_round()
        if not ask_play_again():
            break

    display_final_summary()


if __name__ == "__main__":
    main()
