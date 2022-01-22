"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Roulette Colors
Date: 9/19/2001

Description:
    Determine the color of pocket ball depending on the pocket number where Pocket
    number varies between 0 to 36. We will print 'Invalid Input!' if the number
    does not fit in the range.

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

    color = float(input('Please choose a pocket number: '))
    if color<0: #first case scenario
        print('  Invalid Input!')

    elif int(color)==0: #second case scenario
        print('  Pocket number',str(int(color)),'is green.')

    elif int(color)<=10 and int(color)%2 == 1: #third case scenario
        print('  Pocket number',str(int(color)),'is red.')

    elif int(color)<=10 and int(color)%2 == 0: #fourth case scenario
        print('  Pocket number',str(int(color)),'is black.')

    elif int(color)<=18 and int(color)%2 == 1: #fifth case scenario
        print('  Pocket number',str(int(color)),'is black.')

    elif int(color)<=18 and int(color)%2 == 0: #sixth case scenario
        print('  Pocket number',str(int(color)),'is red.')

    elif int(color)<=28 and int(color)%2 == 1:
        print('  Pocket number',str(int(color)),'is red.')

    elif int(color)<=28 and int(color)%2 == 0:
        print('  Pocket number',str(int(color)),'is black.')

    elif int(color)<=36 and int(color)%2 == 1:
        print('  Pocket number',str(int(color)),'is black.')

    elif int(color)<=36 and int(color)%2 == 0: 
        print('  Pocket number',str(int(color)),'is red.')

    else:
        print('  Invalid Input!')


if __name__ == '__main__':
    main()
