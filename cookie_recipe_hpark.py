"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Cookie recipe
Date: 9/12/2001

Description:
    Calculate the number of cups of sugar and butter and flour according to the
    number of cookies I want to make, given that 48 cookies require 1.75, 1, and
    2.5 respectively.

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
#Cookies = number of cookies I want to make
#Sugar = number of cups of sugar I need to make certain number of cookies
#Butter = number of cups of butter I need to make certain number of cookies
#Flour = number of cups of flour I need to make certain number of cookies
def main():

    Cookies = float(input('How many cookies do you want to make? '))
    print('To make '+ str(int(Cookies)) + ' cookies, you will need:')

    Sugar = float(1.75*Cookies/48)

    Butter = float(Cookies/48)

    Flour = float(2.5*Cookies/48)

    print(format(Sugar,'7,.2f'),'cups of sugar')
    print(format(Butter,'7,.2f'),'cups of butter')
    print(format(Flour,'7,.2f'),'cups of flour')

if __name__ == '__main__':
    main()
