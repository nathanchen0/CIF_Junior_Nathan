# CIF_Junior_Nathan
This is the entire work from Nathan for CIF Junior 2025 - 2026


# Week 3
## Advanced guessing game!
1. Added multiple tries
2. Added small hints to make it easier
3. Added an input so the user can set the lower and upper bound
4. Added an extra guess about the number of tries it would take to guess the number

## What does the game look like?
<img width="1147" height="220" alt="image" src="https://github.com/user-attachments/assets/b7e93dc4-513a-4fa2-92a3-79bea5f6ef0b" />

## How can you make a game like this?
1. Install VSCode on your device
2. Add a Python Compiler and Debugger
3. Optional but very useful, Take Free Lesson at CIF to learn more about python!
4. Have Fun!


# Week 4
## 2D lists!
1. We learned about how 2D lists work

I made a weather database that allows people to find the low, high and the conditions of a day using 2D lists. Check weather in week 4 to see the code.

# Starting up a TBAG (Text Based Adventure Game)
We started our first TBAG! This uses questions of some sort to make an adventure game.

Mine is called "The Adventure of 0s and 1s" and it is a code related game with questions that the user will have to answer.

When I print the instructions, I use my own function called setup() which allows me to print it whenever I want to without another chunk of text.

# Week 5
Now that we had our plan out, we got our next class learning about how to make our TBAGs more fun!
1. Using 2D lists, we stored our questions and answers (This makes our code more simple and easy to access)
2. We added function to check answers from the user so that the game is more interactive
3. We also added a list to make sure that no question are repeated
4. I used the randint function and another list to choose questions

Go to week5, tbag2.py to see my game code.

# Week 6

For class 6, we learned about turtle (my favourite)!
We learned about the general command like turtle.forward() and how to move the turtle. Here are some other things we learned:

1. turtle.penup() and turtle.pendown() - lifts the pen or puts the pen down
2. turtle.shape(), turtle.color() - the turtle customization
3. turtle.begin_fill(), turtle.end_fill() - fill blocks of drawings

We drew fireworks, a starting project for doing turtle. We drew the first part of the firework, the box and the rising explosion line.
<img width="800" height="711" alt="Screenshot 2025-11-21 at 9 42 07 PM" src="https://github.com/user-attachments/assets/61877a61-3c39-4abf-b41b-c85a337de20d" />

All of the week 6 code on turtle and fireworks are in the week6 folder

# Week 7
Continuing off of our last weeks work, we learned about advanced turtle functions.

For example, we learned about:
1. Cloning turtle with turtle.clone()
2. Advanced loops and loops in loops
3. Changing turtle delay and speed

Using these skills, we made an advanced firework drawing. Check mine out in the week7 folder.
<img width="874" height="753" alt="image" src="https://github.com/user-attachments/assets/c1b34db6-31dc-4f79-badb-2ae0197992b5" />

We also created a fancy shape! We used a lot of repeatedly drew a shape and turned to make a cool pattern.

Mine is like a wormhole and is a winding circle. My code is all in the week7 folder.
<img width="834" height="730" alt="image" src="https://github.com/user-attachments/assets/0af48045-b29c-49a7-9c51-71cb2ea47778" />
# Week 8
For week 8, we learned about pygame. For the first homework, we brainstormed how to do simple things in pygame.

Moving a box

First way

1. Draw a box on the screen
2. Move each point of the box to the right to move it

Second way

1. Draw a box on the screen
2. Remove it and draw another one slightly to the right quickly

Homework two: brainstorm some ideas for the game

My idea is tetris

I can use:
1. Randint to choose random blocks
2. Use some kind of moving box to move the shape down
3. Allow some kind of control of the blocks from the player
4. Decide when the game is lost


# Week 9
Now we learned one of the most important skills of Pygame: moving a box.

By very quickly flashing a square that is to the direction of the original box, it looks like the box is moving.

We tried to make a green box and a purple box move in opposite directions as practice. My code can be found in the week9 folder.

# Week 10
To finish off 2025, we made another improvement to our box movement. Firstly, we made our movement smoother and added a boundary to the box.

By adding the position of the box with the box dimensions and checking if it is larger than the screen, we can add a boundary to the box.

    if box_x + boxwidth > width:
        box_x = width - boxwidth
    if box_x < 0:
        box_x = 0
    if box_y + boxheight > height:
        box_y = height - boxheight
    if box_y < 0:
        box_y = 0

We also added a system to allow for diagonal movement and a transition to horizontal or vertical movement.
1. We add an event check to see if the user has lifted up W, A, S, or D
2. We check if the user lifted A or D (If so, we set the x movement to 0)
3. We check if the user lifted W or S (If so, we set the y movement to 0)

elif event.type == pygame.KEYUP:

    if event.key == pygame.K_d or event.key == pygame.K_a:
    
        box_x_change = 0
        
    if event.key == pygame.K_w or event.key == pygame.K_s:
    
        box_y_change = 0

We also did an optional challenge of changing colour every 2 seconds as a decoration.
colour_change_event = pygame.USEREVENT + 1

pygame.time.set_timer(colour_change_event, 2000)  # Change colour every 2 seconds

                            .....

elif event.type == colour_change_event:
    box_colour = random.choice(colour_list)

# Week 11 (Right before Christmas yay!)

We learned about the collision detecting feature in pygame using colliderect.

if rect1.colliderect(rect2):

    print("Collision detected!")

We also made a little game with this new function. When the box collides, it prints "collision detected" and the box changes colour.

<img width="790" height="806" alt="image" src="https://github.com/user-attachments/assets/2cbb0eab-7015-4b32-a1a3-8641c7420cad" />


<img width="790" height="814" alt="image" src="https://github.com/user-attachments/assets/840a33cb-3a75-4b72-9694-7dde5b39e80d" />

# Week 12

In week 12, we started to make our first pygame! 

I wanted to make a real maze that requires the player to carefully not touch the barriers and make their way to the end.

In order to make mazes, I used numbers that each represented a part of the maze. (a 1 is a wall, 0 is a space, 3 is the player, and 2 is the finish)

Credits to https://electronstudio.github.io/pygame-zero-book/chapters/maze.html for the idea! Thank You!

1. With these long string of numbers, I can use the len() function to find out what each number is and find their location.
2. I then do the smae old program with the moving box
3. I also make sure that if the box contacts the finish line, it is a win
4. And add a line that if the player touches the walls, they lose
<img width="805" height="822" alt="image" src="https://github.com/user-attachments/assets/c038103d-e5ff-4fca-90b4-8955d273a135" />

Check my week12 folder for the code!
