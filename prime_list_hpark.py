"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Prime List
Date: 10/04/2021

Description:
    Find all prime numbers from 2 to user's input and print all of them out.

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
                return False
    return True

def main():
    limit = int(input('Enter a positive integer: '))
    primes = []
    for i in range(2, limit+1, 1): #starts with two in order to include two and exclude any number below.
    # use limit+1 to include the limit itself
        if is_prime(i):
            primes.append(i) #use .append to add elements to a list

    result = "The primes up to " + str(limit) + " are: "
    for i in primes:
        length = len(primes)

        if primes[length - 1] == i: #listname[location] == number
            result += str(i)
        else:
            result += str(i) + ", "

    print(result)








if __name__ == '__main__':
    main()
