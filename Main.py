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