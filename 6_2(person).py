
class Person:

    def __init__(self, name, age, gender, has_children,marital_status, high_educated):
        self.name = name
        self.age = age
        self.age = gender
        self.has_children = has_children
        self.marital_status = marital_status
        self.high_educated = high_educated

    def show_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

    def show_all_information(self):
        print(self.__dict__)

class workPerson(Person):
    def __init__(self,name, age, gender, has_children,marital_status, high_educated, profession):
        super(workPerson,self).__init__(name, age, gender, has_children,marital_status, high_educated)
        self.profession = profession

    def show_profession(self):
        print(self.profession)

petya = workPerson("Petya", 26, "male", False, False, True,"programer")
vasya = workPerson("Vasya", 30, "male", True, True, True,"programer")
petya.show_age()
petya.print_name()
petya.show_profession()
petya.show_all_information()
