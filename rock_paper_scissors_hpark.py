"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Rock Paper Scissors
Date: 10/18/2021

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
import random
# message contents
win_message = '  You won the game!'
lose_message = '  You lost.  Better luck next time.'
tie_message = "  Its a tie. Starting over."
exit_message = 'Thanks for playing.'
# get computer choice with arrays
def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    a = random.choices(options)
    answer = ""
    for ele in a:
        answer += ele
    return answer
# get player choice until it has valid input
def get_player_choice():
    b = input('Choose rock, paper, or scissors: ')
    while b != 'rock' and b != 'paper' and b != 'scissors':
        print('You made an invalid choice. Please try again.')
        b = input('Choose rock, paper, or scissors: ')
    return str(b)
# get winner based on computer and plyaer choice
def get_winner(c, p):
    if p == c:
        return 'tie'
    elif p == 'rock':
        if c == 'paper':
            return 'computer'
        elif c == 'scissors':
            return 'player'
    elif p == 'paper':
        if c == 'scissors':
            return 'computer'
        elif c == 'rock':
            return 'player'
    elif p == 'scissors':
        if c == 'rock':
            return 'computer'
        elif c == 'paper':
            return 'player'


def main():
    while True:
        c = get_computer_choice()
        p = get_player_choice()
        w = get_winner(c, p)
        print(f'  The computer chose {c}, and you chose {p}.')

        if w == 'player':
            print(f'  {p} beats {c}')
            print(win_message)
            break
        elif w == 'computer':
            print(f'  {c} beats {p}')
            print(lose_message)
            break
        else:
            print(f'{tie_message}\n')


    print(exit_message)



if __name__ == '__main__':
    main()
