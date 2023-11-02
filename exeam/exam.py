from turtle import *

#mission: draw and color a house

#step 1: draw a square

speed(10)
width(4)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#step 1 done

#step2: draw a door

goto(0, 0)

forward(70)
left(90)

color("yellow")
begin_fill()
forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

#end of door

#roof

penup()
goto(200, 200)
pendown()
begin_fill()
right(150)

color("red")

forward(200)

left(120)
forward(200)
end_fill()

#done

#window

penup()

goto(20, 180)

pendown()

left(30)

color("brown")

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(25)
left(90)

forward(50)
left(90)

forward(25)
left(90)

forward(25)
left(90)

forward(50)
end_fill()

#one window done

#second window

penup()
goto(180, 180)
pendown()

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(25)
right(90)

forward(50)

right(90)

forward(25)
right(90)

forward(25)
right(90)

forward(50)

penup()
goto(0, 0)




exitonclick()