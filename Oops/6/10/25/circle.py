class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"x={self.x}, y={self.y}")

class circle:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def draw(self):
        print(f"Center: ( {self.center.x}, {self.center.y} )")
        print(f"Radius: {self.radius}")
        print(f"Color: {self.color}")
c1 = point(23, 54)
c2 = point(77, 78)  
circle1 = circle(c1, 10, "red")
circle1.draw()
circle2 = circle(c2, 20, "blue")
circle2.draw()
