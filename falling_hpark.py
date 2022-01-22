"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Falling
Date: 10/04/2021

Description:
    Calculates and returns the distance in meters that the object will fall
    during time

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

gravity = 8.87 #gravity is constant throughout all functions
distance = 0

def falling_dist(falling_time):
    distance = 0.5*gravity*(falling_time**2)
    return distance

def main():
    print("Time (s)  Distance (m)")
    print("----------------------")

    for falling_time in range(5, 51, 5): #increase by 5 stops at 50
        distance = falling_dist(falling_time)
        print(f'{falling_time:8}   {distance:11.1f}')




if __name__ == '__main__':
    main()
