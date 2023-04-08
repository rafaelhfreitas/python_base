# Python 3.10
# Pattern Match Estrutural
print("""\
Jogo da Tartaruga

commandos:
    move x y
    move steps
    turn angle (default 90)
    draw shape size (line|circle)
    write text
    stop | exit

"""
)


from turtle import Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("blue", "yellow")
turtle.penup()


while True:
    command = input("🐢>").strip().split()
    if command[0] in ("exit", "stop"):
        # move 2 3 = ["move", "2",  "3"]
        break
    if command[0] == "draw":
        # draw line 40
        shape = command[1]
        size = float(command[2])
        turtle.pendown()
        if shape == "line":
            turtle.forward(size)
        elif shape == "circle":
            turtle.circle(size)
