import Tkinter # built-in Python graphics library
import random
import math
import abc

game_objects = []

class Shape:
    __metaclass__ = abc.ABCMeta
    def __init__(self, x, y):
        # the following variables would be 'protected' if we were writing in java
        self.x = x
        self.y = y
        self.X_SPEED = random.randint(1, 5)
        self.Y_SPEED = random.randint(1,5)
        self.COLOR = '#{0:0>6x}'.format(random.randint(00,16**6))
        self.SIZE = random.randint(30,100)
        self.WIDTH = random.randint(30,100)
        self.LENGTH = random.randint(30,100)
        self.H = random.randint(30,100)
        self.Z = random.randint(30,100)
        self.NUM_SIDES = random.randint(3,10)

    def update(self):

        self.x += self.X_SPEED
        self.y += self.Y_SPEED
        self.H += self.X_SPEED


class Circle(Shape):
    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + self.SIZE, self.y + self.SIZE,
                           fill=self.COLOR, outline="black")


def addCircle(event):

    global game_objects
    game_objects.append(Circle(event.x, event.y))


class Rectangle(Shape):
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.SIZE, self.y + self.SIZE,
                           fill=self.COLOR, outline="black")

def addRectangle(event):

    global game_objects
    game_objects.append(Rectangle(event.x, event.y))

class Triangle(Shape):
    def draw(self, canvas):
        canvas.create_polygon(self.x, self.y, self.x+self.WIDTH, self.y+self.LENGTH, self.x+self.H, self.y+self.Z,
                            fill=self.COLOR, outline="black")

def addTriangle(event):

    global game_objects
    game_objects.append(Triangle(event.x, event.y))

class Polygon(Shape):

    def draw(self,canvas):
        random_polygon = [] # private

        for side in range(self.NUM_SIDES):
            random_polygon.append(self.x + self.Z * math.sin(side * 2 * math.pi / self.NUM_SIDES))
            random_polygon.append(self.y + self.Z * math.cos(side * 2 * math.pi / self.NUM_SIDES))
        canvas.create_polygon(*random_polygon, fill=self.COLOR)

def addPolygon(event):
        global game_objects
        game_objects.append(Polygon(event.x, event.y))




def reset(event):
    global game_objects
    game_objects = []


def draw(canvas):

    canvas.delete(Tkinter.ALL)

    global game_objects
    for game_object in game_objects:
        game_object.update()
        game_object.draw(canvas)

    delay = 33 # private
    canvas.after(__delay, draw, canvas)


if __name__ == '__main__':

    # create the graphics root and a 400x400 canvas
    root = Tkinter.Tk()
    canvas = Tkinter.canvas(root, width=800, height=800)
    canvas.pack()

    # if the user presses a key or the mouse, call our handlers
    root.bind('<Key-r>', reset)
    root.bind('<Button-2>', addCircle)
    root.bind('<Key-s>', addRectangle)
    root.bind('<Key-t>', addTriangle)
    root.bind('<Button-1>', addPolygon)

    # start the draw loop
    draw(canvas)

    root.mainloop() # keep the window open
