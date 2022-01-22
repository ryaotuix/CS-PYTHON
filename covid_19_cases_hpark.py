"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Covid 19 Cases
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
import datetime
import matplotlib.pyplot as plt


def file_to_list():
    #the file has 1. date 2. number of new tests performed 3. number of positie results 4. number of new deaths
    l = []
    with open('indiana_covid_19_data_fall_2021.txt') as fo:
        for line in fo:
            l.append(line.rstrip().split(' ')) # [[202x-xx-xx, 2, 3, 4] .. ]
    return l

def main():
    fig, ax = plt.subplots()

    l = file_to_list()

    # extract dates in format of 20xx-xx-xx and make a list
    dates = []
    for i in range(len(l)):
        dates.append(l[i][0])
    # make x axis list with list of dates
    x = []
    for date in dates:
        y, m, d = date.split('-')
        dt = datetime.date(int(y), int(m), int(d))
        x.append(dt)


    # daily positive result
    daily_positive_result = []
    for i in range(len(l)):
        daily_positive_result.append(int(l[i][2]))

    # make y axis list with the list above
    y = []
    for i in range(1, len(daily_positive_result) + 1, 1):
        accumulated_patients = sum(daily_positive_result[:i]) # list slicing
        y.append(accumulated_patients/1000)

    ax.bar(x,y,width=1)
    fig.autofmt_xdate()

    # title, labels, and grid
    ax.set_title('Positive COVID-19 Cases in Indiana')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')



    plt.show()


if __name__ == '__main__':
    # Do not change this part
    main()
