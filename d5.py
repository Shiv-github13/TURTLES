import turtle as t



t.bgcolor('black')

t.color('cyan')

t.speed(0)


t.pensize(2)


for i in range(600):

    if i%5==0:

        t.lt(3)
    t.fd(200)
    t.lt(360/5)
t.done()