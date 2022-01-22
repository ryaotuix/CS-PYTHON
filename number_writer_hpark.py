"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Number Writer
Date: 11/05/2021

Description:
    Asks user how many random integers he wants to print in a new file.
    Then, write it in a new file.

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

def random_number():
    x = r.randint(1019,1215) # randomly generate integer in bound
    return x



def main():
    num = input('How many numbers would you like? ')

    with open('random_numbers.txt', 'w') as fo:
        for i in range(0,int(num), 1):
            x = random_number()
            fo.write(str(x))
            if i != int(num) -1: # last line should not have extra empty line
                fo.write('\n') # only ohters





if __name__ == '__main__':
    # Do not change this part
    main()
