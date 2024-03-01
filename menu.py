#menu

def menu():
    #menu accepts no arguments
    #it creates a menu allowing user to choose which operation to perform
    
    print("Welcome to the String Manipulator! \n")
    
    print("1.) Input a string")
    print("2.) Reverse a strint")
    print("3.) Count vowels")
    print("4.) Replace characters")
    print("5.) Analyze a string")
    print("6.) Exit")
    
    choice = input("Please choose an option (1-6): ")
    
    if choice.isdigit() == False:
        choice = input("Oops! You didn't enter a number.\n\nPlease choose an option (1-6): ")
    
    return choice