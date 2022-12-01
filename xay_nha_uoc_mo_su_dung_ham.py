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

# vẽ ngôi nhà

draw_rectangle(t, (-100, 100), 200, 100, "white")
draw_rectangle(t, (-30, 70), 60, 70, "white")
draw_rectangle(t, (0, 100), 10, 80, "white")
draw_polygon(t, (-100, 100), 3, 130)


turtle.done()
 
