"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Phone Number Converter
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


def convert_number(x):
    list_of_words = x.lower().split('-') # split and make it to list
    result = [] # add into this list
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' ,'v', 'w', 'x', 'y', 'z']

    for i in range(len(list_of_words)):
        word = list_of_words[i] #each word in the list
        to_digit = []
        for j in range(len(word)):
            conversion = ''
            if (word[j] in alphabets[0:3]):
                conversion = '2'
            elif (word[j] in alphabets[3:6]):
                conversion = '3'
            elif (word[j] in alphabets[6:9]):
                conversion = '4'
            elif (word[j] in alphabets[9:12]):
                conversion = '5'
            elif (word[j] in alphabets[12:15]):
                conversion = '6'
            elif (word[j] in alphabets[15:19]):
                conversion = '7'
            elif (word[j] in alphabets[19:22]):
                conversion = '8'
            elif (word[j] in alphabets[22:]):
                conversion = '9'
            else:
                conversion = word[j]
            to_digit.append(conversion)
        result.append(''.join(to_digit))

    return '-'.join(result)

def main():
    x = convert_number(input('Enter a telephone number: '))
    print(f'The phone number is {x}')


if __name__ == '__main__':
    # Do not change this part
    main()
