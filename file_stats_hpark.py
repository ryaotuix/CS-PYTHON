"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - File Stats
Date: 11/05/2021

Description:
    Change a string with the given description

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


def num_words_file(x):
    total_words = 0
    for line in x:
        l = line.split() # why not split(' ')????
        total_words += len(l)
    return total_words


def num_lines_file(x):
    l = x.readlines() # ez
    return len(l)



def main():
    with open('frontiero_v_richardson.txt') as fo:
        total_words = num_words_file(fo)
    with open('frontiero_v_richardson.txt') as fo:
        num_lines = num_lines_file(fo)

    avg_words = total_words / num_lines # remember you don't have to make another funtion for this

    print(f'Total number of words: {total_words}')
    print(f'Total number of lines: {num_lines}')
    print(f'Average number of words per line: {avg_words:.1f}')



if __name__ == '__main__':
    # Do not change this part
    main()
