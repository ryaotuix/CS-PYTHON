"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Organisms
Date: 9/27/2021

Description:
    A user inputs initial population in million and average daily increase in
    percent and number of days to multiply. The code prints the table that shows
    day and approximate population for corresponding day.

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

    population = float (input('Starting number, in million: '))
    percentage = float (input('Average daily increase, in percent: '))/100#divided by 100 for percentage
    day = int (input('Number of days to multiply: '))
    print('Day   ' + 'Approx. Pop')

    for i in range(0, day+1, 1): #use!! day+1 
        print(f'{i:3}   {population:11.4f}')
        population = population*(1 + percentage)



if __name__ == '__main__':
    main()
