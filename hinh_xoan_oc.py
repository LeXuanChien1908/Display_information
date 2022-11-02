import turtle

t = turtle.Turtle()
d = 200
buoc_di = 0
t.speed(10)
while ( t.distance(0 ,0) < d):
    buoc_di += 0.1
    t.forward(buoc_di)
    t.left(20)

t.done()
