import turtle
t = turtle.Pen()
t.reset()

def kura1():
   for x in range(1,10):
        t.forward(150)
        t.left(110)

def kura2():
    for y in range(1,9):
    #while True:
        t.forward(50)
        t.left(45)

def kura3():
    for y in range(1, 9):
        # while True:
        t.forward(100)
        t.left(225)

def kura4():
    for y in range(1, 38):
        # while True:
        t.forward(100)
        t.left(175)

def kura5():
    #b = turtle.Pen()
    #b.reset()
    #for y in range(1, 20):
    while True:
        t.forward(100)
        t.left(95)

def kura6():
    b = turtle.Pen()
    b.reset()
    b.color(1,0,0)
    b.begin_fill()
    for x in range(1,19):

        b.forward(100)
        if x % 2 == 0:
            b.left(175)
        else:
            b.left(225)

def kura7():
    #buat body
    t.color(1, 0, 0)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.end_fill()

    #buat roda depan
    t.color(0, 0, 0)
    t.up()
    t.forward(10)
    t.down()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    #buat roda belakang
    t.setheading(0)
    t.up()
    t.forward(90)
    t.right(90)
    t.forward(10)
    t.setheading(0)
    t.begin_fill()
    t.down()
    t.circle(10)
    t.end_fill()
#gulaku 2
#susu 4
#gula merah 1

def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def mystar(size, filled):

    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()

t.color(0.9, 0.75, 0)
mystar(120, True)
