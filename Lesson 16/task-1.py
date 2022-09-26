from abc import abstractmethod


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @abstractmethod
    def eat(self):
        pass


class Teacher(Person):
    def __init__(self, first_name, last_name, salary, subject):
        super().__init__(first_name, last_name)
        self.salary = salary
        self.subject = subject

    def eat(self):
        self.salary -= 5
        print(f'{self.full_name()} had a $5 lunch in the cafeteria')

    def teach(self):
        print(f'{self.first_name} teaches students an {self.subject} lesson')


class Student(Person):
    def __init__(self, first_name, last_name, grade):
        super().__init__(first_name, last_name)
        self.classroom = grade

    def eat(self):
        print(f'{self.full_name()} ate the prepared lunch box')

    def study(self):
        print(f'{self.first_name} studies in the {self.classroom}th grade')


john = Teacher('John', 'Compton', 1400, 'English')
john.eat()
john.teach()

ann = Student('Ann', "Grimes", '4')
ann.eat()
ann.study()
