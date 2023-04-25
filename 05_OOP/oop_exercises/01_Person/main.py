# 1) Create a class called "Person" that has attributes "name" and "age". 
#    Add a method called "introduce" that prints "Hi, my name is [person's name] 
#    and I am [person's age] years old." to the console. Then, create an object 
#    of type "Person" and call the "introduce" method.
from person import Person
from functions import ask_name, ask_age

def main():
    user_name = ask_name()
    user_age = ask_age()
    person = Person(user_name, user_age)
    
    print(person.introduce_myself())


if __name__ == '__main__':
    main()
