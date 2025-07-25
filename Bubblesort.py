def bubbleSort(arr, n):
    for i in range (n) :
            for j in range (n-i-1) :
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr
        
arr=[]
n= int(input("Enter How many elements you want add in array :"))
for a in range (n):
    element= int(input(f"enter your element {a+1} "))
    arr.append(element)

sortedArr = bubbleSort(arr, n)
print(sortedArr)

