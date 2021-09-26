
"""In a class, some student’s play cricket, some students play badminton and some students play football.
Write a Python program using functions to compute following: -

a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)
"""

ALL = []
Cricket = []
Badminton = []
Football = []
Cricket_Badminton = []
play_either_Cricket_or_Badminton = []
play_neither_Cricket_nor_Badminton = []
Cricket_Football_not_Badminton = []

numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS PLAYING CRICKET : "))
for i in range(numofstudents):
    total = input("Enter the Student names : ")
    Cricket.append(total)

numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS PLAYING BADMINTON : "))
for i in range(numofstudents):
    total = input("Enter the Student names : ")
    Badminton.append(total)

numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS PLAYING FOOTBALL : "))
for i in range(numofstudents):
    total = input("Enter the Student names : ")
    Football.append(total)

for n1 in Cricket:
    ALL.append(n1)
for n1 in Badminton:
    if n1 not in Cricket:
        ALL.append(n1)
for n1 in Football:
    if n1 not in Badminton:
        if n1 not in Cricket:
            ALL.append(n1)
print("ALL STUDENTS ARE ", ALL)

def mainMenu():

    print(" ")
    print("1. List of common Students who play both Cricket and Badminton")
    print("2. List of Students who play either Cricket or Badminton not both")
    print("3. List of Students who play neither Cricket or Badminton")
    print("4. List of Students who play Cricket and Football but not Badminton")
    print("5. Exit")

    print(" ")
    choice = int(input("Enter Your Choice: "))

    if (choice == 1):
        print(" ")
        play_both_Cricket_and_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")

    elif (choice == 2):
        print(" ")
        either_Cricket_or_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")
    elif (choice == 3):
        print(" ")
        neither_Cricket_nor_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")
    elif (choice == 4):
        print(" ")
        play_Cricket_Football_not_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")
    elif (choice == 5):
        exit()
    else:
        print("Enter Valid Number")


def play_both_Cricket_and_Badminton():
    for n1 in Cricket:
        for n2 in Badminton:
            if n1 == n2:
                Cricket_Badminton.append(n1)
    print("List of common Students who play both Cricket and Badminton are : ", Cricket_Badminton)

def either_Cricket_or_Badminton():
    for n1 in Cricket:
        if n1 not in Badminton:
          play_either_Cricket_or_Badminton.append(n1)
    for n2 in Badminton:
        if n2 not in Cricket:
          play_either_Cricket_or_Badminton.append(n2)
    print("List of Students who play either Cricket or Badminton are : ", play_either_Cricket_or_Badminton)

def neither_Cricket_nor_Badminton():
    for n1 in Football:
      if n1 not in Badminton:
          if n1 not in Cricket:
              play_neither_Cricket_nor_Badminton.append(n1)
    print("List of Students who play neither Badminton nor Cricket are : ", play_neither_Cricket_nor_Badminton)

def play_Cricket_Football_not_Badminton():
    for n1 in Cricket:
        if n1 in Football:
            if n1 not in Badminton:
                Cricket_Football_not_Badminton.append(n1)
    print("List of Student who play Cricket and Football but not Badminton", Cricket_Football_not_Badminton)

mainMenu()


"""class_SEA = []
numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS : "))
for i in range(numofstudents):
    total = input("Enter the Student number " + str(i + 1) + " name : ")
    class_SEA.append(total)

class_SEA = ["RAKESH", "MAHESH", "ATHARVA", "AKASH", "SAYYED", "TANISHQ", "JOSHI", "VISHAL", "BASU", "SAHIL"]
print("Total Student sin SE C class are...", class_SEA)

cricket = ["KUNAL", "ANSHU", "TANISHQ", "PARTH" ]
print("Students who play Cricket = ", cricket)

badminton = ["ATHARVA", "SAYYED", "TANISHQ", "PARTH"]
print("Students who play Badminton", badminton)

football = ["DEVANG", "JOSHI"]
print("Students who play Football", football)"""

