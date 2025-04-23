# File: Kulow_p2.py
# Author: Robert Kulow 
# Date: 11/28/2022
# Section: 0001
# E-mail: robert.kulow@maine.edu
# Description:
# Creates artwork similar to the artist, Piet Mondrian, and does so by drawing a rectangle, then spliting until one side is less then
# 90 pixels, in which it will color in the rectangle and move on the the next large scetion to split again using recursion.
# Collaboration:
# I briefly talked about my ideas and concepts to Bryce Roy, that was about it though.

from graphics import *
from random import *

def art():
    win = GraphWin("My Drawing",1281, 721)
    points = [[[0,0,1280,720]]]
    aRect = Rectangle(Point(points[0][0][0],points[0][0][1]), Point(points[0][0][2],points[0][0][3]))
    aRect.setOutline("black")
    aRect.setFill("white")
    aRect.draw(win)
    points,win = split(points,win)
    color(points,win)
    win.getMouse() # pause for click in window
    win.close()

def split(points,win):
    if (points[-1][0][2] - points[-1][0][0]) > 90 and (points[-1][0][3] - points[-1][0][1]) > 90:
        vaxis = randint(90, int((points[-1][0][2] - points[-1][0][0]) * 1.5))
        haxis = randint(90, int((points[-1][0][3] - points[-1][0][1]) * 1.5))
        vline = 0
        hline = 0
        if vaxis < (points[-1][0][2] - points[-1][0][0]):
            vline = randint(int(points[-1][0][2] * .31),int(points[-1][0][2] * .68))
            aLine = Line(Point(vline,points[-1][0][1]), Point(vline,points[-1][0][3]))
            aLine.draw(win)
            if haxis < (points[-1][0][3] - points[-1][0][1]):
                hline = randint(int(points[-1][0][3] * .31),int(points[-1][0][3] * .68))
                aLine = Line(Point(points[-1][0][0],hline), Point(points[-1][0][2],hline))
                aLine.draw(win)
                points = add(points,vline,hline)
                split(points,win)
                return points,win  
            else:
                points = add(points,vline,hline)
                split(points,win)
                return points,win     
        elif haxis < (points[-1][0][3] - points[-1][0][1]):
            hline = randint(int(points[-1][0][3] * .31),int(points[-1][0][3] * .68))
            aLine = Line(Point(points[-1][0][0],hline), Point(points[-1][0][2],hline))
            aLine.draw(win)
            points = add(points,vline,hline)
            split(points,win)
            return points,win
        else:
            return points,win
    else:
        return points,win 

def color(points,win):
    for n in range(0,len(points[0])):
        aRect = Rectangle(Point(points[0][n][0],points[0][n][1]), Point(points[0][n][2],points[0][n][3]))
        aRect.setOutline("black")
        aRect.setFill(wryb())
        aRect.draw(win)

def wryb():
    num = random()
    if num < 0.1:
        blue = "blue"
        return blue
    elif num < 0.25:
        red = "red"
        return red
    elif num < 0.5:
        yellow = "yellow"
        return yellow
    else:
        white = "white"
        return white

def add(points,vline,hline):
    if vline > 0 and hline > 0:
        points[-1].append([])
        points[-1][-1].append(points[0][0][0])
        points[-1][-1].append(points[0][0][1])
        points[-1][-1].append(vline)
        points[-1][-1].append(hline)
        points[-1].append([])
        points[-1][-1].append(points[0][0][0])
        points[-1][-1].append(hline)
        points[-1][-1].append(vline)
        points[-1][-1].append(points[0][0][3])
        points[-1].append([])
        points[-1][-1].append(vline)
        points[-1][-1].append(points[-1][0][1])
        points[-1][-1].append(points[0][0][2])
        points[-1][-1].append(hline)
        points[-1].append([])
        points[-1][-1].append(vline)
        points[-1][-1].append(hline)
        points[-1][-1].append(points[0][0][2])
        points[-1][-1].append(points[0][0][3]) 
        points[-1].remove(points[-1][0])   
    elif vline > 0:
        points[-1].append([])
        points[-1][-1].append(points[0][0][0])
        points[-1][-1].append(points[0][0][1])
        points[-1][-1].append(vline)
        points[-1][-1].append(points[0][0][3])
        points[-1].append([])
        points[-1][-1].append(vline)
        points[-1][-1].append(points[-1][0][1])
        points[-1][-1].append(points[0][0][2])
        points[-1][-1].append(points[-1][0][3])
        points[-1].remove(points[-1][0])
    elif hline > 0:
        points[-1].append([])
        points[-1][-1].append(points[0][0][0])
        points[-1][-1].append(points[0][0][1])
        points[-1][-1].append(points[0][0][2])  
        points[-1][-1].append(hline)
        points[-1].append([])
        points[-1][-1].append(points[-1][0][0])
        points[-1][-1].append(hline)
        points[-1][-1].append(points[-1][0][2])
        points[-1][-1].append(points[0][0][3])
        points[-1].remove(points[-1][0])
    return points

art()