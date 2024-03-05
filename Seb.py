def string_analysis():
    
    #assign capitals and lowercase vowels and consanants
    consanant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowel = ['a','e','i','o','u']
    vowel2 = ['A','E','I','O','U']
    consanant2 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    specchar = ['&','*','(',')','+','=','_','-','|','\\','{','}','[',']',';',':','<',',','>','.','?','/','"',"'",'^','%','$','#','@','!','`','~']
    strong = 'tacocat.' #assign a string for testing
    #palindrome?
    counter2 = 0
    counter3 = 0
    for character in strong:
        if character in specchar:
            strang = strong.strip(character)
    for thing in strang:
        if thing in vowel or thing in vowel2:
            counter2 += 1
        elif thing in consanant or thing in consanant2:
            counter3 += 1
        
        
    
    gnorts = strang[::-1]
    #assign a counter
    counter = 0
    #remove spaces
    strong2 = strang.strip()
    
    #find amount of characters in string
    for letter in strong2:
        if letter in consanant or letter in vowel or letter in consanant2 or letter in vowel2:
            
            counter += 1 #update the counter
        
        
    print('There are', counter, 'total letters in your string.') #print the data
    
    #find if palindrome
    if strang == gnorts:
        print('It is a palindrome.')
    else:
        print('It is not a palindrome.')
    print('There are', counter2, 'vowels in the string.') 
    print('There are', counter3, 'consanants in your string.')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
string_analysis()