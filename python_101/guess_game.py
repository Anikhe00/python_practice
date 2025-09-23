import random

while True:
    # Step 1: Generate a secret number and intialize counter for the number of guess
    secret_number = random.randint(1, 10)
    guess_count = 0 

    print("I have chosen a number between 1 and 10. Can you guess it?")

    # Step 2: Keep asking until the user guesses correctly
    while True:
        guess = int(input("Enter your guess: "))
        guess_count += 1 

        # Step 3: Match the guess to the secret number
        match guess:
            case _ if guess == secret_number:
                print(f"🎉 Congratulations, you guessed it in {guess_count} tries!")
                break
            case _ if guess > secret_number:
                print("⬆️ Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("⬇️ Nope, your guess is a bit low. Give it another shot!")

    # Step 4: Ask if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again not in ("yes", "y"):
        print("Thanks for playing! 👋")
        break