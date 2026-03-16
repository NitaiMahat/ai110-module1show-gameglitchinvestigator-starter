from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests targeting the hint inversion bug (messages were swapped before fix)
def test_too_high_message_says_go_lower():
    # Guess 60 against secret 50: hint must tell you to go LOWER, not HIGHER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message


def test_too_low_message_says_go_higher():
    # Guess 40 against secret 50: hint must tell you to go HIGHER, not LOWER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_guess_at_range_boundary():
    # Guess 1 against secret 75: should be "Too Low" with Go HIGHER hint
    outcome, message = check_guess(1, 75)
    assert outcome == "Too Low"
    assert "HIGHER" in message
