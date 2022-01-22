"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Avg Grade
Date: 10/04/2021

Description:
    A user inputs grades and according to them, this program tells the letter
    grade of each and the averge letter grade with average score.

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

def get_valid_score():
    while True:
        score = float(input("Enter a score: "))
        if (score < 0 or score > 100):
            print("  Invalid Input. Please try again.")
            continue #skip other parts of while loop and repeat
        elif (score>=0 and score <=100):
            print(f'  The letter grade for {score:.1f} is {determine_grade(score)}.')
            return score #return and get out of the loop

def calc_average(scores):
    total = sum(scores)
    average = total/len(scores)
    return average

def determine_grade(score):
    if (score<64):
        return 'F'
    elif (score<73): # no need to state and bigger than 64 bc it is stated above
        return 'D'
    elif (score<82): # no need to state and bigger than 73 bc it is stated above
        return 'C'
    elif (score<91): # no need to state and bigger than 82 bc it is stated above
        return 'B'
    return 'A' # no need to say else

def main():
    score1 = get_valid_score()
    score2 = get_valid_score()
    score3 = get_valid_score()
    score4 = get_valid_score()
    score5 = get_valid_score()

    scores = [score1, score2, score3, score4, score5] #make a list of five scores

    print("")
    print('Results:')
    print(f'  The average score is {calc_average(scores):.2f}.')
    print(f'  The letter grade for {calc_average(scores):.2f} is {determine_grade(calc_average(scores))}.')




if __name__ == '__main__':
    main()
