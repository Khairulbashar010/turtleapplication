import turtle as t
from mod import *

"""
#Use this if part of the screen is not visible

# Creates a 800 X 800 screen
screen = t.Screen()
screen.screensize(800, 800)
"""

#Creates a 800 X 800 screen
t.setup(800,800,0,0)



# Required Variables
shape = 1 # Default shape (Tree)
tiltAngle = 0.0


# response to Left Mouse click 
def handle_click(x, y):
    global shape
    if distance(x,0,y,370)<=10: # Selects Bird shape
        shape = 0
        selector("Bird")
        turtle.goto(-340,370)
        stampTurtle(-340,370,penColor) # Bird icon on top left

    elif distance(100,x,370,y)<=10: # Selects Tree shape
        shape = 1
        selector("Tree")
        removeTopLeftStamp()
        turtle.goto(0,0)
        
    elif ((x > -350 and x<350) and (y > -350 and y<350)): # Draws on board
        if shape == 0:
            turtle.penup()
            turtle.goto(x,y) 
            stampTurtle(x,y, penColor) # Stamps bird shape
            eraser()
            selector("Bird")
            turtle.goto(-340,370)
            stampTurtle(-340,370,penColor)
        else:
            turtle.penup()
            turtle.goto(x,y)
            drawTree(x,y)
            eraser() # Draws tree
            selector("Tree")
        

# Response to left arrow key
def left_keypress():
    global tiltAngle
    removeTopLeftStamp()
    tiltAngle = tiltAngle + 5 # tilts turtle by 5 degrees anticlockwise
    turtle.settiltangle(tiltAngle)
    stampTurtle(-340,370,penColor)


# Response to right arrow key
def right_keypress():
    global tiltAngle
    removeTopLeftStamp()
    tiltAngle = tiltAngle - 5 # tilts turtle by 5 degrees clockwise
    turtle.settiltangle(tiltAngle)
    stampTurtle(-340,370,penColor)

# main funnction
def main():
    # Listener Function
    t.listen()
    t.onscreenclick(handle_click)
    t.onkey(left_keypress, "Left")
    t.onkey(right_keypress, "Right")

    initialDrawing()
    
    t.done()

    
if __name__ == "__main__":
     main()