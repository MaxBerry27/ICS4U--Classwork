from typing import List


class Person:
    """Food class
    Attributes:
        name (str): the name of the food
        cost (int): how much the food costs
        nutrition (int): how nutritious the food is
    """

    def __init__(self, first_name: str = None, last_name: str = None, email: str = None, age: int = None):
        """Create a Food object.
        Args:
            name: the name of the food
            cost: how much the food costs
            nutrition: how nutritious the food is
        """
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age

    def __str__(self):
        return f"{self._first_name} {self._last_name}"
        
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, new_value):
        if type(new_value) == str:
            self._first_name = new_value
        else:
            raise Exception("must be string")
    
    def get_last_name(self):
        return self._last_name

    def set_last_name(self, new_value):
        if type(new_value) == str:
            self._last_name = new_value
        else:
            raise Exception("must be string")

    def get_email(self):
        return self._email

    def set_email(self, new_value):
        if type(new_value) == str:
            self._email = new_value
        else:
            raise Exception("must be string")

    def get_age(self):
        return self._age

    def set_age(self, new_value):
        self._age = new_value
       

    def greet(self):
        return f"Hi, I am {self._first_name} {self._last_name}"


class Teacher(Person):

    all_teachers = []

    def __init__(self, first_name: str = None, last_name: str= None , email: str= None , age: int = None,  pin: int = None, school: str = None, classes: List = None):
        super().__init__(first_name, last_name, email, age)
        self._pin = pin
        self._school = school
        self._classes = []

        Teacher.all_teachers.append(self)
    
    def get_pin(self):
        return self._pin
    
    def set_pin(self, new_value):
        if type(new_value) == int:
            self._pin = new_value
        else:
            raise Exception("must be int")
    
    def get_school(self):
        return self._school
    
    def set_school(self, new_value):
        if type(new_value) == str:
            self._school = new_value
        else:
            raise Exception("must be str")
    
    def get_classes(self):
        return self._classes

    def assign_work(self, classa):
        if classa in self.classes:
            print(f"{self._last_name} has assigned {classa} work!")
        else:
            raise Exception(f"{self.get_last_name()} does not have a class named {classa}")

    def add_class(self, class_name):
        if len(self._classes) >5:
            raise Exception("max classes reached")
        else:
            self._classes.append(class_name)

    def remove_class(self, class_name):
        if len(self._classes) < 1:
            raise Exception("teacher has no classes")
        else:
            self._classes.remove(class_name)

    @classmethod
    def find_fname(cls, target):
        new_teachers = []
        for teacher in Teacher.all_teachers:
            if teacher._last_name == target:
                Teacher.new_teachers.append(teacher)
        return new_teachers
                

class Student(Person):
    def __init__(self, first_name: str = None, last_name: str= None , email: str= None , age: int = None, student_number = 0000):
        super().__init__(first_name, last_name, email, age)
        self.student_number = student_number


class Class:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)

    def add_dem(self):
        total = 0
        for student in self.students:
            total += student._age
        print(total)


comsci = Class("com", )

bob = Student(age = 65)
joe = Student(age = 1)
nigga = Student(age = 34)

comsci.add_student(bob)
comsci.add_student(joe)
comsci.add_student(nigga)

comsci.add_dem()



