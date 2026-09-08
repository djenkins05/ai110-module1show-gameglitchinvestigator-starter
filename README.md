# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Game's Purpose

Glitchy Guesser is a number-guessing game built with Streamlit. The 
player selects a difficulty (Easy, Normal, or Hard), which sets the 
range of possible secret numbers and the number of attempts allowed. On 
each guess, the game tells the player whether they're too high, too low, 
or correct, tracks their score and guess history, and lets them start a 
new game at any time.

### Bugs Found

- **Hardcoded guess range:** The instructions shown to the player always 
  said "Guess a number between 1 and 100," regardless of the selected 
  difficulty, instead of reflecting the actual low/high range for that 
  difficulty.
- **Swapped hint messages:** When a guess was too high, the game told 
  the player to go *higher* instead of *lower*, and vice versa for 
  guesses that were too low — the hints were telling players to move in 
  the wrong direction.
- **Buggy string-comparison fallback:** `check_guess` contained a branch 
  that stringified the secret number on every other attempt, which 
  forced the comparison into a string-based fallback path and produced 
  incorrect outcomes/hints.
- **"New Game" didn't fully reset state:** Clicking "New Game" after a 
  win or loss left `status` set to `"won"`/`"lost"`, so the app 
  immediately re-displayed the game-over message and appeared to do 
  nothing. It also left the previous game's `score` and `history` in 
  place instead of clearing them.
- **New game secret ignored difficulty:** When starting a new game, the 
  secret number was generated with a hardcoded `random.randint(1, 100)` 
  instead of using the range for the currently selected difficulty, so 
  changing difficulty had no real effect after the first game.
- **Outdated tests:** Several tests in `test_game_logic.py` were written 
  against an older version of `check_guess` that returned a single 
  string, rather than the current `(outcome, message)` tuple, causing 
  them to fail against the updated function signature.

### Fixes Applied

- Refactored `get_range_for_difficulty`, `parse_guess`, `check_guess`, 
  and `update_score` out of `app.py` into a dedicated `logic_utils.py` 
  module for cleaner separation between game logic and UI code.
- Updated the player-facing range message to use the actual `low`/`high` 
  values for the selected difficulty instead of a hardcoded range.
- Corrected the hint text in `check_guess` so "Too High" tells the 
  player to go **lower** and "Too Low" tells them to go **higher**.
- Removed the faulty string-stringification branch in `check_guess`, 
  leaving a single, correct numeric comparison path.
- Updated the "New Game" button handler to reset `status`, `score`, and 
  `history` in addition to `attempts` and `secret`, so a new game 
  actually starts clean.
- Fixed new-game secret generation to use `get_range_for_difficulty()` 
  so the secret always falls within the selected difficulty's range.
- Updated the outdated tests to unpack the `(outcome, message)` tuple 
  correctly, and added new tests covering the hint-direction bug and the 
  "New Game" reset bugs.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects "Easy" difficulty from the sidebar, setting the secret 
   number to a random value between 1 and 20
2. User enters a guess of 5 
3. game returns "Too Low"
4. User enters a guess of 15 
5. game returns "Too High"
6. User enters a guess of 10 
7. game returns "Win," and the score and 
   guess history update to reflect the completed round
8. User clicks "New Game" → status resets to "playing," score and 
   history clear, and a new secret number is generated within the 
   selected difficulty's range

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ pytest tests/
================================================================
platform darwin -- Python 3.12.1, pytest-9.1.1, pluggy-1.6.0
collected 8 items

tests/test_game_logic.py ........                                [100%]

================================================================
8 passed in 1.96s
================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
