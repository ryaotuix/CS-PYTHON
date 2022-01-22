"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Math Quiz
Date: 10/18/2021

Description:
    Generate two random numbers and ask user the result of the sum. If it is correct,
    say correct and if it is not, tell them actual result.

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

import random as r

def random_number(i):
    if i==2:
        x = r.randint(10, 99)
        return x
    elif i==3:
        x = r.randint(100,999)
        return x

def main():
    x=random_number(2) #WHy gradescopes want this
    y=random_number(3) #in 2 and 3 woww
    z=x+y
    print(f'{x:5}') #How to use printf in python
    print(f'+ {y:3}')
    print('-----')
    a = int(input('= ')) #input is string in python
    if a==z:
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {z}.')








if __name__ == '__main__':
    main()
