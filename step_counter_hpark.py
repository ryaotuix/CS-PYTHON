"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Number Reader
Date: 11/13/2021

Description:
    Read a file we made last time, find statistics of it (min, max, etc.)
    Be aware of the formatting!

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

def read_file():
    l = []
    with open('state_capitals.txt') as fo:
        for line in fo:
            l.append(int(line.rstrip()))
    l.sort() # sorted to find min and max by not usng the method
    return l



def main():
    l = read_file()
    min = l[0]
    max = l[-1]
    total = sum(l) # cannot use sum as name of object
    line = len(l)
    avg = total/line
    print(f'{line:,} numbers were read from the file.') # to format :, !
    print(f'Min: {min:,}')
    print(f'Max: {max:,}')
    print(f'Sum: {total:,}')
    print(f'Avg: {avg:,.1f}')





if __name__ == '__main__':
    # Do not change this part
    main()
