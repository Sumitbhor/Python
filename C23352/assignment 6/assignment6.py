 
TABLE_SIZE = 10
#hashtable = [[None, None] for _ in range(TABLE_SIZE)]
hashtable = [[None, None] ]*10

def hash_function(key):
    return key % TABLE_SIZE

def insert(key, value):
    index = hash_function(key)
    original_index = index

    while hashtable[index][0] !=  None and hashtable[index][0] != key:
        index = (index + 1) % TABLE_SIZE
        if index == original_index:
            print("Hashtable is full!")
            return
    hashtable[index] = [key, value]
    

def search(key):
    index = hash_function(key)
    original_index = index

    while hashtable[index][0] is not None:
        if hashtable[index][0] == key:
            return hashtable[index][1]
        index = (index + 1) % TABLE_SIZE
        if index == original_index:
            break
    return None
def delete(key):
    index= hash_function(key)
    ogindex = index
    while hashtable[index][0]!= None:
        if hashtable[index][0]==key:
            hashtable[index]=[None, None]
            return
        index=(index+1)%TABLE_SIZE 

    print("number not found")
def display():
    print(hashtable)

'''while(1):
    print("Menu*")
    print("Choose the appropriate option..")
    print("1 : Insert")
    print("2 : Search")
    print("3 : Print")
    print("4 : Exit")
    print("")
    choice = int(input("Select..any one"))

    if choice == 1:
        x = int(input("Enter key: "))
        y = input("Enter value: ")
        insert(x, y)
    elif choice == 2:
        x = int(input("Enter key to search: "))
        result = search(x)
        if result is not None:
            print(f"Value found: {result}")
        else:
            print("Key not found.")
    elif choice == 3:
        display()
    else:
        exit()
'''

# # Example usage
insert(100,"apple")
insert(200,"banana" )
insert(300,"grape")


delete(100)
display()