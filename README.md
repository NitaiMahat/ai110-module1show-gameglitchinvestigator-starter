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

I built a number guessing game where the app picks a secret number and I try to guess it. After each guess I get a hint telling me if I went too high or too low. I keep guessing until I get it right or run out of attempts.

**Bugs I found:**

1. **The hints were backwards** — when my guess was too high it told me "Go HIGHER!" and when it was too low it told me "Go LOWER!". The messages were swapped inside `check_guess` in `app.py`.

2. **New Game did not actually reset the game** — after I won, clicking New Game kept showing "You already won" and I could not type a new guess. The game status was never changed back to `"playing"` so the app stayed stuck.

3. **The secret number was secretly turned into text** — on every second guess the secret was converted to a string before being compared to my guess. This caused a weird bug where the hints were sometimes wrong in a different way.

**How I fixed them:**

1. I swapped the hint messages so "Too High" now says "Go LOWER!" and "Too Low" says "Go HIGHER!".
2. I added `st.session_state.status = "playing"` in the New Game handler so the game properly resets.
3. I removed the string conversion so the secret is always a number when compared to my guess.
4. I moved all the game logic (`check_guess`, `parse_guess`, `get_range_for_difficulty`, `update_score`) out of `app.py` and into `logic_utils.py` to keep things clean.
5. I wrote 6 pytest tests in `tests/test_game_logic.py` to make sure the fixes actually work — all 6 pass.

## 📸 Demo

when guess is higher:
![alt text](<Screenshot (439).png>)
when guess is lower:
![alt text](<Screenshot (442).png>) 
when guess is correct:
![alt text](<Screenshot (440).png>)
running new game:
![alt text](<Screenshot (443).png>)

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
