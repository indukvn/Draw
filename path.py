from turtle import Turtle, Screen

path = Turtle()
path.pensize(5)
path.shape("arrow")


def mov_fwd():
    path.forward(10)


def mov_bcwd():
    path.backward(10)


def mov_clk():
    path.right(10)


def mov_aclk():
    path.left(10)


def clear():
    path.clear()
    path.penup()
    path.home()
    path.pendown()


screen = Screen()

screen.listen()
screen.onkey(mov_fwd, "W")
screen.onkey(mov_bcwd, "S")
screen.onkey(mov_clk, "D")
screen.onkey(mov_aclk, "A")
screen.onkey(clear, "C")


screen.exitonclick()