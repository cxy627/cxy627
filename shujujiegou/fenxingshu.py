import turtle

t = turtle.Turtle()
mywin = turtle.Screen()


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)
        mywin.delay(20)


t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
tree(75,t)
mywin.exitonclick()
