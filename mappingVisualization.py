import turtle
import primefac

window = turtle.Screen()
pen = turtle.Turtle()

window.screensize(1000, 1000)

window.setworldcoordinates(-500, -500, 500, 500)

window.bgcolor("black")
pen.color("green")
pen.pensize(.000001)
pen.shape("blank")
pen.speed(0)

window.tracer(10000, 0)
pen.up()

# Generates the basic mapping, no prime distinction
# for x in range(0, 20):
#     for y in range(0, 25):
#         pen.goto(30*x - 500, 30*y - 500)
#         num = (x+y)*(x+y+1)/2 + x
#         pen.write(num)

# Generating the mapping, coloring in the primes green
for x in range(0, 20):
    for y in range(0, 25):
        pen.goto(30*x - 500, 30*y - 500)
        num = (x+y)*(x+y+1)/2 + x
        if primefac.isprime(num):
            pen.color("red")
        else:
            pen.color("gray")
        pen.write(num)




window.exitonclick()
