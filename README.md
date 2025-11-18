Hangman (simple CLI)

A small command-line Hangman game written in Python.

How to run

- Make sure you have Python installed (3.7+ recommended).
- From PowerShell in the project folder run:

```powershell
python .\main.py
```

Gameplay

- You have 10 attempts to guess the word.
- Enter single letters to guess.
- Type `hint` to reveal one unrevealed letter; this costs 2 attempts and applies a -3 point penalty and can be used only once.
- Repeated guesses are ignored (no attempt lost) and previously guessed letters are shown.

Scoring

- Correct guesses: +5 points per occurrence of the revealed letter.
- Wrong guesses: -2 points per wrong guess.
- Using the hint: -3 points (in addition to the 2-attempt cost).

Score persistence

- After each game the program asks for your name and saves a record to `scores.json` in the same folder.
- Each record contains `name`, `score`, `word`, `result` (`win` or `lose`) and an ISO timestamp.

Files

- `main.py` - the game
- `scores.json` - created when you save a score (appended as an array of records)
- `README.md` - this file

Want changes?

- I can change the point values, make the hint configurable, or add a high-score display. Tell me which you prefer.
