"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Pig Latin
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


def pig(x):
    list_of_words = x.split() # split and make it to list
    result = [] # add into this list
    for i in range(len(list_of_words)):
        word = list_of_words[i] #first word in the list
        first_char = list_of_words[i][0] # first char in each word
        formatted_word = word[1:] + first_char + 'ay'
        result.append(formatted_word)

    return ' '.join(result).capitalize()




def main():
    x = pig(input('Enter a string: '))
    print(f'Pig latin: {x}')


if __name__ == '__main__':
    # Do not change this part
    main()
