from random import randint
# Get validated integer bounds from the user
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
# Make sure low <= high
if low > high:
    low, high = high, low
# Generate a random number
number = randint(low, high)
#The user can now input a guess to the amount of tries it will take them to guess the number
amount_of_tries = int(input("Enter the amount of tries you want to guess the number: "))
realamount_of_tries = 0
# User guesses a number
guess = int(input(f"Guess a number between {low} and {high}: "))
while number != guess:
    if number == guess:
        print("You got it!")
    elif number > guess:
        print("Too low!")
        guess = int(input("Guess again: "))
        realamount_of_tries += 1
    else:
        print("Too high!")
        guess = int(input("Guess again: "))
        realamount_of_tries += 1
print("You guessed the number!")
# Check if the user guessed the number in the desired amount of tries
if amount_of_tries == realamount_of_tries:
    print("You guessed the number in the amount of tries you wanted!")
else:
    print("You did not guess the number in the amount of tries you wanted.")
print(f"The number was {number}")
