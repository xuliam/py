print ('dad!')

 # 定义一个学生类
#   要求：
# 1. 属性包括学生姓名，学好， 以及语文数学英语成绩
# 2. 能够设置学生某科目成绩
# 3. 能够打印该学生所有成绩

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {'chinese': None, 'math': None, 'english': None}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"Name: {self.name} ({self.student_id}) Grades:")
        for course in self.grades:
            print(f"\t{course}: {self.grades[course]}")

chen = Student('chen', '123456')
zhang = Student('zhang', '245256')

chen.set_grade('chinese', 90)
chen.set_grade('math', 80)
chen.set_grade('english', 70)

chen.print_grades()


# print (chen)
# zhang.set_grade('chinese', 90)
# print (zhang.grades)
# print (zhang.student_id)