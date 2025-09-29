def bubbleSort(arr, n):
    for i in range (n) :
            for j in range (n-i-1) :
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr
        
arr=[]
n= int(input("Enter number of employee's :"))
for a in range (n):
    element= int(input(f"enter salary of employee {a+1} "))
    arr.append(element)

sortedArr = bubbleSort(arr, n)
print(sortedArr)
print("Top 5 salary's")
for b in range (n-1 ,n-6, -1):
    print(sortedArr[b])