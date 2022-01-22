"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Magic Square
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

def print_square(x):
    for i in range(3):
        print(end="  ") # Here to have two spaces every row
        for j in range(3):
            if j != 2:
                print(x[i][j], end=" ") #TO CONTINUE PRINTING IN SAME LINE
            else:
                print(x[i][j], end="")
        print("") #after, 3 column, new line!


def is_magic(l):
    # find the horizontal sum
    for row in range(0, len(l), 1):
        sum_of_row = sum(l[row]) # x[0] = [a,b,c]
        if sum_of_row != 15:
            return False

        # netted loop to find the vertical sum
        list_column = []
        for column in range(0, len(l[row]), 1): # len(x[0]) = 3
            list_column.append(l[row][column])

        sum_of_column = sum(list_column)
        if sum_of_column != 15:
            return False
        else:
            sum_of_column=0

    # find sum diagonally
    list_diagonal=[]
    list_opposite_diagonal=[] # have to check opposite diagonal
    for i in range(0, 3, 1):
        list_diagonal.append(l[i][i])
        list_opposite_diagonal.append(l[i][-(i+1)])
    if sum(list_diagonal) != 15:
        return False
    if sum(list_opposite_diagonal) != 15:
        return False


    # Find if 1-9 is all used
    list_number_used = []
    for i in range(3):
        for j in range(3):
            list_number_used.append(l[i][j])
    for num in range(1, 10, 1):
        if num not in list_number_used:
            return False

    # if all of them pass
    return True


def main():
    yes = "It is a Lo Shu magic square!"
    no = "It is not a Lo Shu magic square."
    statement = "Your square is:"

    square1=[[1,2,3],[4,5,6],[7,8,9]]
    square2=[[5,5,5],[5,5,5],[5,5,5]]
    square3=[[4,9,2],[3,5,7],[8,1,6]]
    #square3=[[4,2,9],[8,6,1],[3,7,5]]

    print(statement)
    print_square(square1)
    if is_magic(square1):
        print(yes)
    else:
        print(no)
    print("")
    print(statement)
    print_square(square2)
    if is_magic(square2):
        print(yes)
    else:
        print(no)
    print("")
    print(statement)
    print_square(square3)
    if is_magic(square3):
        print(yes)
    else:
        print(no)
    print("")

if __name__ == '__main__':
    # Do not change this part
    main()
