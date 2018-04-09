import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
def drawSpiral(myTurtle,linlen):
    if linlen>0:
        myTurtle.forward(linlen)
    myTurtle.right(90)
    drawSpiral(myTurtle,linlen-5)
drawSpiral(myTurtle,100)
myWin.exitonclick()
