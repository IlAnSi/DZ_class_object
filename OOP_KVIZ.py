class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        sum = 0
        len_gr = 0
        for grad in self.grades.values():
            for gr in grad:
                sum += gr
                len_gr += 1
        res = sum / len_gr
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

    def average_grades(self):
        sum = 0
        len_gr = 0
        for grad in self.grades.values():
            for gr in grad:
                sum += gr
                len_gr += 1
        res = sum / len_gr
        return res

    def __str__(self):
        res = f'Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}\n'
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Проверяющий\nИмя: {self.name}\nФамилия: {self.surname}\n'
        return res

#Студенты
best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']
best_student1.finished_courses += ['Introduction to programming']

best_student2 = Student('Deny', 'DeVito', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Introduction to programming']

# Проверяющие
cool_mentor1 = Reviewer('Some', 'Buddy')
cool_mentor1.courses_attached += ['Python']
cool_mentor2 = Reviewer('Anna', 'Second')
cool_mentor2.courses_attached += ['Git']

cool_mentor1.rate_hw(best_student1, 'Python', 10)
cool_mentor2.rate_hw(best_student1, 'Git', 9)
cool_mentor2.rate_hw(best_student2, 'Git', 8)
cool_mentor1.rate_hw(best_student2, 'Python', 7)

# Лекторы
cool_mentor3 = Lecturer('Piter', 'Parker')
cool_mentor4 = Lecturer('Triniti', 'Matrix')
cool_mentor3.courses_attached += ['Python']
cool_mentor4.courses_attached += ['Git']

best_student1.rate_hw(cool_mentor3, 'Python', 10)
best_student1.rate_hw(cool_mentor4, 'Git', 10)
best_student2.rate_hw(cool_mentor3, 'Python', 9)
best_student2.rate_hw(cool_mentor4, 'Git', 8)

print(cool_mentor1)
print(cool_mentor2)

print(cool_mentor3)
print(cool_mentor4)

print(best_student1)
print(best_student2)
