from turtle import Turtle

class Zymejimas(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def taskas(self,pozicija):
        self.color("red")
        self.goto(pozicija)
        self.dot(14)

    def pavadinimas(self,pozicija,miestas):
        self.goto(pozicija)
        self.color("black")
        self.write(miestas, font=("Arial", 13, "bold"))

    def pavadinimas_2(self, pozicija, miestas):
        self.color("black")
        self.goto(pozicija[0]-22, pozicija[1]+9)
        self.write(miestas, font=("Arial", 13, "bold"))

