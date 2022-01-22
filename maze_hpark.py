"""
Author: Hyeonwoo Park, park1244@purdue.edu
Assignment: 10.11 - Maze
Date: 10/11/2021

Description:
    We are trying to import a turtle feature and maze image as a background.
    We are trying to move a turtle outside of the maze

Contributors:
    Hyeonwoo Park, park1244@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

from turtle import *

def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width(5)

def main():
    right(90)
    forward(10)
    left(90)
    forward(35)
    left(90)
    forward(45)
    right(90)
    forward(50)
    right(90)
    forward(25)
    left(90)
    forward(45)
    right(90)
    forward(25)
    left(90)
    forward(50)
    right(90)
    forward(48)
    left(90)
    forward(48)
    left(90)
    forward(60)
    right(90)
    forward(25)


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
