"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Sum Average
Date: 9/27/2021

Description:
    A user inputs positive numbers to continue the loop; a user input a negative
    number to end the loop and calculate how many numbers he/she has submitted
    and the average of those numbers.

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

def main():

    sum = 0
    count = 0

    while True:
        number = float(input('Enter a non-negative number (negative to quit): '))
        if number>=0:
            sum += number
            count = count + 1
            average = sum/count
            continue #continue the loop again without performing other things in loop

        elif number<0 and count >0:
            print(f'  You entered {count} numbers.')
            print(f'  Their sum is {sum:.3f} and their average is {average:.3f}.')
            break #has to break to get our of loop

        elif number<0 and count == 0:
            print('  You didn\'t enter any numbers.')
            break #has to break to get out of loop


if __name__ == '__main__':
    main()
