import turtle
import random


def draw_city():
    """
    Draws a night city landscape with buildings, windows, stars, and the moon.
    :return: None
    """
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("midnightblue")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()


    def draw_building(x, y, width, height, color):
        """
        Draws a building with the specified parameters.
        :param x: X-coordinate of the building's bottom-left corner
        :param y: Y-coordinate of the building's bottom-left corner
        :param width: Width of the building
        :param height: Height of the building
        :param color: Fill color of the building
        :return: None
        """
        t.goto(x, y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()
        t.penup()


    def draw_windows(x, y, width, height, building_color):
        """
        Draws windows on a building.
        :param x: X-coordinate of the building's bottom-left corner
        :param y: Y-coordinate of the building's bottom-left corner
        :param width: Width of the building
        :param height: Height of the building
        :param building_color: Fill color of the building (for unlit windows)
        :return: None
        """
        window_width = 15
        window_height = 20
        start_x = x + 10
        start_y = y + 10

        for row in range(start_y, y + height - window_height, window_height + 10):
            for col in range(start_x, x + width - window_width, window_width + 10):
                t.goto(col, row)
                t.pendown()

                if random.random() > 0.4:
                    t.fillcolor("yellow")
                else:
                    t.fillcolor(building_color)
                t.begin_fill()
                for _ in range(4):
                    t.forward(window_width)
                    t.left(90)
                t.end_fill()
                t.penup()


    def draw_stars(num_stars):
        """
        Draws stars in the night sky.
        :param num_stars: Number of stars to draw
        :return: None
        """
        t.color("white")
        for _ in range(num_stars):
            x = random.randint(-400, 400)
            y = random.randint(45, 300)
            t.goto(x, y)
            t.dot(random.randint(1, 3))

    draw_stars(100)

    t.goto(300, 250)
    t.color("lightyellow")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()

    buildings = [
        (-400, -300, 80, 240, "darkslateblue"),   
        (-320, -300, 70, 280, "midnightblue"),    
        (-250, -300, 85, 210, "darkslateblue"),   
        (-165, -300, 75, 340, "midnightblue"),    
        (-90, -300, 90, 260, "darkslateblue"),    
        (0, -300, 100, 180, "midnightblue"),      
        (100, -300, 80, 310, "darkslateblue"),    
        (180, -300, 85, 240, "midnightblue"),     
        (265, -300, 75, 280, "darkslateblue"),    
        (340, -300, 60, 160, "midnightblue"),     
    ]

    for x, y, width, height, color in buildings:
        draw_building(x, y, width, height, color)
        draw_windows(x, y, width, height, color)


if __name__ == "__main__":
    draw_city()

