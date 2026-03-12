# Guessing Game

A command-line number guessing game in Python.

## What This Project Does

The game chooses a random number between `1` and `100`.  
You keep guessing until you find the correct number, and the game tells you if your guess is too high or too low.

When you guess correctly, it shows:
- The correct number
- How many valid tries you used

You can also type `0` at any time to exit immediately.

## Features

- Random target number from `1` to `100`
- Hint after each guess: `Too low` or `Too high`
- Input validation:
  - Rejects non-numeric values
  - Rejects numbers outside `1-100` (except `0` to exit)
- Tracks and displays total tries when you win
- Replay support after each completed round

## Requirements

- Python 3

## Run

From the project folder:

```bash
python3 starter.py
```

## How to Play

1. Enter a number between `1` and `100`.
2. Use the feedback to adjust your next guess.
3. Continue until you guess the correct number.
4. Enter `0` if you want to exit the game immediately.
5. After a win, enter `yes`/`y` to play again, or anything else to quit.

## Example Session

```text
Guess a number between 1 and 100 (or 0 to exit): 30
Too low! Try again.
Guess a number between 1 and 100 (or 0 to exit): 80
Too high! Try again.
Guess a number between 1 and 100 (or 0 to exit): 64
Congratulations! You guessed correctly! The number was 64. You got it in 3 tries.

Do you want to play again? (yes/no): no
Thanks for playing!
```

## Project Structure

- `starter.py` - main game logic and loop
