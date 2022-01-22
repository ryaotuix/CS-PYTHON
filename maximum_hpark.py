"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Maximum
Date: 10/04/2021

Description:
    Compare two integers and return the greater integer out of two.

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



def max_of_two(a, b):
    max = a #Assume a is bigger always
    if (a < b): #if a is smaller then b is max
        max = b
    return max

def main():
    a = input('Enter the first integer: ')
    b = input('Enter the second integer: ')
    max = max_of_two(a, b)
    print(f'The number {max} is greater.')



if __name__ == '__main__':
    main()
