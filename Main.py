class Group:
    name: str
    number: int
    age: int

    def __init__(self, name: str, number: int, age: int):
        self.Name = name
        self.Number = number
        self.Age = age
    def info_Group(self):
        print(f'Group: {self.Name} | {self.Number} | {self.Age}')

    def info_all(self):
        self.info_Group()


group = Group(name=input(str('Name(group): ')), number=input(str('Number: ')), age=input(str('Age: ')))
group.info_all()

class Person:
    name: str
    surname: str
    age: int
    pensione: bool

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')

personX = Person(name='unknown_name', surname='unknown_surname', age=30)
#personX.info_person()

class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)



    def info_teacher(self):
        print(f'teacher:\t{self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()

teacher = Teacher(subject='Pycharm', hours=24, name='Daniil', surname='Kislita', age=30)

#teacher.info_all()

class Student (Person):
    progress: float
    group: str
    pensione: bool
    def __init__(self, progress: float, group: str, name: str, surname: str, age: int):
        self.progress = progress
        self.group = group
        Person.__init__(self, name=name, surname=surname, age=age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_student(self):
        print(f'student:\t{self.progress} | {self.group}')
    def info_all(self):
        self.info_person()
        self.info_student()

student = Student(progress=10.5, group='C2126', name='Daniil', surname='Kislitsa', age=30)
student.info_all()

class Worker(Person):
    position: str
    duties: list
    pensione: bool
    def __init__(self,position: str, duties: list, name: str, surname: str, age: int):
        self.position = position
        self.duties = duties
        Person.__init__(self, name=name, surname=surname, age=age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_Worker(self):
        print(f'Worker:\t{self.position} | {self.duties}')

    def info_all(self):
        self.info_person()
        self.info_Worker()

worker = Worker(position = 'teacher', duties='teach children'  ,name='Daniil', surname='Kislitsa', age=62)
worker.info_all()

