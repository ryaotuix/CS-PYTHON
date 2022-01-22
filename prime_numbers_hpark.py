"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Prime Numbers
Date: 10/04/2021

Description:
    Determine whether user's input number is prime or not. To stop this, user
    must input -1.

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

def is_prime(number):
    if number == 1:
        return False
    elif number ==2:
        return True
    elif number > 1:
        for i in range(2, number, 1):
            if (number%i) == 0:
                return False # return false if it is divisible by any other number besides itself
    return True

def main():
    while True:
        number = int(input('Enter a positive integer (-1 to quit): '))
        result = "" #initialize result string here
        if is_prime(number):
            result = "prime!" #if it is prime result prints prime!
        else:
            result = "not prime."#if it is not prime it prints not prime.

        if number >= 1:
            print(f'  {number} is ' + result)
            continue
        elif number -1:
            break






if __name__ == '__main__':
    main()
