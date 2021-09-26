marksinFDS = []
numofstudents = int(input("ENTER THE NUMBER OF STUDENTS IN THE CLASS : "))
for i in range(numofstudents):
    marks = input("Enter the Marks for the Subject " + str(i + 1) + " : ")
    marksinFDS.append(marks)


def average(marksinFDS):
    sum = 0
    cnt = 0
    for i in range(len(marksinFDS)):
        sum += marksinFDS[i]
        cnt += 1
    avg = sum / cnt
    return (avg)


def min(marksinFSD):
    for i in range(len(marksinFSD)):
        if marksinFSD[i] != 999:
            Min = marksinFSD[0]
            break
    for i in range(1, len(marksinFSD)):
        if marksinFSD[i] < Min:
            Min = marksinFSD[i]
    return (Min)


def max(marksinFSD):
    for i in range(len(marksinFSD)):
        if marksinFSD[i] != 999:
            Max = marksinFSD[0]
            break
    for i in range(1, len(marksinFSD)):
        if marksinFSD[i] > Max:
            Max = marksinFSD[i]
    return (Max)


def absent(marksinFSD):
    abs = 0
    for i in (marksinFSD):
        if i == "absent":
            abs += 1
    return (abs)


def maxfreq(marksinFSD):
    i = 0
    max = 0
    print("Number    |    Frequency")
    for j in marksinFSD:
        if (marksinFSD.index(j) == i):
            print(j, "    |    ", marksinFSD.count(j))
            if marksinFSD.count(j) > max:
                max = marksinFSD.count(j)
                mark = j
        i = i + 1
    return (max)


flag = 1
while flag == 1:
    print("\n...........SELECT ONE..........\n")
    print("1.Total and Average Marks of the class")
    print("2.Highest and Lowest Marks in the Class")
    print("3.Number of Students abesnt for the test")
    print("4.Marks with Highest Frequency")
    print("5.Exit\n")
    ch = int(input("ENTER YOUR CHOICE FROM 1 TO 5 : "))

    if (ch == 1):
        print("The Average marks are :", average(marksinFDS))
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using the program")

    elif (ch == 2):
        print("Highest score in class is : ", max(marksinFDS))
        print("Lowest score in class is : ", min(marksinFDS))
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using the program")

    elif (ch == 3):
        print("Number of students absent in class is : ", absent(marksinFDS))
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using the program")

    elif (ch == 4):
        print("Maximum frequency of marks is : ", maxfreq(marksinFDS))
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            flag = 1
        else:
            print("Thanks for using the program")

    elif (ch == 5):
        flag = 0

    else:
        print("**Enter valid number**")
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            flag = 1
        else:
            print("Thanks for using the program")