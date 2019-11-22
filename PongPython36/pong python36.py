import turtle
import sys

ventana = turtle.Screen()
ventana.title("Pong Game")
ventana.bgcolor("green")
ventana.setup(width=800, height=600)
ventana.tracer(0) #Lo hace más rapido

#Score
score_a = 0
score_b = 0

#background
image = r"C:\Users\sandrita\Desktop\PongPython36\fondo.gif"
screen = turtle.Screen()
screen.addshape(image)
turtle.shape(image)

#Barra A
barra_a = turtle.Turtle()
barra_a.speed(0) #Velocidad de animacion
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5,stretch_len=1)
barra_a.penup()
barra_a.goto(-350,0)

#Barra B
barra_b = turtle.Turtle()
barra_b.speed(0) #Velocidad de animacion
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5,stretch_len=1)
barra_b.penup()
barra_b.goto(350,0) #coordenadas x e y

#Ball 
ball = turtle.Turtle()
ball.speed(0) #Velocidad de animacion
ball.shape("circle")
ball.color("purple")
ball.penup()
ball.goto(0,0) #coordenadas x e y
ball.dx = 2 #movimiento en x
ball.dy = -2 #movimiento en y

#Tablero
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #es para no ver lineas desde el centro IMPORTANTE QUE SE LEVANTE EL BOLIGRAFO
pen.hideturtle()
pen.goto(0, 230)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 16, "bold"))

#Funciones
def barra_a_up():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)

def barra_a_down():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)

def barra_b_up():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)

def barra_b_down():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)           

#El teclado
ventana.listen() #le decimos a la ventana que escuche el teclado
ventana.onkeypress(barra_a_up, "w") 
ventana.onkeypress(barra_a_down, "s")  
ventana.onkeypress(barra_b_up, "Up") 
ventana.onkeypress(barra_b_down, "Down")  

#Main game loop
while True:
    ventana.update() #Actualiza la ventana

    #movimiento a la bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #bordes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #En los laterales es otra cosa
    #La bola debe aparecer de nuevo en el juego

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "bold"))

    if score_a > 9:
        pen.clear()
        pen.write("Ha ganado jugador A", align="center", font=("Courier", 24, "bold"))
        sys.exit()
                
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear() # limpia la pantalla
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "bold"))

    if score_b > 9:
        pen.clear()
        pen.write("Ha ganado jugador B", align="center", font=("Courier", 24, "bold"))
        sys.exit()

    #Colisiones con las barras
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < barra_b.ycor() + 40 and ball.ycor() > barra_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < barra_a.ycor() + 40 and ball.ycor() > barra_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1    
        
