import math, turtle, random

position_x = 0.00
position_y = 0.00
penColor = "darkgoldenrod"
fillColor = ""


# Drawings after the program start
def initialDrawing(): 
    turtle.clear()
    drawRectangle(0,0,700,700,"black", "white") # 700 X 700 rectangle
    selector("Tree") #selector circles
    turtle.goto(0,0)


# Draws rectangle having a center in the middle
def drawRectangle(centre_x, centre_y, width, height, penColor, fillColor="brown"):
    turtle.color(penColor, fillColor)
    saveState()
    x_init, y_init = (centre_x, centre_y + height/2) 
    x_right = x_init + width/2
    y_bottom = y_init - height
    x_left = x_right - width
    y_top = y_bottom + height
    turtle.penup()
    turtle.goto(x_init,y_init) # moves the turtle to the middle of top line
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x_right,y_init)
    turtle.goto(x_right,y_bottom)
    turtle.goto(x_left,y_bottom)
    turtle.goto(x_left,y_top)
    turtle.goto(x_init,y_init)
    turtle.end_fill()
    turtle.penup()
    restoreState()


# Saves turtle state in global variables
def saveState():
    global position_x, position_y, penColor, fillColor
    position_x = turtle.xcor()
    position_y =  turtle.ycor()
    penColor = turtle.pencolor()
    fillColor = turtle.fillcolor()


# Restores turtle state from global variables
def restoreState():
    global position_x, position_y, penColor, fillColor
    turtle.setx(position_x)
    turtle.sety(position_y)
    turtle.pencolor() == penColor
    turtle.fillcolor() == fillColor

  

# Shape selectors
def selector(name):
    if name == "Bird":
        turtle.goto(0,360)
        drawCircle(0,370, 10,"green", "green") # Selects Bird
        turtle.goto(100,360)
        drawCircle(100,370, 10,"black","white")
        
    else:
        turtle.goto(0,360)
        drawCircle(0,370, 10,"black", "white") 
        turtle.goto(100,360)
        drawCircle(100,370, 10,"green","green") # Selects Tree
    turtle.goto(20,360)
    turtle.pencolor("black")
    turtle.write("Bird", False, font=("Arial",8,"bold"))
    turtle.goto(120,360)
    turtle.write("Tree", False, font=("Arial",8,"bold"))


# Draws Circle
def drawCircle(centre_x, centre_y, radius, penColor, fillColor):
    turtle.color(penColor, fillColor)
    saveState()
    turtle.penup()
    turtle.goto(centre_x,centre_y-radius)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    restoreState()


# determines the distance between two points
def distance(x1,x2,y1,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist


# stamps a bird shape
def stampTurtle(centre_x, centre_y, color):
    turtle.color(color)
    saveState()
    turtle.stamp()
    restoreState()


# removes the stamp from top left corner
def removeTopLeftStamp():
    turtle.goto(-340,370)
    stampTurtle(-340,370,"white")
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(-300, 350)
    turtle.pendown()
    turtle.goto(-350, 350)
    turtle.goto(-350, 300)
    turtle.penup()
    turtle.goto(-340,370)


# Erases drawing outside boundary
def eraser():
    drawRectangle(-450,0,200,1000,"white","white")
    drawRectangle(0,-400,1000,100,"white","white")
    drawRectangle(450,0,200,1000,"white","white")
    drawRectangle(0,550,1000,400,"white","white")
    turtle.pencolor("black")
    turtle.goto(-350,350)
    turtle.pendown()
    turtle.goto(350,350)
    turtle.goto(350,-350)
    turtle.goto(-350,-350)
    turtle.goto(-350,350)
    turtle.penup()

# Draws tree shape
def drawTree(centre_x, centre_y):
    scale_factor = random.uniform(0.7, 1.3) #generates a random numberbetween 0.7 and 1.3
    steam_width = 15 *scale_factor
    steam_height = 80 *scale_factor
    leaf_width = 100 *scale_factor
    leaf_height = 50 *scale_factor
    drawRectangle(centre_x, centre_y-steam_height/2,steam_width,steam_height,"brown") #remove the value for using global varable value
    for _ in range(3):
        turtle.goto(centre_x, turtle.ycor()+leaf_height/2) #sets the center for triangle from current possition
        drawTriangle(turtle.xcor(), turtle.ycor(),leaf_width,leaf_height, "green") #remove the value for using global variable value
        turtle.goto(centre_x, turtle.ycor()+leaf_height/2) # moves turtle to the top of previous triangle
        leafOverlap = leaf_height*0.4
        turtle.sety(turtle.ycor()- leafOverlap) # moves turtle down for 40% leaf overlapping


# Draws triangle having a center in the middle
def drawTriangle(centre_x, centre_y, width, height, penColor, fillColor="green"):
    turtle.color(penColor, fillColor)
    saveState()
    x_init, y_init = (turtle.xcor(), turtle.ycor()-height/2)
    x_middle = x_init
    x_bottom_left = x_init - width/2
    x_bottom_right = x_init + width/2
    y_top = y_init +height
    turtle.penup()
    turtle.goto(x_init, y_init) # moves the turtle to the middle of bottom line
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x_bottom_left, y_init)
    turtle.goto(x_middle, y_top)
    turtle.goto(x_bottom_right, y_init)
    turtle.goto(x_init, y_init)
    turtle.end_fill()    
    turtle.penup()
    restoreState()


turtle.register_shape('bird', ((-22,-39),(-20,-7),(-7,3),(-11,7),(-12,9),(-11,10),(-9,10),(-3,7),(10,24),(30,16),(13,18),(4,0),(14,-6),(6,-13),(0,-4),(-14,-13),(-22,-39))) #registers birdshape
turtle = turtle.Turtle('bird')
turtle.hideturtle()
turtle.speed(0)

