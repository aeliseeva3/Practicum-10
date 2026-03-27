import turtle


def draw_rhombus(x, y, color):
    """
    Draws a rhombus at the specified position.
    :param x: X-coordinate of the rhombus center
    :param y: Y-coordinate of the rhombus center
    :param color: Fill color of the rhombus
    :return: None
    """
    t.penup()
    t.goto(x, y - 30)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x + 30, y)
    t.goto(x, y + 30)
    t.goto(x - 30, y)
    t.goto(x, y - 30)
    t.end_fill()
    t.penup()


def draw_star(x, y, color):
    """
    Draws a star at the specified position.
    :param x: X-coordinate of the star center
    :param y: Y-coordinate of the star center
    :param color: Fill color of the star
    :return: None
    """
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(25)
        t.left(144)
        t.forward(25)
        t.left(72)
    t.end_fill()
    t.penup()


def draw_square(x, y, color):
    """
    Draws a square at the specified position.
    :param x: X-coordinate of the square center
    :param y: Y-coordinate of the square center
    :param color: Fill color of the square
    :return: None
    """
    t.penup()
    t.goto(x - 30, y - 30)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(60)
        t.left(90)
    t.end_fill()
    t.penup()


def draw_ornament():
    """
    Draws an ornament of 9 figures in one row.
    :return: None
    """
    x = -320
    y = 0

    draw_rhombus(x, y, "aliceblue")
    x += 80

    draw_star(x, y, "honeydew")
    x += 80

    draw_square(x, y, "lavender")
    x += 80

    draw_rhombus(x, y, "lightpink")
    x += 80

    draw_star(x, y, "thistle")
    x += 80

    draw_square(x, y, "lightcoral")
    x += 80

    draw_rhombus(x, y, "mistyrose")
    x += 80

    draw_star(x, y, "rosybrown")
    x += 80

    draw_square(x, y, "plum")


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=900, height=300)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    draw_ornament()

