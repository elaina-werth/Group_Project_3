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
    
    
    
    
    