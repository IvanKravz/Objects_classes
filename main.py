class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lectors, course, grade):  # Оценка лекторов студентами
        if isinstance(lectors, Lecturer) and course in lectors.courses_attached and course in self.courses_in_progress:
            if course in lectors.grades:
                lectors.grades[course] += [grade]
            else:
                lectors.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):
        grade = 0
        sum_grade = 0
        for values in self.grades.values():
            for i in values:
                grade += i
                sum_grade += 1
        return round(grade/sum_grade, 1)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_score()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {" ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if self.average_score() > other.average_score():
            print(f'{self.name, self.surname} имеет бал выше чем {other.name} {other.surname}')
        else:
            print(f'{other.name} {other.surname} имеет бал выше чем {self.name} {self.surname}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

    def rate_hw(self, student: object, course: object, grade: object) -> object: # Оценка ревьюерами студентов
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def average_score(self):
        grade = 0
        sum_grade = 0
        for values in self.grades.values():
            for i in values:
                grade += i
                sum_grade += 1
        return round(grade/sum_grade, 1)

    def __lt__(self, other):
        if self.average_score() > other.average_score():
            print(f'{self.name, self.surname} имеет бал выше чем {other.name} {other.surname}')
        else:
            print(f'{other.name} {other.surname} имеет бал выше чем {self.name} {self.surname}')

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_score()}'
        return res

def student_average_grade_course(list_student, course):
    grade = []
    for student in list_student:
        for k, v in student.grades.items():
            if k in course:
                grade.append(v)
    list_grade = sum(grade, [])
    average_grade = round(sum(list_grade) / len(list_grade), 1)
    print(f'Средняя оценка студентов за домашние задания по курсу {course} составляет {average_grade}')

def lector_average_grade_course(list_lector, course):
    grade = []
    for lector in list_lector:
        for k, v in lector.grades.items():
            if k in course:
                grade.append(v)
    list_grade = sum(grade, [])
    average_grade = round(sum(list_grade) / len(list_grade), 1)
    print(f'Средняя оценка лекторов по курсу {course} составляет {average_grade}')


best_student = Student('Ruoy', 'Eman', 'your_gender')   #Студенты
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

second_student = Student('Антон', 'Антонов', 'your_gender')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']


cool_reviewer = Reviewer('Сергей', 'Сергеев')   #Ревьюеры
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
second_reviewer = Reviewer('Гит', 'Гитов')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

cool_lecturer = Lecturer('Иван', 'Иванов')   #Лекторы
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
second_lecturer = Lecturer('Ан', 'Анов')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']


cool_reviewer.rate_hw(best_student, 'Python', 10)  #Ревьюеры ставят оценки студентам
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Git', 8)
second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Git', 10)
second_reviewer.rate_hw(second_student, 'Git', 9)
second_reviewer.rate_hw(second_student, 'Git', 9)

best_student.rate_lector(cool_lecturer, 'Python', 10)  #Студенты оценивают лекторов
best_student.rate_lector(cool_lecturer, 'Python', 9)
best_student.rate_lector(cool_lecturer, 'Python', 8)
best_student.rate_lector(cool_lecturer, 'Git', 9)
best_student.rate_lector(cool_lecturer, 'Git', 9)
best_student.rate_lector(cool_lecturer, 'Git', 8)
second_student.rate_lector(second_lecturer, 'Python', 10)
second_student.rate_lector(second_lecturer, 'Python',10)
second_student.rate_lector(second_lecturer, 'Python', 9)
second_student.rate_lector(second_lecturer, 'Git', 9)
second_student.rate_lector(second_lecturer, 'Git', 9)
second_student.rate_lector(second_lecturer, 'Git', 10)

list_students = [best_student, second_student]
list_lecturer = [cool_lecturer, second_lecturer]

# print(best_student.courses_in_progress)
# print(best_student.grades)
# print(second_student.grades)
# print(cool_lecturer.grades)
# print(second_lecturer.grades)

print('Reviewer: ')
print(cool_reviewer)
print(second_reviewer)
print(' ')
print('Lecturer: ')
print(cool_lecturer)
print(second_lecturer)
print(' ')
print('Students: ')
print(best_student)
print(second_student)
print(' ')
cool_lecturer < second_lecturer
best_student < second_student
print(' ')
student_average_grade_course(list_students, 'Python')
lector_average_grade_course(list_lecturer, 'Python')