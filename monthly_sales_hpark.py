"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Monthly Sales
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



def main():
    fig, ax = plt.subplots() # first step to create plot
    # colors as tuple
    c = ('#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A')
    # labels as tuple
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    # list of each sales in each month
    sales = []
    for month in months:
        sale = input(f'Enter the sales for {month}: ')
        sales.append(sale)
    # add title
    ax.set_title('Monthly Sales Values')
    ax.pie(sales, colors = c, labels = months)
    plt.show() # show anytime after finishing editing plot

if __name__ == '__main__':
    # Do not change this part
    main()
