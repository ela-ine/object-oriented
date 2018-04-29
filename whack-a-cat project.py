import Tkinter
import math
import random

gameobjects = []
score = 0
heart = 3

class Circles:
    number = 9
    def __init__(self, canvas):
        self.size = 100
        self.color = '#000000'

    def draw(self, canvas, x, y):
        canvas.create_oval(x, y, x + self.size, y + self.size, fill = self.color)
    def arrange(self):
        for n in range(self.number):
            x = (n % 3) * (self.size + 50) + 150
            y = (math.floor(n/3) + 1) * 120
            Circles.draw(self, canvas, x, y)
    @staticmethod
    def coordinates(n):
        return ((n % 3) * (100 + 50) + 150, (math.floor(n/3) + 1) * 120)

def addCircles(event):
    global gameobjects
    gameobjects.append(Circles(event.x, event.y))


class Cat:
    clickstatus = False
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.color = '#6EDFFF'
        self.size = 80
        self.count = 0 #counts the milliseconds that the cat is visible
        self.round = 0
        self.visible = False

    def draw(self, canvas, x, y):
        if self.count == 0: # makes the cat disappear
            self.x = x
            self.y = y
            self.visible = False
            self.round += 1
            self.count = 100 - self.round
        else:
            canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size,
                               fill=self.color) # this needs to be inside one of the Circles
            self.visible = True
            self.count -= 1
            clickstatus = False

        if self.count == 0 and clickstatus == False:
            global heart
            heart -= 1
        else:
            pass

    def click(self, event): #need a function that docks a heart for not clicking at all
        clickstatus = True
        if self.x < event.x < self.x + self.size and self.y < event.y < self.y + self.size and self.count >= 0:
            global score
            score += 1
            self.visible = False
            self.count = 0
        else:
            global heart
            heart -= 1


def addCats(event):
    global gameobjects
    gameobjects.append(Cat(event.x, event.y))

def draw(canvas, cat):
    canvas.delete(Tkinter.ALL)

    global gameobjects, circles
    circles.arrange()

    for gameobject in gameobjects:
        gameobject.update()
        gameobject.draw(canvas)
    circlenumber = random.randint(1, Circles.number)
    x, y = Circles.coordinates(circlenumber)

    canvas.create_text(50, 40, text = "score = %d" % score)
    canvas.create_text(52, 70, text = "hearts = %d" % heart)

    if heart <= 0:
        canvas.create_text(300, 300, text = "GAME OVER") #need to make this project for more than 1 frame
        reset(canvas)

    cat.draw(canvas, x, y)
    delay = 33
    canvas.after(delay, draw, canvas, cat)

def reset(event):
    global gameobjects
    gameobjects = []
    global score
    score = 0
    global heart
    heart = 3

if __name__ == '__main__':

    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=800, height=800)
    canvas.pack()
    cat = Cat(canvas)
    root.bind('<Button-1>', cat.click)
    circles = Circles(canvas)
    draw(canvas, cat)
    root.mainloop()