# creating empty lists
"""ALL = []
common = []
Cricket = []
Badminton = []
Football = []
only_Cricket = []
only_Badminton = []
Cricket_Badminton = []
play_neither_Cricket_nor_Badminton = []
Cricket_Football = []
Cricket_Football_not_Badminton = []


numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS PLAYING CRICKET : "))
for i in range(numofstudents):
    total = input("Enter the Student names : ")
    Cricket.append(total)

numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS PLAYING BADMINTON : "))
for i in range(numofstudents):
    total = input("Enter the Student names : ")
    Badminton.append(total)

numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS PLAYING FOOTBALL : "))
for i in range(numofstudents):
    total = input("Enter the Student names : ")
    Football.append(total)

ALL.append(Cricket,Football,Badminton)
ALL.append(Football)
ALL.append(Badminton)
print("TOTAL SPORTS PLAYERS NAMES ARE  \n", Cricket,Football,Badminton)




def mainMenu():

    print(" ")
    print("1. List of common Students who play both Cricket and Badminton")
    print("2. List of Students who play either Cricket or Badminton not both")
    print("3. List of Students who play neither Cricket or Badminton")
    print("4. List of Students who play Cricket and Football but not Badminton")
    print("5. Exit")

    print(" ")
    choice = int(input("Enter Your Choice: "))

    if (choice == 1):
        print(" ")
        play_both_Cricket_and_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")

    elif (choice == 2):
        print(" ")
        either_Cricket_or_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")
    elif (choice == 3):
        print(" ")
        neither_Cricket_nor_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")
    elif (choice == 4):
        print(" ")
        play_Cricket_Football_not_Badminton()
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            mainMenu()
        else:
            print("Thanks for using the program")
    elif (choice == 5):
        exit()
    else:
        print("Enter Valid Number")


def play_both_Cricket_and_Badminton():
    for num in Cricket:
        for n1 in Badminton:
            if num == n1:
                common.append(num)
    print("List of common Students who play both Cricket and Badminton are : ", common)


def either_Cricket_or_Badminton():
    for num in Cricket:
        flag = 0
        for n1 in Badminton:
            if (num == n1):
                flag = 1
        if flag == 0:
            only_Cricket.append(num)
    print("List of Students who play only Cricket are : ", only_Cricket)

    for num in Badminton:
        flag = 0
        for n1 in Cricket:
            if (num == n1):
                flag = 1
        if (flag == 0):
            only_Badminton.append(num)
    print(" ")
    print("List of Students who play only Badminton are : ", only_Badminton)


def neither_Cricket_nor_Badminton():
    for num in Cricket:
        Cricket_Badminton.append(num)
    for no in Badminton:
        flag = 0
        for n1 in Cricket_Badminton:
            if no == n1:
                flag = 1
        if flag == 0:
            Cricket_Badminton.append(no)
    print("List of Students who play both Cricket and Badminton are :", Cricket_Badminton)

    for num in Football:
        flag = 0
        for n1 in Cricket_Badminton:
            if num == n1:
                flag = 1
        if flag == 0:
            play_neither_Cricket_nor_Badminton.append(num)
    print(" ")
    print("List of Students who play neither Badminton nor Cricket are : ", play_neither_Cricket_nor_Badminton)


def play_Cricket_Football_not_Badminton():
    for num in Cricket:
        Cricket_Football.append(num)
    for no in Football:
        flag = 0
        for n1 in Cricket_Football:
            if no == n1:
                flag = 1
        if flag == 0:
            Cricket_Football.append(no)
    print("List of Students who play Cricket and Football ", Cricket_Football)

    for num in Cricket_Football:
        flag = 0
        for no in Badminton:
            if no == num:
                flag = 1
        if flag == 0:
            Cricket_Football_not_Badminton.append(num)
    print("")
    print("List of Student who play Cricket and Football but not Badminton", Cricket_Football_not_Badminton)"""
