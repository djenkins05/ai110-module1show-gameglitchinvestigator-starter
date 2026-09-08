# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked like a random number generator guess game where depending on the difficulty goes in a certain range and gives a certain number of guesses, for example in normal 1-100 in 8 guesses, then easy is 1-20 in 6 guess, and hard is 1-50 in 5 guesses. You chose the difficulty on the left sidebar to chose the difficulty. There is a debug function to tell help figure out bugs. 

- List at least two concrete bugs you noticed at the start  
The new game button doesn't work 
Changing the difficulty doesn't change anything on the frontend 
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|     Input     |   Expected Behavior   | Actual Behavior | Console Output / Error |
|---------------|-----------------------|-----------------|------------------------|
|New game button|For a new game to start|Nothing happens  |No Output         

|Guess of 8     |     Go higher         | Go Lower        | No Output

|Easy difficulty|Show new range and number of guess|Keeps the rules for normal difficulty| No output 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

For this project I used ClaudeAI that is integrated as an extension in VSCode so that it can directly look at my code and make suggestion directly to the file. Where I only have to press a button to integrate whatever changes I came up with, while using Claude. Claude was the only AI that I used. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
**What the AI suggested:** The AI identified that the button's handler 
wasn't fully resetting game state. Specifically, it pointed out that 
`status` was never being reset to `"playing"` after a win/loss, and that 
`score`, `history`, and `attempts` were also being left over from the 
previous game instead of being cleared. It suggested resetting all of 
these values in the "New Game" handler.

**Whether the suggestion was correct:** The suggestion was correct. Once 
I implemented the fix, the button behaved as expected — starting a new 
game fully reset the session state instead of leaving stale values behind.

**How I verified the result:** I wrote two pytest tests targeting the two 
specific failure modes the AI identified — one confirming that starting a 
new game after a win/loss properly resets `status` back to `"playing"` 
instead of re-showing the game-over message, and another confirming 
that `score`, `history`, and `attempts` are all cleared when a new game 
starts mid-game rather than carrying over from the previous one. Both 
tests passed after applying the fix. I also manually tested the behavior 
by playing a full game to completion, win and loss, in the app itself and 
clicking "New Game" each time, confirming the status, score, history, and 
attempts all reset correctly and the game was immediately playable again.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
**What the AI suggested:** After `check_guess()` was refactored to return 
a tuple (`outcome, message`) instead of a single string, I asked the AI 
to help update the old tests to match the new function signature. For 
most of the tests (`test_winning_guess`, `test_guess_too_high`, 
`test_guess_too_low`), it correctly suggested changing lines like 
`result = check_guess(50, 50)` to `outcome, _ = check_guess(50, 50)`, 
using `_` to discard the message since those tests only cared about the 
outcome. It then tried to apply this same pattern to 
`test_guess_too_high_hint_says_go_lower` and 
`test_guess_too_low_hint_says_go_higher`, suggesting those be rewritten 
the same way — unpacking the message into `_` and discarding it. 
**Whether the suggestion was correct:** This part of the suggestion was 
incorrect/misleading. Those two tests exist specifically to check the 
*content* of the hint message (that it says "LOWER" instead of "HIGHER," 
and vice versa). Discarding the message into `_` removed the exact value 
the test was supposed to validate, so applying the AI's blanket fix 
caused the test to break/error out instead of actually testing anything, 
it was a case of the AI over-generalizing a pattern that worked for other 
tests but didn't fit the intent of these two.
**How I verified the result:** I ran the tests after applying the AI's 
suggested change and got an error, which told me the fix wasn't right 
for this case. I went back into the code and manually kept `message` 
instead of discarding it (`outcome, message = check_guess(60, 50)`), 
then reran the tests and then they passed and correctly caught the hint text.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
