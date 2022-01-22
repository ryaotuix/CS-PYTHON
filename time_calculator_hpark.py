"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Time Calculator
Date: 9/19/2001

Description:
    Determine the time in seconds, minutes, hours, and day according to user's
    input in seconds. You will result in certain format for different range of
    seconds

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

    second = int(input('Please enter a time in seconds: '))

    if second < 60:
        second = format(second,",d")
        print('  ' + str(second),'seconds is less than one minute.')

    elif second == 60:
        second = format(second,",d")
        print('  ' + str(second),'seconds is 1 minute(s).')

    elif second < 3600: #case where you have minutes, and seconds
        seconds = int(second%60)
        minutes = int((second-seconds)/60)
        second = format(second,",d")
        if seconds == 0:
            print('  ' + str(second),'seconds is: ' + str(minutes), 'minute(s).')
        else:
            print('  ' + str(second),'seconds is: ' + str(minutes), 'minute(s) and', str(seconds), 'second(s).')

    elif second == 3600:
        second = format(second,",d")
        print('  ' + str(second),'seconds is 1 hour(s).')

    elif second < 86400: #case where you have hours, minutes, and seconds
        hours = int(second/3600)
        minutes = int(second%3600/60)
        seconds = second%3600%60
        second = format(second,",d")
        if seconds == 0 and minutes == 0:
            print('  ' + str(second),'seconds is: ' + str(hours), 'hour(s).')
        elif minutes == 0:
            print('  ' + str(second),'seconds is: ' + str(hours), 'hour(s) and', str(seconds), 'second(s).')
        elif seconds == 0:
            print('  ' + str(second),'seconds is: ' + str(hours), 'hour(s) and', str(minutes), 'minute(s).')
        else:
            print('  ' + str(second),'seconds is: ' + str(hours), 'hour(s),', str(minutes), 'minute(s) and', str(seconds), 'second(s).')

    elif second == 86400:
        second = format(second,",d")
        print('  ' + str(second),'seconds is 1 day(s).')

    elif second > 86400: #case where you have all days, hours, minutes, and seconds
        days = int(second/86400)
        hours = int(second%86400/3600)
        minutes = int(second%86400%3600/60)
        seconds = second%86400%3600%60
        second = format(second,",d")
        if hours == 0 and minutes == 0 and seconds == 0:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s).')
        elif minutes == 0 and seconds == 0:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s) and', str(hours), 'hour(s).')
        elif hours == 0 and seconds == 0:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s) and', str(minutes), 'minute(s).')
        elif hours == 0 and minutes == 0:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s) and', str(seconds), 'second(s).')
        elif hours == 0:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s),', str(minutes), 'minute(s) and', str(seconds), 'second(s).')
        elif minutes == 0:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s),', str(hours), 'hour(s) and', str(seconds), 'second(s).')
        elif seconds == 0:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s),', str(hours), 'hour(s) and', str(minutes), 'minute(s).')
        else:
            print('  ' + str(second),'seconds is: ' + str(days), 'day(s),', str(hours), 'hour(s),', str(minutes), 'minute(s) and', str(seconds), 'second(s).')

if __name__ == '__main__':
    main()
