"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Arrows
Date: 9/27/2021

Description:
    ask user how many arrows he/she wants to draw and print certain amount of
    arrows increasing its length gradually.

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

def main():

    arrows = int(input('How many arrows should I draw? '))
    for i in range(0, arrows, 1): #it can be expressed as range(arrows) too
        print('<',end='') #end'' allows you to print in the same line
        for j in range(0,i):
            print('-',end='')
        print('>')

if __name__ == '__main__':
    main()
