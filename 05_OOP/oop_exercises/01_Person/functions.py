def ask_name():
    while True:
        try:
            name = input("Enter your name: ")
        except Exception as e:
            print(f"Error: {e}")
        else:
            if name != "":
                return name
            else:
                print("Error: name cannot be empty.")


def ask_age():
    while True:
        try:
            age = int( input("Enter your age: "))
        except Exception as e:
            print(f"Error: {e}")
        else:
            if age > 0:
                return age
            else:
                print("Error: age must be greater than 0.")
