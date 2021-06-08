

from random import randrange

# QUESTION: 1
def merge_two_strings(s1: str, s2: str):
    string2 = s2[::-1]
    if len(s1) != len(string2):
        print("Length of strings not equal")
    else:
        result = ""
        x = zip(s1, string2)
        for a, b in x:
            result += a + b
        print(f"Result={result}")


# QUESTION: 2        
def decode(s: str):
    if s[0].isdigit():
        print("The String can not have Digit as first letter")
    else:
        print("Decoding...")
        result = ""
        for index, letter in enumerate(s):
            if letter.isdigit():
                x = s[index - 1] * (int(letter) - 1)
                result += x
            else:
                result += letter
        print(f"Result: {result}")


# QUESTION: 3        
def countTypes(s1: str):
    uppercase, lowercase, digits, special = 0, 0, 0, 0
    for i in range(len(s1)):
        if s1[i].isupper():
            uppercase += 1
        elif s1[i].islower():
            lowercase += 1
        elif s1[i].isdigit():
            digits += 1
        else:
            special += 1
    print(f"Uppercase chars={uppercase}")
    print(f"Lowercase chars={lowercase}")
    print(f"Digits={digits}")
    print(f"Symbol={special}")


# QUESTION: 4    
def lottery():
    randints = []
    userinpint = []
    userincount = 0
    counter = 0
    for i in range(6):
        randints.append(randrange(1, 50))
    while userincount < 6:
        usr = int(input("Please Enter a number: "))
        if int(usr) < 1 or int(usr) > 49:
            print(f"{usr} s not in the range [1,49]  try a different number !")
        if usr in userinpint:
            print(f"You entered  {usr} try a different number !")
        else:
            userincount += 1
            userinpint.append(usr)
    for i in randints:
        if i in userinpint:
            counter += 1
    randints.sort()
    userinpint.sort()
    print(f"Winning numbers are: {randints}")
    print(f"Your numbers are: {userinpint}")
    print(f"Congrats, you guessed {counter} number correctly.")
    

# QUESTION 5 Read Text File and output digits    
def find_numbers(file_name: str):
    """
    Here we initialize a variable called counter, initialized at top to make this a global variable inside the function
    """
    counter = 0
    # This creates an opened instance of the file
    with open(file_name) as f:
    # readlines() is a built in method to read content 1 by 1 line wise
        content = f.readlines()
    """ 
    since text files have ascii characters and utf-8 encoding a space in the document will be depicted as  
    "/n" but we dont want that. another python method strip() exists this removes any whitespace or "/n"
    from a string of characters.
    """   
    content = [x.strip() for x in content] 
    """
        since content variable will be storing all the content in a list we can loop through the list
        isdigit() is another python function that checks if you guessed it a string is a digit it returns
        true or false on conditions. those true or false states have been stored in chk variable
        so we can use if statements
        if the element in the list is a digit we add one to the counter 
        counter+=1 is the same as counter= counter+1
        otherwise if it is not a digit we do nothing
        in the end we pring the counter
    """
    for li in content:
        chk = li.isdigit()
        if chk:
            counter+=1
    print(counter)    
            
