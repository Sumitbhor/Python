class Stack:
    def __init__(self):
        self.elements= [None]*5
        self.top =-1 
    def push(self,element):
        if self.top< len(self.elements)-1 :
           self.top += 1
           self.elements[self.top]= element
        else:
            print("stack is overflow")
    def pop(self):
        if self.top== -1:
            print("stack is empty ")
        element=self.elements[self.top]
        self.top -= 1
        return element
    def is_empty(self):
        return self.top == -1
    
    def clear(self):
        self.top = -1 
    
class TextEditor:
    def __init__(self):
        self.undoStack= Stack()
        self.redoStack= Stack()
        self.document =[None]*5
        self.docIndex= -1 
    
    def makeChange(self, text ):
        if self.docIndex< len(self.document)-1 :
            self.docIndex += 1
            self.document[self.docIndex]= text
            self.undoStack.push(text)
            self.redoStack.clear()
            print("change added ")
        else :
            print("documet is full")
    
    def undoAction(self):
        if self.undoStack.is_empty():
            print("empty")
        else : 
            change= self.undoStack.pop()
            self.redoStack.push(change) 
            self.document[self.docIndex]=None
            self.docIndex-= 1
            print ("undo perform ")

    def redoAction(self):
        if self.redoStack.is_empty():
            print("empty")
        else: 
            change = self.redoStack.pop()
            if self.docIndex < len(self.document)-1:
                self.docIndex+=1
                self.document[self.docIndex]=change
                self.undoStack.push(change)
                print("redo perform")
            else:
                print("document is full ")
    def display(self):
        print("current state ")
        if self.docIndex == -1:
            print("document is empty ")
        else :
            for i in range (self.docIndex+1):
                print(self.document[i]) 
        print() 

def main():
    editor= TextEditor()
    while True:
        print("Options:")
        print("1. Make a Change")
        print("2. Undo")
        print("3. Redo")
        print("4. Display Document")
        print("5. Exit")
        choice = int(input("enter your choice: "))
        if choice ==1 :
            text = input("enter text to add ")
            editor.makeChange(text)
        elif choice == 2 :
            editor.undoAction()
        elif choice == 3 :
            editor.redoAction()
        elif choice == 4 :
            editor.display()
        elif choice == 5:
            break
        else : 
            print("invalid input ")
main()
