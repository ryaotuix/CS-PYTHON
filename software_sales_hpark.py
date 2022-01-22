"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Software Sales
Date: 9/19/2001

Description:
    Determine the discount and the price of packages someone wants to purchase
    based on the number of packages he/she wants to buy. The price of a single
    package is fixed and discount varies according to number of purchased packages.

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

    package = float(input('How many packages will be purchased: '))
    if package<0: #first case scenario
        print('  Invalid Input!')
    elif package<5: #second case scenario
        price = float(package*79)
        print('  No discount applied.')
        print('  The total price for purchasing',str(int(package)),'packages is $'+format(price,'2,.2f')+'.')
    elif package<25: #third case scenario
        price = float(package*79*0.9)
        print('  10% discount applied.')
        print('  The total price for purchasing',str(int(package)),'packages is $'+format(price,'2,.2f')+'.')
    elif package<50: #fourth case scenario
        price = float(package*79*0.8)
        print('  20% discount applied.')
        print('  The total price for purchasing',str(int(package)),'packages is $'+format(price,'2,.2f')+'.')
    elif package<100: #fifth case scenario
        price = float(package*79*0.7)
        print('  30% discount applied.')
        print('  The total price for purchasing',str(int(package)),'packages is $'+format(price,'2,.2f')+'.')
    else: #last case scenario
        price = float(package*79*0.55)
        print('  45% discount applied.')
        print('  The total price for purchasing',str(int(package)),'packages is $'+ format(price,'2,.2f')+'.')







if __name__ == '__main__':
    main()
