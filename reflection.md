# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  

The game was very confusing and had a lot of misleading bugs for the guessing game. One bug I noticed was that the hint was backwards. Instead of saying go higher it would say go lower and vice versa. Another bug I noticed was that when I restarted the game, it would not really restart but remain frozen, and all the attempts and scores were inaccurate. The patterns for the scores and attempts also did not line up correctly. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

AI suggested that I fix the number of attempts for the difficulty levels when I was adjusting the range for each level. I found this useful because the number of attempts also affects how difficult the game is. After comparing the levels, I corrected them so Easy used 1–20 with 8 attempts, Normal used 1–50 with 6 attempts, and Hard used 1–100 with 5 attempts. To verify the result, I kept restarting the game and testing each difficulty to make sure the attempts and ranges reset correctly. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One suggestion AI made that was inaccurate was when I was setting the starting score. It listed the starting score as 0, and every time someone guessed the score would go into the negatives. I noticed this when I was testing the game and the score kept becoming very low. I fixed this by starting the score higher and making it decrease with each attempt.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
- Did AI help you design or understand any tests? How?

When figuring out if a bug was really fixed, I would play the game in different scenarios, such as when I did not guess the secret number or when I tried different difficulty levels. Once the scores and attempt patterns were fixed, I started testing cases where numbers were out of range or when letters or symbols were entered. These tests helped show whether the patterns in my code were correct or not. AI helped me understand how the scoring pattern worked at first since I did not see a clear pattern before fixing the bug.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

One thing I learned about Streamlit is that the script reruns every time the user interacts with the app, like when entering a guess or pressing a button. Because of this, variables reset each time the code runs. In the original game, the secret number kept changing because a new random number was created on every rerun. I fixed this by storing the secret number in st.session_state, which keeps the value the same during the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future projects is testing my code more often while fixing bugs. It also taught me to be more detailed when asking AI questions or writing prompts so I can get clearer and more accurate help. I also learned that if I do not fully understand a function, I can ask AI to explain it instead of just fixing the code without understanding it. Playing the game multiple times helped me notice when something was not working correctly. This project also showed me that AI can be helpful for suggestions, but I still need to check and test the code myself.
