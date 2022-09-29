import turtle
# GAME SCREEN SETUP 
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# GAME LOOP 
while True:
    wn.update()