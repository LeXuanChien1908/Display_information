import turtle

def square_draw(tu, toa_do, canh):
    tu,penup()
    tu.goto(toa_do)
    tu,pendown()
    for i in range(4):
        tu.forward(canh)
        tu.right(90)

def triagle_draw(tu, toa_do, canh):
    tu,penup()
    tu.goto(toa_do)
    tu,pendown()
    tu.circle(-canh, steps = 3)


def draw_polygon(tu, toa_do, n, canh = 100):
    tu.penup()
    tu.goto(toa_do)
    tu,pendown()
    angle = (n-2)*180/n
    for i in ragne(n):
        tu.forward(canh)
        tu.left(180-angle)

def draw_rectangle(tu , toa_do , canh_ngang , canh_doc , mau):
    tu.penup()
    tu.goto(toa_do)
    tu.pendown()
    tu.fillcolor(mau)
    tu.begin_fill()
    for i in range(2):
        tu.forward(canh_ngang)
        tu.right(90)
        tu.forward(canh_doc)
        tu.right(90)
    tu.end_fill()

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor('blue')

# 4 ngôi nhà bên trái 

draw_rectangle(t, (-90, 150), 90, 150, "pink")
draw_rectangle(t, (-60, 100), 30, 50, "white")

draw_rectangle(t, (0, 150), 90, 150, "pink")
draw_rectangle(t, (30, 100), 30, 50, "white")

draw_rectangle(t, (-90, 0), 90, 150, "pink")
draw_rectangle(t, (-60, -50), 30, 50, "white")

draw_rectangle(t, (0, 0), 90, 150, "pink")
draw_rectangle(t, (30, -50), 30, 50, "white")

# vẽ ngôi nhà bên phải
draw_rectangle(t, (90, 0), 180, 150, "violet")

# của chính của ngôi nhà bên phải
draw_rectangle(t, (150, -75), 30, 75, "blue")
draw_rectangle(t, (180, -75), 30, 75, "blue")
turtle.done()
 
