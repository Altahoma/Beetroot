from abc import abstractmethod


class Animal:
    @staticmethod
    @abstractmethod
    def talk():
        pass


class Cat(Animal):
    @staticmethod
    def talk():
        print('meow')


class Dog(Animal):
    @staticmethod
    def talk():
        print('woof')


tomas = Cat()
odie = Dog()

tomas.talk()
odie.talk()