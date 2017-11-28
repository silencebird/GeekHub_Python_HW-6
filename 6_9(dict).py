dict = {
    'name': 'Vasya',
    'l_name': 'Pupkin',
    'age': 20
}

class DefaultClass1:
    def __init__(self, name, l_name,age ):
        self.name = name
        self.l_name = l_name
        self.age  = age

    def print_info(self):
        print(self.__dict__.keys())

user = DefaultClass1(dict['name'], dict['l_name'], dict['age'])


user.print_info()