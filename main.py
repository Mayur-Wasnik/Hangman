import random
import json
import os
from datetime import datetime, timezone, timedelta

try:
    from zoneinfo import ZoneInfo
    IST = ZoneInfo("Asia/Kolkata")
except Exception:
    IST = timezone(timedelta(hours=5, minutes=30))

WORDS = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift', 'go', 'rust']

def save_score(record, path='scores.json'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []
    data.append(record)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def play():
    chosen = random.choice(WORDS)
    display = ['_' for _ in chosen]
    attempts = 10
    score = 0
    guessed = set()
    hint_available = True

    print(f"Welcome to Hangman! You have {attempts} attempts.")
    print("Type 'hint' to reveal one letter (costs 2 attempts; usable once).")

    while attempts > 0 and '_' in display:
        print('\n' + ' '.join(display))
        if guessed:
            print('Guessed:', ' '.join(sorted(guessed)))
        print('Score:', score)
        guess = input("Enter a letter (or 'hint'): ").lower().strip()
        if not guess:
            print('Please enter something.')
            continue

        if guess == 'hint':
            if not hint_available:
                print('Hint already used.')
                continue
            choices = [c for c in set(chosen) if c not in guessed]
            if not choices:
                print('Nothing to reveal.')
                continue
            letter = random.choice(choices)
            for i, ch in enumerate(chosen):
                if ch == letter:
                    display[i] = letter
            attempts -= 2
            score -= 3
            hint_available = False
            guessed.add(letter)
            print(f"Revealed: {letter}. Attempts left: {attempts}")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue
        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.add(guess)
        if guess in chosen:
            count = chosen.count(guess)
            for i, ch in enumerate(chosen):
                if ch == guess:
                    display[i] = guess
            gained = 5 * count
            score += gained
            print(f"Good! +{gained} points.")
        else:
            attempts -= 1
            score -= 2
            print(f"Wrong! Attempts left: {attempts}")

    result = 'win' if '_' not in display else 'lose'
    print()
    if result == 'win':
        print('Congratulations! You guessed the word:', chosen)
    else:
        print('Game Over! The word was:', chosen)
    print('Final score:', score)

    name = input("Enter your name to save your score (leave blank for 'Anonymous'): ").strip() or 'Anonymous'
    record = {
        'name': name,
        'score': score,
        'word': chosen,
        'result': result,
        'timestamp': datetime.now(IST).isoformat()
    }
    save_score(record)
    print(f"Score saved to scores.json. Thanks, {name}!")

if __name__ == '__main__':
    play()
    