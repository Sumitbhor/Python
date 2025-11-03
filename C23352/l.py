class Node():
    def __init__(self,rollNo, Name, Marks):
        self.rollNo = rollNo 
        self.Name = Name
        self.Marks = Marks
        self.next = None

class linkeslist ():
    def __init__(self):
        self.head =None
    def addStudent(self,rollNO, Name,Marks):
        newNode = Node(rollNO, Name, Marks)
        if self.head==None:
            self.head = newNode
            return
        current = self.head
        while current.next!=None:
            current = current.next
        current.next = newNode

    def delete(self, rollNo):
        current= self.head
        if 
    def displaylist(self):
        if self.head == None :
            print ("list is empty" )
            return
        current = self.head 
        while current != None:
            print(current.Name, current.rollNo, current.Marks,"->")
            current = current.next
    


list = linkeslist()
list.addStudent(1, "sumit", 88)
list.addStudent(2, "sanika",87)
list.addStudent(3, "parikshit", 28)
list.addStudent(4, "ashwin", 38)
list.displaylist()

