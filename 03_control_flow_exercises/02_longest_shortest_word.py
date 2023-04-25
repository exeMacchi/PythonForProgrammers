# 2) Create a program that asks the user for a list of words and determines the 
#    longest and shortest word. If the user enters an empty string, the program 
#    should display an error message and ask the user to enter a valid string.
def main():
    while True:
        try:
            length = int ( input("2) Enter the amount of words for the list: "))
        except:
            print("Error: non-numeric value.")
        else:
            if length > 0:
                break
            else:
                print("Error: the number must be greater than 0.")
    
    words = list()
    i = 0
    while i < length:
        try:
            word = input(f"{i + 1}. Enter a word: ")
        except Exception as e:
            print(f"Error: {e}")
        else:
            if word != "":
                words.append(word)
                i += 1
            else:
                print("Error: string cannot by empty.")
    
    longest_word = words[0]
    shortest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        
        if len(word) < len(shortest_word):
            shortest_word = word
        
    print(f"# The shortest word in the list: {shortest_word}")
    print(f"# The longest word in the list: {longest_word}")

if __name__ == '__main__':
    main()
