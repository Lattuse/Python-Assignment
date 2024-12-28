

courses = {
 "CS101": ("Intro to Computer Science", "Dr. Smith", 30, set()),
 "MATH203": ("Calculus II", "Dr. Johnson", 25, set()),
 "PHY150": ("General Physics", "Dr. Clark", 20, set()),
 "ENG102": ("English Composition", "Dr. Taylor", 40, set()),
 "BIO110": ("Introduction to Biology", "Dr. Lee", 35, set())
}

registered_courses = {}

#courses filler
#for i in range(30):
#   courses["CS101"][3].add(i)

option = 0

while option!=5:
    print('''\nWelcome to the Course Registration System!
    1. View all courses
    2. Register for a course
    3. Drop a course
    4. View my courses
    5. Exit''')

    option = int(input("\nOption: "))

    if option == 1:
        print("\nAll existing courses:")
        for course in courses:
            print("\n==========================================")
            print(f'''Course Code: {course}
        Title: {courses[course][0]}
        Instructor: {courses[course][1]}
        Capacity: {courses[course][2]}
        Enrolled: {len(courses[course][3])}
        ''')
            print("==========================================")
        
            
    if option == 2:
        course_code = input("\nEnter course code: ")
        if course_code in courses:
            if "User" not in courses[course_code][3]:
                if len(courses[course_code][3]) < courses[course_code][2]:

                    courses[course_code][3].add("User")
                    registered_courses[course_code] = courses[course_code]
                    print(f"\nSuccessfully registered for {course_code}.")

                else:
                    print("\nSorry, the number of students in this course has already reached its limit!")
            else:
                print("\nYou are already registered for the course!")
        else:
            print("\nSuch course code doesn't exist!")

    if option == 3:
        if len(registered_courses) !=0:
            course_code = input("\nEnter course code: ")
            if course_code in courses:
                if course_code in registered_courses:
                    
                    courses[course_code][3].remove("User")
                    registered_courses.pop(course_code)
                    print(f"\nSuccessfully dropped {course_code} course.")
                    
                else:
                    print(f"\nYou are not registered for {course_code}.")
            else:
                print("\nSuch course code doesn't exist!")
        else:
            print("\nYou are not registered for any courses.")

    if option == 4:
        if len(registered_courses) !=0:
            print("\nYour registered courses:")
            for course in registered_courses:
                print("\n==========================================")
                print(f'''Course Code: {course}
            Title: {registered_courses[course][0]}
            Instructor: {registered_courses[course][1]}
            Capacity: {registered_courses[course][2]}
            Enrolled: {len(registered_courses[course][3])}
            ''')
                print("==========================================")
        else:
            print("\nYou are not registered for any courses.")

print("\nThank you for using the Course Registration System. Goodbye!\n")
