import math
import turtle
from datetime import datetime


screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor('#080b14')
screen.title('NEON TIME')
screen.tracer(False)

face = turtle.Turtle(visible=False)
face.speed(0)
hands = turtle.Turtle(visible=False)
hands.speed(0)
labels = turtle.Turtle(visible=False)


def draw_clock_face() -> None:
    for radius, color, width in [(245, '#26334d', 3), (232, '#12566b', 2)]:
        face.penup()
        face.goto(0, -radius)
        face.color(color)
        face.pensize(width)
        face.pendown()
        face.circle(radius)

    for mark in range(60):
        angle = math.radians(90 - mark * 6)
        mark_x = 220 * math.cos(angle)
        mark_y = 220 * math.sin(angle)
        face.penup()
        face.goto(mark_x, mark_y)
        if mark % 5:
            face.color('#53f3ff')
            face.dot(3)
        else:
            face.color('#ff9f43')
            face.setheading(90 - mark * 6)
            face.pensize(8)
            face.forward(20)
            face.backward(20)


def draw_hand(angle: float, length: float, width: int, line_color: str, fill_color: str) -> None:
    hands.penup()
    hands.goto(0, 0)
    hands.setheading(angle)
    hands.color(line_color, fill_color)
    hands.pensize(width)
    hands.pendown()
    hands.forward(length)
    hands.left(150)
    hands.begin_fill()
    hands.forward(16)
    hands.left(60)
    hands.forward(16)
    hands.left(60)
    hands.end_fill()


def update_clock() -> None:
    now = datetime.now()
    hour_angle = 90 - ((now.hour % 12) + now.minute / 60) * 30
    minute_angle = 90 - (now.minute + now.second / 60) * 6
    second_angle = 90 - now.second * 6

    hands.clear()
    draw_hand(hour_angle, 125, 8, '#ff9f43', '#ff5f56')
    draw_hand(minute_angle, 175, 5, '#53f3ff', '#118ab2')
    draw_hand(second_angle, 195, 2, '#ff5f56', '#ff5f56')

    hands.penup()
    hands.goto(0, -9)
    hands.color('#f4f7ff')
    hands.dot(18)
    hands.color('#ff5f56')
    hands.dot(7)

    labels.clear()
    labels.color('#d9e6ff')
    labels.penup()
    labels.goto(0, 55)
    labels.write('NEON TIME', align='center', font=('Consolas', 18, 'bold'))
    labels.goto(0, 30)
    labels.write('LIVE SYSTEM CLOCK', align='center', font=('Consolas', 9, 'normal'))
    labels.goto(0, -85)
    labels.color('#53f3ff')
    labels.write(now.strftime('%A'), align='center', font=('Consolas', 16, 'bold'))
    labels.goto(0, -115)
    labels.write(now.strftime('%d %B %Y'), align='center', font=('Consolas', 11, 'normal'))
    labels.goto(0, -175)
    labels.write(now.strftime('%H:%M:%S'), align='center', font=('Consolas', 28, 'bold'))

    screen.update()
    screen.ontimer(update_clock, 1000)


draw_clock_face()
update_clock()
turtle.done()
