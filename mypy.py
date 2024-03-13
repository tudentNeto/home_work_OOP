class Student():
    def __init__(self,name,surname,gender):
        self.name=name
        self.surname=surname
        self.gender=gender
        self.finished_courses=[]
        self.courses_in_progress=[]
        self.grades={}

    def add_courses(self,course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self,lector,course,grade):
        if isinstance(lector,Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            lector.grades.setdefault(course,[])
            lector.grades[course]+=[grade]
        else:
            return 'Error'

    def calc_rate_avg(self):
        sum_rate, count_rate = 0, 0
        for k, v in self.grades.items():
            for i in v:
                sum_rate+=i
                count_rate+=1
        return sum_rate/count_rate

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calc_rate_avg()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n")

    def __lt__(self, other):
        return self.calc_rate_avg()<other.calc_rate_avg()
                

class Mentor():
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        self.courses_attached=[]

    def add_course_attached(self,course):
        self.courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades={}

    def calc_rate_avg(self):
        sum_rate, count_rate = 0, 0
        for k, v in self.grades.items():
            for i in v:
                sum_rate+=i
                count_rate+=1
        return sum_rate/count_rate

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calc_rate_avg()}\n"

    def __lt__(self, other):
        return self.calc_rate_avg()<other.calc_rate_avg()


class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)

    def rate_hw(self,student,course,grade):
        if isinstance(student,Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course,[])
            student.grades[course]+=[grade]
        else:
            return 'Error'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


def calc_avg_grade_in_course(list_students,course):
    sum_grade=0
    counter=0
    for el in list_students:
        d_el=el.grades
        if d_el.get(course,0)!=0:
            sum_grade+=sum(d_el[course])
            counter+=len(d_el[course])
    return 0 if sum_grade==0 or counter==0 else sum_grade


def calc_avg_grade_lec_in_course(list_lecturers,course):
    sum_grade=0
    counter=0
    for el in list_lecturers:
        d_el=el.grades
        if d_el.get(course,0)!=0:
            sum_grade+=sum(d_el[course])
            counter+=len(d_el[course])
    return 0 if sum_grade==0 or counter==0 else sum_grade/counter


best_student=Student('Ryon', 'Eman','m')
best_student.finished_courses+=['Git']
best_student.finished_courses+=['Java']
best_student.courses_in_progress+=['Python']
best_student.courses_in_progress+=['PHP']
best_student.grades['Git']=[10,10,10,10,10]
best_student.grades['Python']=[10,10]
next_student=Student('RRyon', 'EEman','m')
next_student.finished_courses+=['Git', 'Python', 'Delphi']
next_student.courses_in_progress+=['Excel','Oracle','Java']
next_student.grades['Excel']=[8,8,8,8]
next_student.grades['Python']=[7,7,7]
next_student.grades['Oracle']=[5,5,5]
first_lecturer=Lecturer('Ome','Buddy')
first_lecturer.courses_attached+=['Python']
second_lecturer=Lecturer('Ame', 'Guddy')
second_lecturer.courses_attached+=['Java']
second_lecturer.add_course_attached('Delphi')
best_student.rate_lec(first_lecturer,'php',9)
best_student.rate_lec(first_lecturer,'Python',7)
best_student.rate_lec(first_lecturer,'Python',10)
next_student.rate_lec(first_lecturer,'Python',7)
best_student.rate_lec(second_lecturer,'Java',10)
next_student.rate_lec(second_lecturer,'Java',5)
best_student.rate_lec(second_lecturer,'Delphi',9)
first_reviewer=Reviewer('OOme','BBude')
first_reviewer.courses_attached+=['Python', 'PHP', 'Java']
first_reviewer.rate_hw(best_student,'Python',10)
first_reviewer.rate_hw(next_student,'Excel',8)
second_reviewer=Reviewer('AAme','GGude')
second_reviewer.courses_attached+=['Excel', 'Oracle']
second_reviewer.add_course_attached('PHP')
second_reviewer.rate_hw(next_student,'Oracle',9)
print(first_lecturer.courses_attached)
print(first_lecturer.grades)
print(best_student.calc_rate_avg())
print(first_lecturer.calc_rate_avg())
print(first_lecturer)
print(second_lecturer)
print(second_reviewer)
print(first_reviewer)
print(best_student)
print(next_student)
print(best_student>next_student)
print(first_lecturer.calc_rate_avg())
print(second_lecturer.calc_rate_avg())
print(first_lecturer>second_lecturer)
print(calc_avg_grade_in_course([best_student,next_student],'Java'))
print(calc_avg_grade_lec_in_course([first_lecturer, second_lecturer],'Java'))



