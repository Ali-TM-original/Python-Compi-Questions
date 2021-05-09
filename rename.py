# First Name Last Name
# StudentID
# Department


from random import randrange


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
