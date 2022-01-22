"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Capital Quiz
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

def get_state_data():
    l = [] # create a list
    with open('state_capitals.txt') as fo:
        for line in fo:
            l.append((line.rstrip().split(', '))) # strip to get rid of right side

    # now, l has each object [capital, state]

    list_of_tuples = [] # [(key1, value1), (key2, value2)...]

    for i in range(0, len(l), 1):
        t = (l[i][1], l[i][0]) #key as state  #value as capital
        list_of_tuples.append(t)

    dic = dict(list_of_tuples) # create dictionary

    return dic




def main():
    #asking to enter capital (value) for particular state (key)

    dic = get_state_data()


    num_question = 0
    num_correct = 0

    while len(dic) > 0:
        list_of_items = list(dic.items()) # return list of items in tuple in random order
        r.shuffle(list_of_items)
        #(key:state, value:capital)
        answer = input('What is the capital of ' + list_of_items[0][0] + ' (enter 0 to quit)? ')


        if answer == '0':
            break

        if answer.lower() == list_of_items[0][1].lower():
            del dic[list_of_items[0][0]]
            num_correct += 1
            print('  That is correct!')
        else:
            print('  That is incorrect.')
            print(f'  The capital of {list_of_items[0][0]} is {list_of_items[0][1]}.')
        num_question += 1


    print(f'You answered {num_correct} out of {num_question} questions correctly.')


if __name__ == '__main__':
    # Do not change this part
    main()
