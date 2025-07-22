def menu():
    print("1.Linear search ")
    print("2.Binary search ")
    print("3.Exit ")

def LinearSearch(arr, number):
    for i in range (len(arr)):
       if arr[i] == number:
            return i 
    return -1  

def BinarySearch(arr, number):
    arr.sort()  
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < number:
            low = mid + 1
        elif arr[mid] > number:
            high = mid - 1
        else:
            return mid
    return -1

arr=[]
for i in range(5):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)


print(arr)

while True:
    number=int(input("which number you want to find : "))
    menu()
    choice =int(input("enter your choice: "))
    if choice==1:
        index =LinearSearch(arr, number)
        if index != -1 :    
            print("number find at index ",index)
        else:
            print("number not found ")
    elif choice==2:
        index =BinarySearch(arr, number )
        if index != -1 :    
            print("number find at index: ",index )
        else:
            print("number not found ")
    elif choice==3:
        break 
    else :
        print("invalid input ")


