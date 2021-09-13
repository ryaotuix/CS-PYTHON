"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Interest
Date: 9/12/2001

Description:
    Calculate the interest in $ given that P (initial amount), r (annual interest rate),
    n (number of times per year that the interest is compounded), and t (number of years)

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

# FV = the amount of money in the account after the specified number of years
# P = the principal amount that was originally deposited into the account
# r = annual interest rate
# n = number of times per year that the interest is compounded
# t = number of years

    print('Please enter the following quantities.')

    P = float(input('  How much is the initial deposit? '))

    r = float(input('  What is the annual interest rate in percent? '))

    n = float(input('  How many times per year is the interest compounded? '))

    t = float(input('  How many years will the account earn interest? '))

    FV = P*(1+(r/100)/n)**(n*t)

    print('\n'+'At the end of', format(t,'2,.1f'), 'years, this account will be worth $' + format(FV, '2,.2f') + '.')

if __name__ == '__main__':
    main()
