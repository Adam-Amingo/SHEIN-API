class OnlineCourse :
    def __init__(self, course , instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_students(self, student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the {self.course}")
    
    def course_detail(self):
        print(f"Course name: {self.course}")
        print(f"Instructor name : {self.instructor}")
        print(f"Enrolled students: ")
        for student in self.students:
            print(student.name)
    
    def completed_course(self , name):
        for student in self.students:
            if student.name in name:
                self.students.remove(name)
                print(f"{name } had completed the course")

        print(f"{name} is not enrolled in the course")
        
    def avg_grade(self,grades):
        total = sum(student.grades)
        average = total  / len(student.grades)
        print(f"The average grade is : {average}")

class Student:
    def __init__(self , name , grades):
        self.name = name 
        self.grades = grades


#
course_input = input("Enter a course : ").lower()
name = input("Enter a  Instructor : ").lower()



course = OnlineCourse(course_input , name)
# grades = [90 , 85 , 93 , 78 , 80]

#
num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    student_name = input("Enter a student name: ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Entera grade: "))
        grades.append(grade)
    student = Student(student_name , grades)
    course.enroll_students(student)
    course.avg_grade(student)
course.course_detail()
