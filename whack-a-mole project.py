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
        self.number = 9

    def draw(self, canvas, x, y):
        canvas.create_oval(x, y, x + self.size, y + self.size, fill = self.color)
    def arrange(self):
        for n in range(self.number):
            x = (n % 3) * (self.size + 50) + 150
            y = (math.floor(n/3) + 1) * 120
            Circles.draw(self, canvas, x, y)
    @staticmethod
    def coordinates(n):
        return ((n % 3) * (100 + 50) + 150 + 10, (math.floor(n/3) + 1) * 120 + 10)

def addCircles(event):
    global gameobjects
    gameobjects.append(Circles(event.x, event.y))


class Mole:
    clickstatus = False
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.color = '#6EDFFF'
        self.size = 80
        self.count = 0 #counts the milliseconds that the mole is visible
        self.round = 0
        self.visible = False

    def draw(self, canvas, x, y):
        clickstatus = False
        if self.count == 0: # makes the mole disappear
            self.x = x
            self.y = y
            self.visible = False
            self.round += 1
            self.count = 100 - self.round
        else:
            # img = Tkinter.PhotoImage(file = "/Users/elaine/Documents/cat.gif")
            # canvas.create_image(self.x, self.y, img)
            canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size,
                               fill=self.color)
            self.visible = True
            self.count -= 1
            clickstatus = False

        if self.count == 0 and clickstatus == False:
            global heart
            heart -= 1
        else:
            pass

    def click(self, event): #rewards point for clicking mole, docks a heart for not clicking at all
        clickstatus = True
        if self.x < event.x < self.x + self.size and self.y < event.y < self.y + self.size and self.count >= 0:
            global score
            score += 1
            self.visible = False
            self.count = 0
        else:
            global heart
            heart -= 1


def addMoles(event):
    global gameobjects
    gameobjects.append(Mole(event.x, event.y))

def draw(canvas, mole):
    canvas.delete(Tkinter.ALL)
    global gameobjects, circles
    circles.arrange()
    circlenumber = random.randint(1, Circles.number-1) # references one of the 9 circles
    x, y = Circles.coordinates(circlenumber) # calculates coordinates of randomly selected circle
    delay = 33

    for gameobject in gameobjects:
        gameobject.update()
        gameobject.draw(canvas)

    canvas.create_text(50, 40, text = "score = %d" % score)
    canvas.create_text(52, 70, text = "hearts = %d" % heart)

    mole.draw(canvas, x, y)
    canvas.after(delay, draw, canvas, mole)

    if heart <= 0:
        canvas.delete(Tkinter.ALL)
        canvas.create_text(400, 200, text = "GAME OVER", font = "Sans-serif 30 bold", justify = "center")
        canvas.create_text(400, 250, text = "CLICK TO PLAY AGAIN",font = "Sans-serif 20 italic", justify = "center")
        # need to reference click to reset(canvas)
        # if mole.clickstatus == True:
        reset(canvas)

def reset(event):
    global gameobjects
    gameobjects = []
    global score
    score = 0
    global heart
    heart = 3

if __name__ == '__main__':

    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=1200, height=1200)
    canvas.pack()
    mole = Mole(canvas)
    root.bind('<Button-1>', mole.click)
    circles = Circles(canvas)
    draw(canvas, mole)
    root.mainloop()
