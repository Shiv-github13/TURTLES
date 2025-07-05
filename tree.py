import turtle as t

t.speed(0)
t.pensize(2)
t.left(90)
t.backward(100)
t.color("black")

def draw(i):
    if (i<10):
        return
    else:
        t.forward(i)
        t.color("red")
        t.circle(2)
        t.color("black")
        t.left(30)
        draw(3*i/4)
        t.right(60)
        draw(3*i/4)
        t.left(30)
        t.backward(i)

draw(100)




