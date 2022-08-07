from turtle import *

pensize(10)
color("blue")

penup()
goto(-250, 100)
pendown()

# The letter 'T'
forward(200)
back(100)
right(90)
forward(200)

# Move to the next letter
penup()
back(200)
left(90)
forward(150)
pendown()
color("yellow")
pensize(20)

# The letter 'I'
right(90)
forward(200)

# Move to the next letter
penup()
back(200)
left(90)
forward(50)
pendown()
color("red")
pensize(30)

# The letter 'M'
right(90)
forward(200)
back(200)
left(30)
forward(150)
left(120)
forward(150)
right(150)
forward(200)
