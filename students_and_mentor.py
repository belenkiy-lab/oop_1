class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def give_raiting(self, lecturer, course, raitng):
        if not isinstance(raitng, int):
            print('Оценка должна быть числом')
        elif raitng not in range(10):
            print(f'"{raitng}" - недопустимая  оценка. Оценка должна быть от 0 до 9')
        elif course not in self.courses_in_progress:
            print("Оценку можно поставить только за курс на котором учишься")
            print('Текущие курсы')
            print(*self.courses_in_progress, sep=', ')
        elif course not in lecturer.courses_attached:
            print("Оценку можно поставить только преподователю который ведет курс.")
            print(f'Лектор {lecturer.name} {lecturer.surname} ведет:')
            print(*lecturer.courses_attached, sep=', ')
        else:
            lecturer.raiting[course] = lecturer.raiting.get(
                course, []) + [raitng]
            print(lecturer.raiting)


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.raiting = {}


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
