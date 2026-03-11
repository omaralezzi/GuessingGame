import random

def play_game():
    random_number = random.randint(1, 10)  # numbers 1 - 10
    
    # handle user guesses
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10!")
                continue
            
            if guess == random_number:
                print(f"Congratulations! You guessed correctly! The number was {random_number}.")
                break
            elif guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number!")

# BONUS - let player play again if they want!
while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing!")
        break