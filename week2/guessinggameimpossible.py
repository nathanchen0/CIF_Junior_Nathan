from random import randint
#use randint to make a number guessing game
number = randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
#the user guesses a number and the program tells them if they guessed correctly
if number == guess:
    print("You guessed the number!")
else:
    print("you failed")

print("The number was", number)
