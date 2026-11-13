import turtle


# Make a geometric rainbow pattern.
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'red','indigo','brown','white']

aiden = turtle.Turtle()
aiden.speed(10)
turtle.bgcolor('black')

# Make 36 hexagons, each 10 degrees apart.
for _ in range(36):
	# Make a hexagon by repeating 6 times.
	for i in range(9):
		aiden.color(colors[i])
		aiden.forward(100)
		aiden.left(60)
	aiden.right(10)

# Get ready to draw 36 circles.
aiden.penup()
aiden.color('white')

# Repeat 36 times to match the 36 hexagons.
for _ in range(36):
	aiden.forward(220)
	aiden.pendown()
	aiden.circle(5)
	aiden.penup()
	aiden.backward(220)
	aiden.right(10)

# Hide turtle to finish the drawing.
aiden.hideturtle()
turtle.done()
