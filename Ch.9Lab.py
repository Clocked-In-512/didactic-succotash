##Robert Fernandez
##Complete
##The program will prompt the user to enter a course number which will provide the room number, time, and the instuctor for each course.  

# Dictionary containing course numbers and the room numbers where the courses meet
course_rooms = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}

# Dictionary containing course numbers and the names of the instructors that teach each course
course_instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvardo',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

# Dictionary containing course numbers and the meeting times for each course
course_meeting_times = {
    'CS101': '8:00 a.m.',
    'CS102': '9:00 a.m.',
    'CS103': '10:00 a.m.',
    'NT110': '11:00 a.m.',
    'CM241': '1:00 p.m.'
}

# Function to display course information based on user input
course_number = input('Enter a course number or press Enter to stop: ')

if course_number in course_rooms:
    print('The details for course', course_number, 'are:')
    print(f'Room Number: {course_rooms[course_number]}')
    print(f'Instructor: {course_instructors[course_number]}')
    print(f'Meeting Time: {course_meeting_times[course_number]}')
else:
    print('is an invalid course number.')
