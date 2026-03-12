import random

def play_game():
    random_number = random.randint(1, 100)  # numbers 1 - 100
    attempts = 0
    
    # handle user guesses
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100 (or 0 to exit): "))

            if guess == 0:
                print("You chose to exit the game.")
                return False
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue

            attempts += 1
            
            if guess == random_number:
                print(
                    f"Congratulations! You guessed correctly! "
                    f"The number was {random_number}. "
                    f"You got it in {attempts} tries."
                )
                return True
            elif guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number! (0 to exit)")

# BONUS - let player play again if they want!
while True:
    finished_round = play_game()
    if not finished_round:
        print("Thanks for playing!")
        break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing!")
        break
