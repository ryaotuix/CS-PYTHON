"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - Course Info
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

def get_course_data():
    # make lists for all entities
    numbers = ['CS101', 'CS102', 'CS103', 'NT110', 'CM241']
    rooms = [3004, 4501, 6755, 1244, 1411]
    instructors = ['Django', 'Idle', 'Rich', 'Marshal', 'Pickle']
    times = ['9:00 a.m.', '10:00 a.m.', '11:00 a.m.', '12:00 p.m.', '2:00 p.m.']
    d = {} # initialize empty dictionary
    for i in range(5):
        d.update({numbers[i]: {"room": str(rooms[i]), "instructor": instructors[i], 'time': times[i]}})
        # update it

    return d





def main():

    d = get_course_data()
    course = input('Enter a course number: ').upper()
    if course in d.keys(): # if it is a key
        print(f'  The details for course {course} are:')
        # one nested dictionary
        room = d[course]['room']
        instructor = d[course]['instructor']
        time = d[course]['time']
        print(f'    Instructor: {instructor}')
        print(f'          Room: {room}')
        print(f'          Time: {time}')
    else:
        print(f'  {course} is an invalid course number.')




if __name__ == '__main__':
    # Do not change this part
    main()
