from pathlib import Path

from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_high_hint_says_go_lower():
    # If the guess (60) is above the secret (50), the hint must tell the
    # player to go LOWER, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_guess_too_low_hint_says_go_higher():
    # If the guess (40) is below the secret (50), the hint must tell the
    # player to go HIGHER, not lower.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_new_game_resets_a_finished_game():
    # Bug: clicking "New Game" after a win/loss left status as "won"/"lost",
    # so the app immediately re-showed the game-over message and stopped,
    # making the button look like it did nothing.
    at = AppTest.from_file(APP_PATH).run()

    at.session_state["status"] = "lost"
    at.session_state["score"] = 42
    at.session_state["history"] = [10, 20, 30]
    at.session_state["attempts"] = 5
    at.run()
    assert len(at.error) == 1  # "Game over" message shown

    new_game_button = [b for b in at.button if "New Game" in b.label][0]
    new_game_button.click().run()

    assert at.session_state["status"] == "playing"
    assert len(at.error) == 0

def test_new_game_resets_score_and_history_mid_game():
    # Bug: New Game reset attempts/secret but left the old score and
    # history in place, so the "new" game still carried over the last one.
    at = AppTest.from_file(APP_PATH).run()

    at.session_state["score"] = 30
    at.session_state["history"] = [5, 15]
    at.session_state["attempts"] = 3
    at.run()

    new_game_button = [b for b in at.button if "New Game" in b.label][0]
    new_game_button.click().run()

    assert at.session_state["score"] == 0
    assert at.session_state["history"] == []
    assert at.session_state["attempts"] == 0

def test_new_game_secret_respects_difficulty_range():
    # Bug: the New Game secret was hardcoded to random.randint(1, 100)
    # instead of using the selected difficulty's range.
    at = AppTest.from_file(APP_PATH).run()
    at.sidebar.selectbox[0].set_value("Easy").run()

    new_game_button = [b for b in at.button if "New Game" in b.label][0]
    new_game_button.click().run()

    assert 1 <= at.session_state["secret"] <= 20
