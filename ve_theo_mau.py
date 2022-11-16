import turtle

turtle.speed(0)
r = 150 
colors = ["red" , "yellow" , "blue" , "green" , "brown" , "violet" ]
for i in range(0, 360, 10):
    turtle.right(10)
    turtle.color(color[i//10%len(colors)])
    cnt = 0
    while (cnt < 2):
        turtle.circle(r,90)
        turtle.circle(r//2,90)
        cnt += 1
turtle.done()