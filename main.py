import turtle as t 
import random

tim = t.Turtle()
t.colormode(255)
t.speed("fast")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def create_spirograph(gap):
  for _ in range(360 // gap):
      tim.color(random_color())
      tim.circle(50)
      current_heading = tim.heading()
      tim.setheading(current_heading + gap)

create_spirograph(10)

screen = t.Screen()
screen.exitonclick()