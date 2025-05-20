# 🤖 Number Guessing Game (Binary Search)

This Python script is an interactive game where the computer tries to guess a number you're thinking of between 0 and 1000 — in **10 tries or fewer**, using a binary search strategy.

## 📋 How It Works

- You (the user) think of a number between 0 and 1000.
- The computer repeatedly makes a guess.
- After each guess, you give feedback:
  - `Too big` – if the guess is higher than your number.
  - `Too small` – if the guess is lower than your number.
  - `Correct` – if the guess is right.
- The computer narrows down its guesses accordingly.

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Save the script as `guess_number.py`.
3. Run it using your terminal or command prompt:

   ```bash
   python guess_number.py
4. Think of a number and follow the on-screen instructions.

## ✅ Example Interaction

```
Think of a number between 0 and 1000, and I'll guess it in no more than 10 tries
I think it's 500
Is it correct? (Too small/Too big/Correct) Too small
I think it's 750
Is it correct? (Too small/Too big/Correct) Too big
I think it's 625
...
I win!
```

## 💡 Notes

- The algorithm uses binary search, guaranteeing a correct guess in 10 or fewer attempts.
- Input is case-insensitive and whitespace-tolerant.
- If you provide unexpected input, the script responds with "Don't lie!" as a basic error handler.

Have fun trying to outsmart the computer! 🧠💻