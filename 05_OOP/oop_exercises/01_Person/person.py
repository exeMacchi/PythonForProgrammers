class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    
    def introduce_myself(self):
        return f"Hi, my name is {self.__name} and I am {self.__age} years old."
