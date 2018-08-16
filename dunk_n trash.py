import turtle
import random
import time
start = False
turtle.register_shape("start.gif")
start = turtle.Turtle()
start.shape("start.gif")
startext = turtle.Turtle()
startext.hideturtle()
startext.penup()
startext.goto(0,-300)
turtle.textinput(start, "to start press Enter")
start.hideturtle()
screen = turtle.Screen()
screen.setup(1000,1000)
screen.bgpic("bg.gif")
player = turtle
score=0
score1=turtle.Turtle()
turtle.tracer(1,0)
score1.hideturtle()
score1.penup()
score1.goto(0,-500)
xpos = [-240, -160, -80, 0, 80, 160, 240]

xpos1 = [-240, -160, -80, 0, 80, 160, 240]
xpos2 = [-240, -160, -80, 0, 80, 160, 240]
xpos3 = [-240, -160, -80, 0, 80, 160, 240]
random_xpos1 = random.choice(xpos1)
random_xpos = random.choice(xpos)
random_xpos2 = random.choice(xpos2)
random_xpos3 = random.choice(xpos3)
#creating borders
title = turtle.Turtle()
title.penup()
title.goto(0,400)
title.write("Dunkin' Trash", font=("Comic Sans MS",60),align="center")
title.hideturtle()
border = turtle.Turtle()
border.speed(0)
border.penup()
border.goto(-400,-400)
border.pendown()
border.goto(-400,400)
border.goto(400,400)
border.goto(400,-400)
border.goto(-400,-400)
border.hideturtle()
turtle.register_shape('chips.gif')
turtle.register_shape('paper.gif')
turtle.register_shape("bottle.gif")
turtle.register_shape('milk.gif')
trash = turtle.Turtle()
trash.shape("bottle.gif")
trash.hideturtle()
trash.speed(0)
trash.setheading(270)
trash.penup()
chips = turtle.Turtle()
chips.shape('chips.gif')
chips.hideturtle()
chips.speed(0)
chips.setheading(270)
chips.penup()
paper = turtle.Turtle()
paper.shape('paper.gif')
paper.hideturtle()
paper.speed(0)
paper.setheading(270)
paper.penup()
milk = turtle.Turtle()
milk.shape('milk.gif')
milk.hideturtle()
milk.speed(0)
milk.setheading(270)
milk.penup()

random_xpos = random.choice(xpos)
random_xpos1 = random.choice(xpos1)
random_xpos2 = random.choice(xpos2)
random_xpos3 = random.choice(xpos3)

trash.setpos(random_xpos,400)
trash.showturtle()

paper.setpos(random_xpos,400)
paper.showturtle()

chips.setpos(random_xpos1,400)
chips.showturtle()

milk.setpos(random_xpos1,400)
milk.showturtle()


#making the player move
def player_move():

    def right():
        if player.xcor() > 280:
            player.setpos(280,-300)
        else:
            player.forward(80)

    def left():
        if player.xcor() < -280:
            player.setpos(-280,-300)
        else:
           player.back(80)

    turtle.onkeypress(right, "Right")

    turtle.onkeypress(left, "Left")

    turtle.listen()

#creating the recycle bin


player.penup()
turtle.register_shape("recyclebin.gif")
player.shape("recyclebin.gif")
player.goto(0,-300)

#falling trash function

def falling_trash():

    global score, random_xpos, random_xpos1, trash, chips
    game_over = False
    
    player_move()
    trash.forward(10.9)
    chips.forward(9.5)
    paper.forward(5.4)
    milk.forward(7.2)

    if trash.pos()[1] <-250:
        
        if abs(trash.pos()[0] - player.pos()[0]) < 1:
            score +=1
            score1.clear()
            score1.write(score, font=("Comic Sans MS",60),align=("center"))
            
            random_xpos = random.choice(xpos)
            trash.hideturtle()
            trash.setpos(random_xpos,400)
            trash.showturtle()
        else:
            game_over = True


    if milk.pos()[1] <-250:
        if abs(milk.pos()[0] - player.pos()[0]) < 1:
            score +=1
            score1.clear()
            score1.write(score, font=("Comic Sans MS",60),align=("center"))
            
            random_xpos = random.choice(xpos)
            milk.hideturtle()
            milk.setpos(random_xpos,400)
            milk.showturtle()
        else:
            game_over = True
            
    if chips.pos()[1] <-250:
        
        if abs(chips.pos()[0] - player.pos()[0]) < 1:
            score +=1
            score1.clear()
            score1.write(score, font=("Comic Sans MS",60),align=("center"))
            
            random_xpos = random.choice(xpos)
            chips.hideturtle()
            chips.setpos(random_xpos,400)
            chips.showturtle()
        else:
            game_over = True

    if paper.pos()[1] <-250:
        
        if abs(paper.pos()[0] - player.pos()[0]) < 1:
            score +=1
            score1.clear()
            score1.write(score, font=("Comic Sans MS",60),align=("center"))
            
            random_xpos = random.choice(xpos)
            paper.hideturtle()
            paper.setpos(random_xpos,400)
            paper.showturtle()
        else:
            game_over = True
            
            

        
        
    if game_over:
        score1.goto(0,0)
        score1.color("red")
        score1.write("GAME OVER", font = ("Comic Sans MS", 100), align = ("center"))
        time.sleep(2)
        quit()

    turtle.ontimer(falling_trash, 70)
                

    
falling_trash()
   

    

turtle.listen()
turtle.mainloop()



