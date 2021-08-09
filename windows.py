from turtle import *

def windows_logo():

    speed(1)
    hideturtle()
    bgcolor('black')
    pensize(3)
    penup()
    goto(-50, 60)
    pendown()
    color("#00adef")
    begin_fill()
    goto(100, 100)
    goto(100, -100)
    goto(-50, -60)
    goto(-50, 60)
    end_fill()
    color("black")
    penup()
    goto(25, 80)

    pendown()
    pensize(8)
    goto(25, -80)
    penup()

    goto(-50, 0)

    pendown()
    goto(100, 0)
    
    
    
    


def star():

    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    
    done()

def windows_logo2():
    speed(1)
    hideturtle()
    bgcolor('black')
    pensize(2)
    penup()
    goto(20, 5)
    pendown()
    color("#00adef")
    begin_fill()
    goto(-50,5)
    goto(-50,60)
    goto(20,80)   
    
    goto(20,5)
    #end_fill()
    #begin_fill()
    penup()
    goto(20,-5)
    pendown()
    goto(20,-80)
    goto(-50,-60)
    goto(-50,-5)
    goto(20,-5)

    penup()
    goto(30,-5)
    pendown()
    goto(100, -5)
    goto(100,-100)
    goto(30, -83)
    goto(30, -5)

    penup()
    goto(30,5)
    pendown()
    goto(30, 83)
    goto(100,100)
    goto(100, 5)
    goto(30, 5)
    end_fill()
    
    penup()
    color('black')
    shape('square')
    shapesize(.45)
    goto(24.9,0.1)
    showturtle()
      
    


if __name__ == '__main__':
    #star()
    windows_logo2()
    
    mainloop()
