"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Vowels
Date: 10/24/2021

Description:
    Find all prime numbers from 2 to user's input and print all of them out.

Contributors:
    Harrison Park, park1244@purdue.edu [repeat for each]

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


def draw_a():
    """Complete this function to draw the character a."""
    penup()
    setheading(90)
    forward(30)
    setheading(270)
    pendown()
    circle(30,540)
    forward(30) #
    left(180)
    forward(60) #
    penup()
    right(90)
    forward(60)
    right(180)

def draw_e():
    """Complete this function to draw the character e."""
    penup()
    setheading(90)
    forward(30)
    setheading(0)
    pendown()
    forward(60) #
    left(90)
    circle(30,315)
    penup()
    circle(30,195)
    forward(30)
    right(180)

def draw_i():
    """Complete this function to draw the character i."""
    penup()
    setheading(0)
    forward(30) #
    pendown()
    left(90)
    forward(60) #
    penup()
    forward(30) #
    pendown()
    dot(9)
    penup()
    left(180)
    forward(90) #
    right(90)
    forward(30)
    right(180)

def draw_o():
    """Complete this function to draw the character o."""
    penup()
    setheading(0)
    forward(30)
    pendown()
    circle(30.360)
    penup()
    left(180)
    forward(30) #
    right(90)
    forward(60) #
    right(180)
    forward(60)
    setheading(0)

def draw_u():
    """Complete this function to draw the character u."""
    penup()
    setheading(90)
    forward(60) # r=30
    pendown()
    left(180)
    forward(30) # r=30
    circle(30,180) # r=30
    setheading(90)
    penup()
    forward(30) # r=30
    pendown()
    left(180)
    forward(60) # r=30
    setheading(180)
    penup()
    forward(60)
    setheading(0)

def square():
    goto(-220, -30)
    setheading(0)
    pendown()
    for i in range(4):
        forward(60)
        left(90)
    penup()

def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this for your own testing."""
    pass


if __name__ == '__main__':
    # Do not change this part
    start()

    draw_u()
    done()
