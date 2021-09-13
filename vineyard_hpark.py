"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Vineyard
Date: 9/12/2001

Description:
    Calculate numbers of Vineyard with the given variables: R
    (length of the row), E (amount of space in meters by an end-post assembly),
    and S (space between vines)

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
# V = number of groupvines that will fit in the row
# R = Length of the row in meters
# E = amount of space in meters used by an end-post assembly
# S = space between vines in meters.

def main():

    print('Enter each of the following quantities in meters.')

    S = float(input('  How much space should be between the vines? '))

    E = float(input('  How wide is the end-post assembly? '))

    R = float(input('  How long is this row? '))

    V = int((R - 2*E)//S)

    print('\n''This row has enough space for '+ str(max(0,V)) + ' vine(s).')

if __name__ == '__main__':
    main()
