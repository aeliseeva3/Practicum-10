import turtle

turtle.speed(0)
turtle.tracer(0)

BLUE = 'blue'
LIGHT = 'lightblue'
WHITE = 'white'


def figura(vertices, color):
    '''
    Draws a filled polygon from a list of vertices
    :param vertices: list of (x, y) tuples
    :param color: fill color
    '''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(vertices[0])
    turtle.down()
    for vertex in vertices[1:] + [vertices[0]]:
        turtle.goto(vertex)
    turtle.end_fill()
    turtle.up()


def square(vertices, color1, color2):
    '''
    Draws a square made of two triangles
    :param vertices: [left_bottom, right_bottom, right_top]
    :param color1: color of the first triangle (bottom)
    :param color2: color of the second triangle (top)
    '''
    figura(vertices, color1)
    if vertices[1][1] > vertices[2][1]:
        vertices[1] = (vertices[1][0] - 20, vertices[1][1] - 20)
    else:
        vertices[1] = (vertices[1][0] - 20, vertices[1][1] + 20)
    figura(vertices, color2)


square([(0, 200), (20, 200), (20, 180)], BLUE, LIGHT)
square([(20, 200), (40, 200), (40, 180)], LIGHT, BLUE)
square([(40, 200), (60, 200), (60, 180)], WHITE, LIGHT)
square([(60, 180), (80, 180), (80, 200)], LIGHT, WHITE)
square([(80, 180), (100, 180), (100, 200)], BLUE, LIGHT)
square([(100, 180), (120, 180), (120, 200)], LIGHT, BLUE)

square([(0, 180), (20, 180), (20, 160)], LIGHT, WHITE)
square([(20, 180), (40, 180), (40, 160)], BLUE, LIGHT)
square([(40, 180), (60, 180), (60, 160)], LIGHT, BLUE)
square([(60, 160), (80, 160), (80, 180)], BLUE, LIGHT)
square([(80, 160), (100, 160), (100, 180)], LIGHT, BLUE)
square([(100, 160), (120, 160), (120, 180)], WHITE, LIGHT)

square([(0, 160), (20, 160), (20, 140)], WHITE, LIGHT)
square([(20, 160), (40, 160), (40, 140)], LIGHT, WHITE)
square([(40, 160), (60, 160), (60, 140)], BLUE, LIGHT)
square([(60, 140), (80, 140), (80, 160)], LIGHT, BLUE)
square([(80, 140), (100, 140), (100, 160)], WHITE, LIGHT)
square([(100, 140), (120, 140), (120, 160)], LIGHT, WHITE)

square([(0, 120), (20, 120), (20, 140)], WHITE, LIGHT)
square([(20, 120), (40, 120), (40, 140)], LIGHT, WHITE)
square([(40, 120), (60, 120), (60, 140)], BLUE, LIGHT)
square([(60, 140), (80, 140), (80, 120)], LIGHT, BLUE)
square([(80, 140), (100, 140), (100, 120)], WHITE, LIGHT)
square([(100, 140), (120, 140), (120, 120)], LIGHT, WHITE)

square([(0, 100), (20, 100), (20, 120)], LIGHT, WHITE)
square([(20, 100), (40, 100), (40, 120)], BLUE, LIGHT)
square([(40, 100), (60, 100), (60, 120)], LIGHT, BLUE)
square([(60, 120), (80, 120), (80, 100)], BLUE, LIGHT)
square([(80, 120), (100, 120), (100, 100)], LIGHT, BLUE)
square([(100, 120), (120, 120), (120, 100)], WHITE, LIGHT)

square([(0, 80), (20, 80), (20, 100)], BLUE, LIGHT)
square([(20, 80), (40, 80), (40, 100)], LIGHT, BLUE)
square([(40, 80), (60, 80), (60, 100)], WHITE, LIGHT)
square([(60, 100), (80, 100), (80, 80)], LIGHT, WHITE)
square([(80, 100), (100, 100), (100, 80)], BLUE, LIGHT)
square([(100, 100), (120, 100), (120, 80)], LIGHT, BLUE)


turtle.update()
turtle.done()
