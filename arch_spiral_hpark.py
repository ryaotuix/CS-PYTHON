"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Arch Spiral
Date: 10/18/2021

Description:
    Draw arch spiral with the given Cartasian x and y coordinates

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
import math

# Import additional modules below this line.


# Write new functions below this line (starting with unit 4).


def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    width('5')


def main():
    """Write your mainline logic here."""

    for deg in range(0, 6*360+1, 1):
        rad = deg * math.pi/180
        x = deg/(math.pi**float(2))*math.cos(rad)
        y = deg/(math.pi**float(2))*math.sin(rad)
        goto(x,y)






if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
