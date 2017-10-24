import Tkinter # Python graphics library
import random

class Bird:

    def __init__(self, canvas, min_x_speed, max_x_speed, min_y_speed, max_y_speed, size):
        self.canvas = canvas
        # winfo gets us the current size of the canvas
        self.x = random.uniform(0, self.canvas.winfo_width())
        self.y = random.uniform(0, self.canvas.winfo_height())
        self.x_speed = random.uniform(self.min_x_speed, self.max_x_speed)
        self.y_speed = random.uniform(self.min_y_speed,self.max_y_speed)
        self.size = size
        self.fill_color = '#{0:0>6x}'.format(random.randint(00,16**6))
        self.min_x_speed = min_x_speed
        self.max_x_speed = max_x_speed

    def display(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.size*2, self.y + self.size,
                                     fill=self.fill_color)

class SoaringBird(Bird):

  def __init__(self, canvas):
    self.canvas = canvas
    self.min_x_speed = 1
    self.max_x_speed = 3
    self.min_y_speed = 0
    self.max_y_speed = 0
    self.size = 30.0
    Bird.__init__(self, self.canvas, self.min_x_speed, self.max_x_speed, self.min_y_speed, self.max_y_speed, self.size)

  def display2(self):
    self.canvas.create_oval(self.x, self.y, self.x + self.size*2, self.y + self.size,
                            fill=self.fill_color)
  def  move(self):
    self.x += self.x_speed

    # if off the right side of the screen,
    # move to just off the left side of the screen
    if (self.x > self.canvas.winfo_width()):
      self.x = -self.size



class FlittingBird(Bird):

  def __init__(self, canvas):
    self.canvas = canvas
    # winfo gets us the current size of the canvas
    self.min_x_speed = 2.0
    self.max_x_speed = 5.0
    self.min_y_speed = -1.0
    self.max_y_speed = 1.0
    self.size = 15.0
    Bird.__init__(self, self.canvas, self.min_x_speed, self.max_x_speed, self.min_y_speed, self.max_y_speed, self.size)


  def move(self):
    self.x += self.x_speed
    self.y += self.y_speed

    # if off the right side of the screen
    # move to just off the left side of the screen
    if (self.x > self.canvas.winfo_width()):
      self.x = -self.size

    # if off the top or bottom of the screen, reverse y speed
    if (self.y < -self.size or self.y > self.canvas.winfo_height()):
      self.y_speed = -self.y_speed

    # about 20% of the time, change speed a bit
    if (random.random() > 0.8):
      self.y_speed += random.uniform(-0.5, 0.5)
      self.y_speed = max(self.min_y_speed, self.y_speed)
      self.y_speed = min(self.max_y_speed, self.y_speed)

      self.x_speed += random.uniform(-0.5, 0.5)
      self.x_speed = max(self.min_x_speed, self.x_speed)
      self.x_speed = min(self.max_x_speed, self.x_speed)


class FallingFeather(Bird):

  def __init__(self, canvas):
    self.canvas = canvas
    # winfo gets us the current size of the canvas
    self.y = random.uniform(-self.canvas.winfo_height(), 0)
    self.min_x_speed = -1
    self.max_x_speed = 1
    self.min_y_speed = 0.5
    self.max_y_speed = 1.5
    self.size = 5.0
    Bird.__init__(self, self.canvas, self.min_x_speed, self.max_x_speed, self.min_y_speed, self.max_y_speed, self.size)


  def move(self):
    self.x += self.x_speed
    self.y += self.y_speed
    # if off the bottom of the screen, move to the top
    if (self.y > self.canvas.winfo_height()):
      self.y = -self.size

    # about 5% of the time,
    # or if going off the left or right of the screen,
    # reverse x direction
    if (random.random() > 0.95 or self.x < -self.size or self.x > self.canvas.winfo_width()):
      self.x_speed = -self.x_speed



if __name__ == '__main__':
    # create the graphics root and a 400x400 canvas
    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=600, height=400)
    canvas.pack()
    canvas.update() # need this for the canvas object to have the correct height set
    birds = []
    soaring = []
    for x in range(5):
        birds.append(FlittingBird(canvas))
        birds.append(FallingFeather(canvas))
        birds.append(FallingFeather(canvas))
    for x in range(5):
        soaring.append(SoaringBird(canvas))

    # define the draw loop
    def draw():
      canvas.delete(Tkinter.ALL)
      for bird in birds:
          bird.move()
          bird.display()
      for bird in soaring:
          bird.move()
          bird.display2()
      delay = 33 # milliseconds, so about 30 frames per second
      canvas.after(delay, draw) # call this draw function again after the delay

    # start the draw loop
    draw()

    root.mainloop() # keep the window open
