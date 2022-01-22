"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - World Series
Date: 11/13/2021

Description:
    Read a file we made last time, find statistics of it (min, max, etc.)
    Be aware of the formatting!

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

def load_winners_data():

    l = []
    with open('WorldSeriesWinners.txt') as fo:
        for line in fo:
            l.append((line.rstrip()))

    # dic 1 = keys:teams  values: number of win
    teams = list(set(l)) #make a list of unique teams
    list_of_tuples = []
    for i in range(len(teams)):
        team = teams[i]
        wins = l.count(team)
        t = (team, wins)
        list_of_tuples.append(t)
    dic_1 = dict(list_of_tuples)


    years = []
    for i in range(1903, 2021, 1):
        years.append(i)
    years.remove(1904)
    years.remove(1994)
    # made a list for correct years
    dic_2 = dict(zip(years,l))
    


    return dic_1, dic_2




def main():
    dic_1, dic_2 = load_winners_data()

    items1 = list(dic_1.items())
    items2 = list(dic_2.items())

    year = int(input('Enter a year in the range 1903 -- 2020: ')) # have to change it to integer
    if year in dic_2.keys():
        win_team = dic_2[year]
        print(f'  The {win_team} won the World Series in {year}.')
        print(f'  They have won the World Series {dic_1[win_team]} times.')
    elif year == 1904 or year == 1994: # if the year when the world series wasn't played
        print(f'  The World Series wasn\'t played in the year {year}.')
    else:
        print(f'  Data for the year {year} is not included in this system.')




if __name__ == '__main__':
    # Do not change this part
    main()
