import turtle
import time
import random

def draw_background():
    ground = turtle.Turtle()
    ground.hideturtle()
    ground.speed(0)
    ground.penup()
    ground.goto(-500, -150)
    ground.color("darkgreen")
    ground.begin_fill()

    for _ in range(2):
        ground.forward(1000)
        ground.right(90)
        ground.forward(450)
        ground.right(90)
    ground.end_fill()

def draw_house(x, y):
    house = turtle.Turtle()
    house.hideturtle()
    house.speed(0)
    house.penup()
    house.goto(x, y)
    house.pendown()

    house.color("lightgray")
    house.begin_fill()
    for _ in range(2):
        house.forward(90)
        house.left(90)
        house.forward(70)
        house.left(90)
    house.end_fill()

    house.penup()
    house.goto(x, y + 70)
    house.pendown()
    house.color("darkred")
    house.begin_fill()
    house.goto(x + 45, y + 115)
    house.goto(x + 90, y + 70)
    house.goto(x, y + 70)
    house.end_fill()
    return house

def draw_car(x, y):
    car = turtle.Turtle()
    car.hideturtle()
    car.speed(0)
    car.penup()
    car.goto(x, y)
    car.pendown()
    
    car.color("blue")
    car.begin_fill()
    for _ in range(2):
        car.forward(65)
        car.left(90)
        car.forward(28)
        car.left(90)
    car.end_fill()

    car.penup()
    car.goto(x + 10, y - 5)
    car.dot(10, "black")
    car.goto(x + 55, y - 5)
    car.dot(10, "black")

    return car

def create_tornado():
    tornado = turtle.Turtle()
    tornado.hideturtle()
    tornado.speed(0)
    tornado.penup()
    return tornado

def draw_tornado(tornado, x, y):
    tornado.clear()
    height = 300
    top_half_width = 90

    tornado.color("gray60")
    tornado.penup()
    tornado.goto(x, y)
    tornado.pendown()
    tornado.begin_fill()
    tornado.goto(x - top_half_width, y + height)
    tornado.goto(x + top_half_width, y + height)
    tornado.goto(x, y)
    tornado.end_fill()
    tornado.penup()

def draw_minor_damage():
    damage = turtle.Turtle()
    damage.hideturtle()
    damage.speed(0)
    damage.color("gray70")

    damage.penup()
    damage.goto(250, -80)
    damage.pendown()
    damage.pensize(5)
    damage.goto(340, -65)

    for _ in range(15):
        x = random.randint(230, 390)
        y = random.randint(-150, -80)
        damage.penup()
        damage.goto(x, y)
        damage.dot(random.randint(3, 6))

def draw_major_damage():
    damage = turtle.Turtle()
    damage.hideturtle()
    damage.speed(0)
    damage.color("sienna")

    damage.penup()
    damage.goto(250, -150)
    damage.pendown()
    damage.begin_fill()

    for _ in range(2):
        damage.forward(70)
        damage.left(90)
        damage.forward(30)
        damage.left(90)
    damage.end_fill()

    damage.penup()
    damage.goto(310, -100)
    damage.pendown()
    damage.color("darkred")
    damage.begin_fill()
    damage.goto(360, -120)
    damage.goto(320, -140)
    damage.goto(310, -100)
    damage.end_fill()

    damage.color("gray80")
    for _ in range(35):
        x = random.randint(220, 420)
        y = random.randint(-170, -60)
        damage.penup()
        damage.goto(x, y)
        damage.dot(random.randint(4, 9))

def draw_catastrophic_damage():
    rubble = turtle.Turtle()
    rubble.hideturtle()
    rubble.speed(0)

    for _ in range(80):
        x = random.randint(210, 450)
        y = random.randint(-180, -70)
        size = random.randint(4, 14)
        color = random.choice([
            "gray60",
            "gray80",
            "sienna",
            "darkred",
            "black"
        ])
        rubble.penup()
        rubble.goto(x, y)
        rubble.color(color)
        rubble.dot(size)

    rubble.penup()
    rubble.goto(240, -155)
    rubble.pendown()
    rubble.color("gray30")
    rubble.pensize(6)
    rubble.forward(100)

def apply_damage(house, car, ef_rating):
    if ef_rating <= 1:
        draw_minor_damage()
    elif ef_rating <= 3:
        draw_major_damage()
    else:
        house.clear()
        car.clear()
        draw_catastrophic_damage()

def run_animation(event):
    screen = turtle.Screen()
    screen.title("Vortex Lab")
    screen.bgcolor("gray25")
    screen.setup(width=1000, height=600)

    screen.clear()
    screen.bgcolor("gray25")
    draw_background()
    house = draw_house(250, -150)
    car = draw_car(380, -150)
    tornado = create_tornado()
    x = -450
    y = -120

    while x < 600:
        draw_tornado(tornado, x, y)
        x += 25
        time.sleep(0.01)
    tornado.clear()
    apply_damage(house, car, event["ef_rating"])
    time.sleep(2)
    return
