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
        self.space = 100

    def draw(self, canvas, x, y):
        canvas.create_oval(x, y, x + self.size, y + self.size, fill = self.color)
    def arrange(self):
        for n in range(self.number):
            x = (n % 3) * (self.size+ self.space) + 150
            y = (math.floor(n/3) + 1) * self.space
            Circles.draw(self, canvas, x, y)
    @staticmethod
    def coordinates(n):
        return ((n % 3) * (100 + 100) + 150, (math.floor(n/3) + 1) * 100)

def addCircles(event):
    global gameobjects
    gameobjects.append(Circles(event.x, event.y))


class Cat:
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.color = '#6EDFFF'
        self.size = 50
        self.count = 0 #milliseconds
        self.round = 0
        self.visible = False

    def draw(self, canvas, x, y):
        if self.count == 0: # makes the cat appear
            self.x = x
            self.y = y
            self.visible = False
            self.round += 1
            self.count = 150 - self.round
        else:
            canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size,
                               fill=self.color) # this needs to be inside one of the Circles
            self.visible = True
            self.count -= 1

    def click(self, event):
        if self.x < event.x < self.x + self.size and self.y < event.y < self.y + self.size and self.count >= 0:
            global score
            score += 1
            self.visible = False
            self.count = 0
            print "score = %d" % score
        else:
            global heart
            heart -= 1
            print "hearts = %d" % heart
            #if heart <= 0:
                #print "GAME OVER"
                #reset()


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
    circlenumber = random.randint(0, Circles.number)
    x, y = Circles.coordinates(circlenumber)

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
    root.bind('<Button-1>', cat.click) # cat.Click shouldn't be bound to Button-1... define 2 separate f(x)?
    circles = Circles(canvas)
    draw(canvas, cat)
    root.mainloop()
