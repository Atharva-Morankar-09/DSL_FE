# Linear Search and Sentinel Search
# Linear Search

"""def linear_search(a,n,ele):
    for i in range(0, n):
        if(a[i]==ele):
            return i
    return -1

a =[]
n = int(input("Enter the total number of students who attended -  "))
for i in range(0, n):
    a.append(int(input("Enter the Roll Number - ")))

ele = int(input("Enter the roll number you want to find - "))

answer = linear_search(a, n, ele)

if(answer == -1):
    print("Student was absent ")
else:
    print("Student was present at ", answer)"""

# Sentinel Search

"""def sentinel_search(arr,n,key):
    end = arr[n-1]
    arr[n-1] = key
    i = 0
    while(arr[i]!=key):
        i += 1
    arr[n-1] = end
    if((i < n-1) or arr[n-1]==key):
        return i
    else:
        return -1


arr = []
n = int(input("Enter total number of students who attended - "))
for i in range(0,n):
    arr.append(int(input("Enter the Roll Number - ")))

key = int(input("Enter the Roll Number you want to find - "))

result = sentinel_search(arr, n, key)
if(result == -1):
    print("Student was absent ")
else:
    print("Student was present at ", result)"""

# Both

arr = []
n = int(input("Enter total number of students who attended - "))
for i in range(0, n):
    arr.append(int(input("Enter the Roll Number - ")))
print("Students Present were ", arr)
print("")
print("1)Using Linear Search")
print("2)Using Sentinel")
print("3)EXIT")
print("")

def mainMenu():
    key = int(input("Enter the Roll Number you want to find - "))
    print("")
    x = int(input("Enter your choice - "))
    print("")
    if(x==1):
        linear_search(arr, n, key)
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            print("")
            mainMenu()
        else:
            print("Thanks for using the program")
    elif(x==2):
        sentinel_search(arr, n, key)
        a = input("Do you want to continue (yes/no) : ")
        if a == "yes":
            print("")
            mainMenu()
        else:
            print("Thanks for using the program")
    elif (x==3):
        print("Thanks for using the program")
        exit()
    else:
        print("Enter Valid Number")
        mainMenu()


def sentinel_search(arr,n,key):
    end = arr[n-1]
    arr[n-1] = key
    i = 0
    while(arr[i]!=key):
        i += 1
    arr[n-1] = end
    if((i < n-1) or arr[n-1]==key):
        print("Student", key, "was present at ", i)
    else:
        print("Student was absent ")


def linear_search(arr,n,key):
    for i in range(0, n):
        if(arr[i]==key):
            print("Student", key, "was present at ", i)
            return 1
    print("Student was absent ")

mainMenu()
