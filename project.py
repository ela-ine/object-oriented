import Tkinter

gameobjects = []
score = []
heart = [3]

class Circles:
    def __init__(self, canvas):
        self.size = 50
        self.color = '#0'

    def draw(self, canvas, x, y):
        canvas.create_oval(x, y, x + self.size, y + self.size,
                           fill = self.color)
    def arrange():
        for x in range(0,2):
            draw(self, canvas, x * self.size + 2, 20)
            # still trying to figure out the y coordinate

def addCircles(event):
    global gameobjects
    gameobjects.append(Circles(event.x, event.y))


class Cat:
    def __init__(self, canvas):
        self.x = x
        self.y = y
        self.color = '#16776960'
        self.size = 30

    def draw(self,canvas): # eventually will hopefully be a sprite, but it's a circle for now
        canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color)

    # another thing to figure out: how to make the cats randomly appear in the holes at certain intervals

# def clickCat:
    # if cat is clicked (I don't know how to say this):
        # score = score + 1
    # else:
        # heart = heart - 1
        # if heart = 0:
            # print "GAME OVER"
        # else: continue???

def draw(canvas):
    canvas.delete(Tkinter.ALL)
    global gameobjects
    for gameobject in gameobjects:
        gameobject.update()
        gameobject.draw(canvas)

def reset(event):
    global gameobjects
    gameobjects = []
    global score
    score = []
    global heart
    heart = [3]

if __name__ == '__main__':

    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=800, height=800)
    canvas.pack()

    # root.bind('<Button-1>', clickCat)
    # how would I call the function to make the game board?

    draw(canvas)
    root.mainloop()
