"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Leap Year
Date: 9/19/2001

Description:
    Determine whether if the input year is a leap year or not from the information
    that says if it is divisible by 100 then check if it is divisible by 400.
    If it is, or if it is divisible by 4, it is leap year.

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

    year = int(input('Please input a year: '))

    if year%100 == 0: #first case scenario
        if year%400 == 0: #1-1 case scenario
            print('In the year', str(year) + ', ' + 'February has 29 days.')
        else: #1-2 case scenario
            print('In the year', str(year) + ',','February has 28 days.')
    elif year%4 == 0: #second case scenario
        print('In the year', str(year) + ', ' + 'February has 29 days.')
    else: #thrid case scenario
        print('In the year', str(year) + ',','February has 28 days.')



if __name__ == '__main__':
    main()
