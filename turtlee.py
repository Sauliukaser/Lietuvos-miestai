from turtle import Turtle

class Marking(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def dot_mark(self, location):
        self.color("red")
        self.goto(location)
        self.dot(14)

    def name_location_1(self, location, city):
        self.goto(location)
        self.color("black")
        self.write(city, font=("Arial", 13, "bold"))

    def name_location_2(self, location, city):
        self.color("black")
        self.goto(location[0] - 22, location[1] + 9)
        self.write(city, font=("Arial", 13, "bold"))

