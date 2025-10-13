class point:
    def __init__(self,x,y):
        self.X=x
        self.Y=y
    def display(self):
        print(f"x coordinate :{self.X}, ycoordinate :{self.Y}")

class line:
    def __init__(self, pt1, pt2):
        self.startpoint= pt1
        self.endpoint= pt2

    def display(self):
        print