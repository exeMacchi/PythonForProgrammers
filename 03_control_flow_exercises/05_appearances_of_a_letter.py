# 5) Create a program that asks the user for a text string and determines how 
#    many times a given letter appears in the string. If the user enters an 
#    empty string or a letter that is not a character, the program should 
#    display an error message and ask the user to enter a valid string or a 
#    valid letter.
def main():
    while True:
        user_text = input("5) a) Enter a text: ")
        if user_text != "":
            break
        else:
            print("Error: text cannot by empty.")
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    user_letter = str()
    while True:
        user_character = input("5) b) Enter a letter: ")
        if user_character[0] in alpha or user_character[0] in alpha.upper():
            user_letter = user_character[0]
            del user_character
            break
        else:
            print("Error: the character entered is not a letter.")
    
    appearences = 0
    for char in user_text:
        if char.lower() == user_letter.lower():
            appearences += 1
        
    print(f"# The letter '{user_letter}' appears {appearences} times in the text.")

if __name__ == '__main__':
    main()
