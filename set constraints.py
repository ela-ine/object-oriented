import Tkinter # built-in Python graphics library
import random
import math
import abc

game_objects = []

class Shape:
    __metaclass__ = abc.ABCMeta
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.x_speed = random.randint(1, 5)
        self.y_speed = random.randint(1,5)
        self.color = '#{0:0>6x}'.format(random.randint(00,16**6))
        self.size = random.randint(30,100)
        self.width = random.randint(30,100)
        self.length = random.randint(30,100)
        self.h = random.randint(30,100)
        self.z = random.randint(30,100)
        self.numSides = random.randint(3,10)

    def update(self):

        self.x += self.x_speed
        self.y += self.y_speed
        self.h += self.x_speed

    def numSides(self):
        pass

class Circle(Shape):
    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color, outline="black")


def addCircle(event):

    global game_objects
    game_objects.append(Circle(event.x, event.y))


class Rectangle(Shape):
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color, outline="black")

def addRectangle(event):

    global game_objects
    game_objects.append(Rectangle(event.x, event.y))

class Triangle(Shape):
    def draw(self, canvas):
        canvas.create_polygon(self.x, self.y, self.x+self.width, self.y+self.length, self.x+self.h, self.y+self.z,
                            fill=self.color, outline="black")

def addTriangle(event):

    global game_objects
    game_objects.append(Triangle(event.x, event.y))

class Polygon(Shape):

    def draw(self,canvas):
        random_polygon = []

        for side in range(self.numSides):
            #random_polygon.append(self.y + random.randint(30,100) * math.sin(2 * math.pi / numSides))
            #random_polygon.append(self.x + random.randint(30,100) * math.cos(2 * math.pi / numSides))
            random_polygon.append(self.x + self.z * math.sin(side * 2 * math.pi / self.numSides))
            random_polygon.append(self.y + self.z * math.cos(side * 2 * math.pi / self.numSides))
        #random_polygon.append()
        canvas.create_polygon(*random_polygon, fill=self.color)

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

    delay = 33
    canvas.after(delay, draw, canvas)


if __name__ == '__main__':

    # create the graphics root and a 400x400 canvas
    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=800, height=800)
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
