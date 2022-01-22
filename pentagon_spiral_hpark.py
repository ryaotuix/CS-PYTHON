"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Pentagon Spiral
Date: 10/10/2021

Description:
    Draw a pentagon extension! We are given that length of the pentagon increases
    as we go through the shape

Contributors:
    Harrison Park, park1244@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
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
color('black')


def start():
    setup(564, 564)
    width(5)

def main():
    len = 8 # initialize initial length as 8 outside of loop
    for i in range (1, 34, 1):
        forward(len)
        len += 8 # for each loop add 8 to the length
        left(72) # then shift its angle 72 degree left


if __name__ == '__main__':
    start()
    main()
    done()
