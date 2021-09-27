

"""Write a Python program to compute following operations on String:

a) To display word with the longest length

b) To determines the frequency of occurrence of particular character in the string

c) To check whether given string is palindrome or not

d) To display index of first appearance of the substring

e) To count the occurrences of each word in a given string"""
# DSL Assignment 3 - String operations

string = input("Enter the string : ")

def mainMenu():
    print("")
    print("1.To display word with longest length")
    print("2.To determine frequency of occurrence of given character")
    print("3.To check whether list is palindrome or not")
    print("4.To display index of first appearance of substring")
    print("5.To count occurrences of each word in a given string")
    print("6.Exit")
    print(" ")
    choice = int(input("Enter Your Choice: "))

    if (choice==1):
        print(" ")
        longest_length()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")

    elif (choice==2):
        print(" ")
        freq_char()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")

    elif (choice==3):
        print(" ")
        palindrome()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")

    elif (choice==4):
        print(" ")
        index_substring()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")

    elif (choice==5):
        print(" ")
        occurrence()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")

    elif (choice==6):
        exit()

    else:
        print("Enter valid number")

def longest_length():
    list = string.split()
    longest_word = ''
    length = 0
    for i in list:
        if (len (i) > length):
            longest_word = i
            length = len(i)
    print("The word with largest length ", length, " is ", longest_word)

def freq_char():
    freq = 0
    char = input("Enter the character whose frequency you want to check : ")
    for i in string:
        if (char==i):
            freq+=1
    print("The frequency of ", char, " is ", freq)

def palindrome():
    list1 = string.split()
    list2 = list1[::-1]
    #print(list1)
    #print(list2)
    if (list1 == list2):
        print("String is a PALINDROME")
    else:
        print("String is NOT A PALINDROME")

def index_substring():
    """list1 = string.split()
    substring = input("Enter the substring : ")
    list2 = substring.split()
    for i in list1:
        if (list2 == list1):
            location = list1[i]
    print("The index of first appearance of substring is ", location)"""
    substring = input("Enter the substring : ")
    location = string.index(substring)
    print("The index of first appearance of substring is ", location)

def  occurrence():
    list1 = string.split()
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    for i in range(0,len(list2)):
            print("The '", list2[i], "' word occurs ", list1.count(list2[i]), " times")

mainMenu()



