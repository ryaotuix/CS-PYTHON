"""
Author: Hyeonwoo Park, park1244@purdue.edu
Assignment: 10.11 - Star Pattern
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
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

def main():
    side_length = 60
    color('black', 'pink')
    points = int(input("How many points do you want on a star?"))
    a = 360/points # inner angle
    b = 2*a # concave angle
    if points == 5:
        setheading(-((180-a)/2 + b - 180)) # formula figured out for if point is 5
    elif points == 8:
        setheading(360-(b-180)/2) # formula figured out for if point is 8
    elif points == 13:
        setheading(-(360-(b-180)/2)) # formula figured out for if point is 13
    begin_fill()
    for i in range(points):
        forward(side_length)
        left(180-a)
        forward(side_length)
        right(180-b)
    end_fill()




# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
