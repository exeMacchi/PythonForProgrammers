# Declarar una clase padre.
class Person:
    # Crear un constructor.
    def __init__(self, name, age):
        self.name = name  # Campo público
        self.__age = age  # Campo privado
    
    def introduce_myself(self):
        print(f"Hi! my name is {self.name} and I am {self.__age} years old.")
    
    def __del__(self):
        print("Object destroyed")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self._subject = subject  # Campo protegido
    
    # Método para representar de forma legible una instancia.
    def __repr__(self):
        return f"Name: {self.name}, Age: {self._Person__age}"

   
def main(): 
    # Instanciar una clase.
    myTeacher = Teacher('Mr. White', 50, 'Chemistry')

    # Acceder a campos y métodos de la clase.
    print(myTeacher.name)
    # print(myTeacher.__age) ---> Atribute Error: el campo es privado.
    myTeacher.introduce_myself()
    print(myTeacher.__repr__())

    # Accionar destructor.
    del myTeacher


if __name__ == '__main__':
    main()
