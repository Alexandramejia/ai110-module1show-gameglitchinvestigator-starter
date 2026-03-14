# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  

The game was very confusing and had alot of misleading bugs for the guessing game. One bug I noticed was that the hint was backwards instead of going higher it was say go lower and vise versa. Another bug I notice was that when I would restart the game, it would never really re-start but remain frozen and all the attempts and scores were in accurate. All the patterns for the scores and attempts never seemed to line up. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggested that I fix the number of attempts for the diffculity level, when I was fixing the range amount for the diffcultit which I found useful and important because that also plays a role on how diffcult the game is. While I was adjusting easy mode to have numbers 1 through 20 it only had 4 attemps whereas numbers 1-100 for hard mode had 8 attemps. The easy mode had less tries than hard, which would make the levels inaccruate. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One suggestion AI made that was inaccurate was when I was setting the start score, it listed it as 0 and then everytime someone guessed it would go into the negatives making the user's score a negative result. I noticed when I was attemping guessing and the score was always very low. I fixed this by making the start score high and each guess declines the more guesses a user does. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
- Did AI help you design or understand any tests? How?
When figuring out if a bug was really fixed I would always play the game in the case if I were to not figure out the sercet number, when I did and the different amount of diffculties. Once the scores and attempt patterns were fixed I would start testing in the case if the numbers were out of range, letters or different symbols. All these tests showed my codes patterns weather they were correct or not. AI helped me understand how the score pattern was calulated at first since I didnt see a pattern after notcin the bug with the pattern I created my own rules for the score whcih was decreading the start score each time after an attempt.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
