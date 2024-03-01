#main

def string_manipulator():
    #string_manipulator accepts no arguments
    #it takes a user-inputted string and performs various string manipulations using loops, conditional statements, and functions
    
    #keep_going variable
    keep_going = 'y'
    
    #call menu, call chosen function, ask for keepgoing
    while keep_going == 'y':
        choice = menu()
        if choice == 1:
            input_gathering()
        elif choice == 2:
            string_reversal()
        elif choice == 3:
            count_vowels()
        elif choice == 4:
            character_counter()
        elif choice == 5:
            character_replacer
        elif choice == 6:
            string_analysis()
        keep_going = input("Would you like to choose another option? (y/n) ")
        
def character_replacer(string):
    #ask for character to replace
    #ask for what to replace with
    #find character in string
    #replace with new character
    #return new string
    
    #ask for character and replacement
    og = input('What character is to be replaced? ')
    
    while og not in string:
        
        og = input('What character in the text is to be replaced? ')
    else:
        replacement = input(f'What is {og} to be replaced with? ')
        
        new_string = string.replace(og, replacement)
    
        new_string = string.replace(og, replacement)
    
    return new_string

