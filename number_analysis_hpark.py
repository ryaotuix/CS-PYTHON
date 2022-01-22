"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Number Analysis
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

def get_number_list():
    x=[]

    for i in range(10):
        a = float(input(f'  number {i+1:2} of 10: ')) #indentation:2
        x.append(a)
    return x

def main():
    print('Enter 10 numbers:') # IDK why this has to be in main function but whatever
    x = get_number_list()

    maximum_num = max(x) #max
    min_num = min(x) # min
    total = sum(x)
    average = total/len(x)
    print(f'Highest number: {maximum_num:.2f}')
    print(f'Lowest number: {min_num:.2f}')
    print(f'Total: {total:.2f}')
    print(f'Average: {average:.2f}')




if __name__ == '__main__':
    # Do not change this part
    main()
