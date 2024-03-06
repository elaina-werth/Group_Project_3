#main

def character_counter(string):
    #accepts a string as a argument
    #has lists of consonants and vowels
    #compare str to lists
    #each time a character is found in a list
    #it adds to either consonant or vowel depending on list found in
    
    #base lists and varibles
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    con_found = 0
    vow_found = 0
    
    #find amount of vowels
    for character in string:
        if character in vowels:
            vow_found += 1
    
    #find amount of consonants
    for character in string:
        if character in consonants:
            con_found += 1
    
    #return amount each occoured
    return con_found, vow_found

def string_manipulator():
    #string_manipulator accepts no arguments
    #it takes a user-inputted string and performs various string manipulations using loops, conditional statements, and functions
    
    #keep_going variable
    keep_going = 'y'
    
    #call menu, call chosen function, ask for keepgoing
    print("Welcome to the String Manipulator!\n")
    while keep_going == 'y':
        choice = menu()
        if choice == 1:
            string = input_gathering()
        elif choice == 2:
            reverse = string_reversal(string)
            print (f"\n{string} reversed is {reverse}. ")
        elif choice == 3:
            con_found, vow_found = character_counter(string)
            print (f"\nYour string has {con_found} consonants and {vow_found} vowel(s).")
        elif choice == 4:
            new_string = character_replacer(string)
            print("\nYour new string is", new_string)
        elif choice == 5:
            string_analysis(string)
        elif choice == 6:
            print("\nExiting...")
            break
            
        keep_going = input("\nWould you like to choose another option? (y/n): ")
        
def input_gathering():
    #accepts no arguments
    #asks for a string a least 5 digits long
    #return string to string_manipulator()
    
    string = input('\nEnter a string that is at least 5 digits long: ')
    
    while len(string) <= 4:
        string = input('\nEnter a string that is AT LEAST 5 digits long: ')
    else:
        return string
      
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
        
    
    return new_string

def menu():
    #menu accepts no arguments
    #it creates a menu allowing user to choose which operation to perform
    
    
    print("1.) Input a string")
    print("2.) Reverse a string")
    print("3.) Count characters")
    print("4.) Replace characters")
    print("5.) Analyze a string")
    print("6.) Exit")
    
    choice = input("\nPlease choose an option (1-6): ")
    
    if choice.isdigit() == False:
        choice = input("\nOops! You didn't enter a number.\n\nPlease choose an option (1-6): ")
    
    return int(choice)

def string_reversal(string):
    #string_reversal accepts a string as an argument
    #it returns its reversed form
    
    reverse = string [::-1]
    
    return reverse


def string_analysis(string):
    
    #assign capitals and lowercase vowels and consanants
    consanant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowel = ['a','e','i','o','u']
    vowel2 = ['A','E','I','O','U']
    consanant2 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    specchar = ['&','*','(',')','+','=','_','-','|','\\','{','}','[',']',';',':','<',',','>','.','?','/','"',"'",'^','%','$','#','@','!','`','~']
    
    #palindrome?
    
    vowel_count = 0
    consonant_count = 0
    
    for character in string:
        if character in specchar:
            string = string.strip(character)
    for thing in string:
        if thing in vowel or thing in vowel2:
            vowel_count += 1
        elif thing in consanant or thing in consanant2:
            consonant_count += 1
        
        
    
    gnirts = string[::-1]
    #assign a counter
    counter = 0
    #remove spaces
    string2 = string.strip(' ')
    
    #find amount of characters in string
    for letter in string2:
        if letter in consanant or letter in vowel or letter in consanant2 or letter in vowel2:
            counter += 1 #update the counter
        
        
    print('There are', counter, 'total letters in your string.') #print the data
    
    #find if palindrome
    if string == gnirts:
        print('It is a palindrome.')
    else:
        print('It is not a palindrome.')
    print('There are', vowel_count, 'vowels in the string.') 
    print('There are', consonant_count, 'consonants in your string.')

