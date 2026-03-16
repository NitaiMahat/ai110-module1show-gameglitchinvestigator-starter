# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

-When i guess correct and then i press new game you still see the text " you already won. Start a new game  to play again". I expected it to go away when i pressed new game;
- Also i cant enter new guess, even though the new score has been set. Attemp is also fixed at 0 after you guess 0;

- the hint is incorrect. for example if secrect is 75 if i guess something lower it says gues lower if i get something higher it says guess higher.
however if it goes out of the range the hint is correct;


## 2. How did you use AI as a teammate?

I used Claude (an AI tool) to help me find and fix the bugs in this project.

**Good suggestion — fixing the hints:**
The AI told me that the hint messages were the wrong way around. When your guess was too high, it said "Go HIGHER!" and when it was too low, it said "Go LOWER!" the opposite of what it should say. I fixed it by swapping the messages. I checked it was right by running the tests with pytest and they all passed.

**Bad / confusing suggestion — explaining why the hints were wrong:**
The AI also said the bug happened because the secret number was being turned into text on even attempts, and that caused wrong hints through a weird text-sorting issue. This was a bit misleading. The real reason the hints were wrong was just the swapped messages. The text-conversion thing was a separate extra bug. I found this out by testing the `check_guess` function on its own, where there was no text conversion at all, and the hints were still wrong.

---

## 3. Debugging and testing your fixes

I only said a bug was fixed when both the tests passed and the game looked right in the browser.

For the hint bug, I ran `pytest tests/test_game_logic.py -v` and all 6 tests passed. For example, one test checks that if your guess is 60 and the secret is 50, the message says "LOWER". That test used to fail before the fix.

For the new game bug, there is no automated test for it because it needs the game to be running. So I tested it by hand I played the game, won, pressed New Game, and checked that the "you already won" message went away and I could type a new guess.

The AI helped me write the tests too. It suggested checking if the word "LOWER" is inside the message instead of checking the exact full message. That way if someone changes the emoji later, the test still works.

---

## 4. What did you learn about Streamlit and state?

Every time I click a button, Streamlit reruns the whole page. It forgets everything unless I save it in `session_state`. I think of it like a small notebook the app keeps open. If I forget to update something in that notebook  like resetting the game status when I press New Game  the old value stays and breaks the game.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing small tests for every bug I fix. Before this project I would just run the app and look at it. But using pytest showed me that tests catch problems faster and give you proof the fix actually worked.

Next time I work with AI, I want to double-check everything it tells me instead of trusting it right away. In this project the AI gave me one explanation that was a bit misleading, and I only caught it because I tested the function on its own.

This project made me realize that AI-generated code can look correct but still have sneaky bugs in it. You have to read it carefully and test it, just like code written by a person.
