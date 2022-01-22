"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Fluid Mechanics
Date: 9/19/2001

Description:
    Determine reynoldnumber value given that temperature and velocity. Viscosity value
    varies according to temperature.

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

def main():

    temperature = float(input('Enter the temperature in °C as 5, 10, or 15: '))
    if int(temperature) == 5: #viscosity varies aepend on temperature
        viscosity = 1.49*10**-6
    elif int(temperature) == 10:
        viscosity = 1.31*10**-6
    elif int(temperature) == 15:
        viscosity = 1.15*10**-6
    else:
        viscosity = 0
    velocity = float(input('Enter the velocity of water in the pipe: '))
    diameter = float(input('Enter the pipe\'s diameter: '))
    reynoldsNumber = velocity*diameter/viscosity

    print('At', str(temperature) + '°C,', 'the Reynolds number for flow at', str(velocity), 'm/s in a', str(diameter), f'm diameter pipe is {reynoldsNumber:.2e}.' )
#remember fstring and {} to format

if __name__ == '__main__':
    main()
