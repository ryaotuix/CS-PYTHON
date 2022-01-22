"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Rainfall
Date: 9/27/2021

Description:
    User inputs number of years and corresponding rainfall for each months. Given
    those values, the code generates number of months and average rainfall

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
    years = int(input('Enter the number of years: '))
    countMonth = 0
    total = 0

    if years<=0:
        print('Invalid input.')

    else:
        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for year_num in range(1, years + 1, 1):
            print(f'  For year No. {year_num}')
            for month_name in month:# iterate in array!!!! use month instead of range
                while True:
                    rainfall = float(input(f'    Enter the rainfall for {month_name}.: '))

                    if rainfall>=0:
                        total += rainfall
                        break
                    else: #this is unncesarilly
                        print('    Invalid input, please try again.')



        print(f'There are {12 * years} months.')
        print(f'The total rainfall is {total:.2f} inches.')
        print(f'The monthly average rainfall is {total/(12 * years):.2f} inches.')


if __name__ == '__main__':
    main()
