import random
print("")
print("Welcome to Number guessing game")
print("          Rules          ")
print("* You have only 5 chance to Guess a number (between 1 to 9)")
number = int(random.randint(1, 9))
Number = int(10)
chance = 0
while chance < 5:
    print("")
    if chance < 5:
        print("You have",5-chance,"chance left")
    else:
        print("You don't have any chance")
    guess = input("  Enter your guess:- ")
    chance += 1
    if guess.isnumeric() == False:
        if chance < 5:
            print("Don't enter a string. Enter a number (between 1 to 9)")
        else:
            print("You lose!!! because your chance is over and you have entered a string")
    elif not int(guess) < Number:
        if chance < 5:
            print("Please enter a number (between 1 to 9)")
        else:
            print("You lose!!! because your chance is over and you haven't entered a number (between 1 to 9)")
    else:
        if int(guess) < number:
            if chance < 5:
                print("Your guess was too low: Guess the number higher than",guess)
            else:
                print("You lose!!! The number was",number,"and you had chosen",guess)
        elif int(guess) > number:
            if chance < 5:
                print("Your guess was too high: Guess the number lower than",guess)
            else:
                print("You lose!!! The number was",number,"and you had chosen",guess)
        else:
            print("You win!!! The number was",number,"and you had chosen",guess,"in",chance)
            break

