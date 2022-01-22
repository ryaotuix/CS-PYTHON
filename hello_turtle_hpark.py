"""
Author: Hyeonwoo Park, park1244@purdue.edu
Assignment: 10.11 - Hello Turtle
Date:10/11/2001

Description:
    Make a star pattern shape according to user's input of how many edges There
    are

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
    setup(600, 400)
    width(9)


def draw_e():
    pendown()
    left(90)
    penup()
    forward(30)
    pendown()
    right(90)
    forward(60)
    penup()
    backward(30)
    circle(30, 340)


def draw_h():
    """Write this function."""
    penup()
    setheading(90)
    forward(50)
    pendown()
    



def draw_l():
    """Write this function."""


def draw_o():
    """Write this function."""


def draw_r():
    """Write this function."""


def draw_t():
    """Write this function."""


def draw_u():
    """Write this function."""


def main():
    """After these lines, use your letter drawing functions
    to write code that will draw the words "hello turtle".
    """


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
