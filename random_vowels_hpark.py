"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Random Vowels
Date: 10/18/2021

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

# Import additional modules below this line.
import vowels as v
import random as r
# Write new functions below this line (starting with unit 4).


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
    """Write your mainline logic here."""
    a = v.draw_a
    e = v.draw_e
    i = v.draw_i
    o = v.draw_o
    u = v.draw_u
    vowel_list = [a,e,i,o,u]
    x = -220
    r.shuffle(vowel_list)
    for i in vowel_list:
        pendown()
        i()
        x += 80
        penup()
        goto(x, -30)
        pendown()
        setheading(0)
        penup()




if __name__ == '__main__':
    # Do not change this part
    start()
    main()
    done()
