"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Multiples of N
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

def multiples_of(a,l = []):
    x = []
    for i in range(0, len(l), 1): # loop through the length of list
        if l[i] % a == 0:
            x.append(l[i])
    return x


def main():
    a=13 # example a
    l=[19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406] # example l
    x = multiples_of(a,l) # implement l multiples_of method
    print(f'Original list of numbers:\n  {l}')
    print(f'Numbers in the list that are multiples of {a}:\n  {x}')







if __name__ == '__main__':
    # Do not change this part
    main()
