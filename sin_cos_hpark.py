"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Sin Cos
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
from math import pi
import math
import matplotlib.pyplot as plt

def main():
    fig, ax = plt.subplots()
    # r'$\pi$'
    degs = []
    for i in range (0,361,1): # 361 to go to 360
        degs.append(i)
    x, y_sin, y_cos = [], [], []
    for deg in degs:
        x_rad = math.radians(deg) # change it to degree
        x.append(x_rad)
        y_sin.append(math.sin(x_rad))
        y_cos.append(math.cos(x_rad))



    ax.set_xticks([pi/2, pi, 3*pi/2, 2*pi])
    ax.set_xticklabels(['$\\pi/2$','$\\pi$','$3\\pi/2$','$2\\pi$']) # important latex figure
    ax.plot(x,y_sin, color = 'r') # use string for color
    ax.plot(x,y_cos, color = 'b')
    ax.set_yticks([-1,1])
    # get rid of the line in the top and right of graph
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    # set axis as y =0
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')

    plt.show()

if __name__ == '__main__':
    # Do not change this part
    main()
