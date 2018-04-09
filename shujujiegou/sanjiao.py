# coding:utf-8

import turtle


def sanjiao(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']

    def getMid(firstpoint, secondpoint):
        return [(firstpoint[0]+secondpoint[0])/2,
                (firstpoint[1]+secondpoint[1])/2]

    def drawTriangle(points, colordegree, myTurtle):
        turtle.pencolor(colordegree)
        turtle.penup()
        turtle.goto(points[0])
        turtle.pendown()
        turtle.fillcolor(colordegree)
        turtle.begin_fill()
        turtle.goto(points[1])
        turtle.goto(points[2])
        turtle.goto(points[0])
        turtle.end_fill()

    drawTriangle(points, colormap[degree], myTurtle)

    if degree > 0:
        sanjiao([points[0], getMid(points[0], points[1]),
                 getMid(points[0], points[2])], degree-1, myTurtle)
        sanjiao([points[1], getMid(points[0], points[1]),
                 getMid(points[1], points[2])], degree-1, myTurtle)
        sanjiao([points[2], getMid(points[2], points[1]),
                 getMid(points[0], points[2])], degree-1, myTurtle)


t = turtle.Turtle()
mysc = turtle.Screen()
mysc.delay(30)
myPoints = [[-200, -100], [0, 200], [200, -100]]
sanjiao(myPoints, 5, t)
mysc.exitonclick()
