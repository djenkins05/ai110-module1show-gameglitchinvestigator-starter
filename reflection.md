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
For this project I Used 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

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
