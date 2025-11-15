#importing random module for questions
import random

from random import randint

#defining the questions and answers
questionlist = [
    ["What function do I use for showing something on a terminal? ", ["Print", "print", "print()"]],
    ["In code, what symbol is used to assign a value to a variable? ", ["=", "equals", "equal sign"]],
    ["What is the most commonly used programming language? ", ["Python", "python"]],
    ["Name one of the main loops in python ", ["for", "For", "while", "While"]],
    ["True/False: An if statement needs an else statement ", ["False", "false"]],
    ["How many variables can I have in a program?", ["As many as I want ", "As many as I want", "unlimited", "unlimited", "infinite", "infinite", "countless", "countless", "no limit", "no limit"]],
    ["What keyword is used to define a function in Python? ", ["def", "Def"]],
    ]

#tracking which questions have been done
question_done = [False, False, False, False, False, False, False]
#game setup function
def setup():
    print("--------------------------------------")
    print()
    print("This is the Adventure of 0s and 1s!")
    print()
    print("--------------------------------------")
    print("In a world where everything is made of code,")
    print("two brave characters, 0 and 1, embark on a quest")
    print("to find the legendary 'Bug-Free Code'.")
    print("Join them as they navigate through loops")
    print("and functions to achieve their goal!")
    print("--------------------------------------")
    print("You will be given a coding challenge to solve.")
    print("A correct solution will bring you closer to finding clues")
    print("A wrong solution will lead you nothing but danger.")
    print("--------------------------------------")
    print("Good luck on your quest!")
    print("--------------------------------------")
    print("You have 10 lives to start with.")
    print("For each wrong answer, you will lose a life.")
    print("Once you get to 7 lives, the monster of bugs will catch you with their seven swords!")
    print("--------------------------------------")
#initializing lives and question count
lives = 10

questioncount = 0
#calling setup function
setup()
#defining answer checking function
def checkanswer(questiontext):
    #getting user answer
    answer = input(questiontext)
    global lives
    global questioncount
    #checking if answer is correct
    if (answer in questionlist[questionnumber][1]):
        print("Correct!")
        questioncount += 1
        if questioncount > 7:
            print("Congratulations! You have completed the quest!")
            return True
    else:
        lives -= 1
        print("Wrong! You have " + str(lives) + " lives left.")
        return False

#main game loop
while 7 < lives <= 10:
    if questioncount >= 7:
        break  
    #selecting a random question that hasn't been asked yet
    questionnumber = int(randint(0, 6))
    while(question_done[questionnumber]):
        questionnumber = int(randint(0, 6))

    question_done[questionnumber] = True
    question = questionlist[questionnumber][0]
    checkanswer(question)

#end of game messages
if lives <= 7:
    print("Oh no! The monster of bugs has caught you!")
    print("Better luck next time!")
else:
    print("You have successfully completed the quest!")
