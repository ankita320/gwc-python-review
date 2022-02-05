# GOAL: Create your own turtle race with your own features!

from turtle import *
import turtle

# Feel free to customize your screen size!
screen = turtle.Screen()
screen.setup(2500, 2500)
screen.bgcolor("aliceblue")

speed(0) # turtle moves as quickly as possible
penup() # move turtle without leaving tracks
        # similar to NetLogo's pu function to pick pen up
goto(150, 150)

# If you want to try making a checkerboard at the end of the race!
def black():
  pd()
  fillcolor('pink')
  begin_fill()
  for i in range(4):
    turtle.forward(15)
    turtle.right(90)
  end_fill()
  

 
 
  # TO DO: try making one black square
  # Hint: how many sides does a square have?

def white():
  # TO DO: try making one white square
  # Hint: this should be the same as black()
  pd()
  fillcolor('turquoise')
  begin_fill()
  for i in range(4):
    turtle.forward(15)
    turtle.right(90)
  end_fill()
  
# NOTE: i and j keep track of the position of the turtle
# s keeps track of which color the square should be
j = 140
for rows in range(11): # 11 represents the number of rows
    if rows % 2: # To determine which color square to start with
      s = 0 
    else:
      s = 1
    i = 180
    for step in range(3): # 3 represents the number of squares per row
      pu()
      goto(i, j) # Go to the correct position

      # Starting to alternate the different color squares using the functions using modulus 
      if s % 2 == 0:
        black()
      else:
        white()
      i = i + 15
      s = s + 1 # NOTE: don't forget to increment it by one so it could alternate colors
    j = j - 15


# GOAL: Create your own turtle race with your own features!


# Feel free to customize your screen size!

# keep track of all the turtles in the race!
turtles = []

# Initalize your turtle
# What color and shape do you want your turtle to be? 
# Where should it start?
turtle_name = turtle.Turtle()
competitor0 = turtle.Turtle()
lala = turtle.Turtle()
circle = turtle.Turtle()
turtle_name.pu()
turtle_name.goto(-160, 100)
turtle_name.pendown()


competitor0.pu()
competitor0.goto(-160, 120)
competitor0.pendown()


lala.pu()
lala.goto(-160, 30)
lala.pendown()


circle.pu()
circle.goto(-160, -100)
circle.pendown()


turtles.append(turtle_name)
turtles.append(competitor0)
turtles.append(lala)
turtles.append(circle)




def pink():
  pd()
  fillcolor('red')
  begin_fill()
  for i in range(8):
    competitor0.forward(20)
    competitor0.right(45)
  end_fill()
pink()


def red():
  pd()
  fillcolor('red')
  begin_fill()
  for i in range(5):
    lala.forward(10)
    lala.right(72)
  end_fill()
red()

def blue():
  pd()
  fillcolor('red')
  begin_fill()
  for i in range(360):
    circle.forward(10)
    circle.right(1)
  end_fill()
blue()





# We don't want a race of one though.
# TO DO: Add some more turtles to the competition!
# <--insert code here-->

# TODO: Make the turtles move and find the winner! Stop the race when a turtle wins (break can stop a loop)
# Hint: turtle.xcor() lets you access the x coordinate of a turtle

# NOTE: There are several different ways to do this! 
# Here's an example of what you could do:
for i in range(0): # What parameter should range() be?

  # TO DO: How can we make the turtles move randomly so we don't know the outcome of the race?
  # Hint: You can use another library!
  turtle_name.forward()
