# initialize a bag of marbles: 6 green and 4 red
marbles = ['green'] * 6 + ['red'] * 4

# User starts the game with 1000 gold prizes or $, ￡, €
initial_money = 1000
money = initial_money
target_money = initial_money * 2
rounds = 0

# Prompt user for the amount of money they want to bet
bet = int(input(f"You current have ${money}, how much will you like to bet? "))

# User draws a marble from the bag
import random
while money > 0 and money > initial_money / 2:
    
    #Prevent over-betting
    if bet > money:
        bet = int(input(f"You only have ${money}, how much will you like to bet? "))

    marble = random.choice(marbles)
    rounds += 1
    if marble == 'green':
        money += bet
        if money >= target_money:
            print(f"Congratulations: You drew {marble}, and won ${bet}, you now have ${money}")
            break
        else:
            bet = int(input(f"You drew {marble}, and won ${bet}, you now have ${money}, how much will you like to bet? "))
    else:
        money -= bet
        if money > initial_money / 2:
          bet = int(input(f"You drew {marble}, and lost ${bet}, you now have ${money}, how much will you like to bet? "))
        else:
            print(f"You Lose: You drew {marble}, and lost ${bet}")
            break

print(f"You played {rounds} rounds, and you have ${money} left")
    
    