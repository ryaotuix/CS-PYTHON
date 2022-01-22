"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Roll Analysis
Date: 10/25/2021

Description:
    Have functions that generate random rock paper or scissor and get user input,
    and decide who is the winner. Build a main function to play rock paper scissors.

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

def roll_d6():
    x = r.randint(1,6) # use rand int to generate rand int
    return x

def get_2d6_rolls(rolls):
    x=[]
    for i in range(rolls):
        a=roll_d6()
        b=roll_d6()
        x.append(a+b)
    return x

def main():
    rolls = 1000000 # but we can test with smaller numbers
    l = get_2d6_rolls(rolls)
    print('Roll  Frequency')
    for i in range(2,13,1): #
        count = l.count(i)
        frequency = count/len(l)*100
        print(f'{i:3}    {frequency:5.2f}%') # width and decimal places





if __name__ == '__main__':
    # Do not change this part
    main()
