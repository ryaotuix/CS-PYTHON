"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Rock, Paper, Scissors
Date: 10/18/2021

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
import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    a = random.choices(options)[0]
    return a

def main():
    win_message = 'You won the game!'
    lose_message = 'You lost.  Better luck next time.'
    tie_message = "Its a tie. Starting over."
    exit_message = 'Thanks for playing.'
    while True:
        comchoice = get_computer_choice()
        yourchoice = input('Choose rock, paper, or scissors: ')
        if yourchoice == comchoice:
            print(f'The computer chose {comchoice}, and you chose {yourchoice}.')
            print(tie_message)
            continue
        elif yourchoice == 'rock':
            print(f'The computer chose {comchoice}, and you chose {yourchoice}.')
            if comchoice == 'paper':
                print('paper beats rock')
                print(lose_message)
            elif comchoice == 'scissors':
                print('rock beats scissors')
                print(win_message)
            break
        elif yourchoice == 'paper':
            print(f'The computer chose {comchoice}, and you chose {yourchoice}.')
            if comchoice == 'scissors':
                print('scissors beats paper')
                print(lose_message)
            elif comchoice == 'rock':
                print('paper beats rock')
                print(win_message)
            break
        elif yourchoice == 'scissors':
            print(f'The computer chose {comchoice}, and you chose {yourchoice}.')
            if comchoice == 'rock':
                print('rock beats scissors')
                print(lose_message)
            elif comchoice == 'paper':
                print('scissors beats paper')
                print(win_message)
            break
        else:
            print('You made an invalid choice. Please try again.')
            continue #not necessary

    print(exit_message)



if __name__ == '__main__':
    main()
