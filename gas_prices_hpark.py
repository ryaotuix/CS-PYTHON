"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Gas Prices
Date: 11/27/2021

Description:
    read files named xian1 and xian2. Then, from each text file, find the word
    and freqeuncy of the word of each file; print it in a new file.
    Moreover, we should find common words and words that are not common; print
    them in a new file


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
import matplotlib.pyplot as plt

def file_to_list():
    l = []
    with open('2008_Weekly_Gas_Averages.txt') as fo:
        for line in fo:
            l.append(float(line.rstrip()))
    return l

def main():
    fig, ax = plt.subplots()

    # make plot with x as week y as average gas price
    x = []
    for i in range(1,53,1):
        x.append(i)
    y = file_to_list()
    ax.plot(x, y)


    # title, labels, and grid
    ax.set_title('2008 Weekly Gas Prices')
    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_xlabel('Weeks (by number)')
    ax.set_ylim(1.5,4.25) # set limit of y

    ax.set_xlim(1,52)
    
    ax.grid()

    plt.show()


if __name__ == '__main__':
    # Do not change this part
    main()
