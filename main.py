from graphics import Canvas 
import time
import random

ufo_size = 50
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
DELAY = 0.001
N_stars = 100

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    rect = canvas.create_rectangle(0,0,500,500, "black")
    stars = canvas.create_image_with_size(50,50,300,400, "stars.gif")
    moon = canvas.create_image_with_size(10, 10, 150, 150, "moon.png")
    city = canvas.create_image_with_size(100,135,400,300, "city.png")
    for i in range (N_stars):
        draw_stars(canvas)


# coordinates of UFO
    start_y = random.randint(0, CANVAS_HEIGHT) - ufo_size / 2
    end_y = start_y + ufo_size
    ufo = canvas.create_image_with_size(0,start_y,ufo_size,ufo_size,"ufo.png")
    change_x = 1 
    change_y = 1


# UFO Animation
    while (True):
        left_x = canvas.get_left_x(ufo)
        top_y = canvas.get_top_y(ufo)

        if left_x + random.randint(0,10) < 0 or left_x + 10 > CANVAS_WIDTH:
            change_x = -change_x 

        if top_y + random.randint(0,10) < 0 or top_y + 10 > CANVAS_HEIGHT:
            change_y = -change_y

        canvas.move(ufo, change_x, change_y)
        time.sleep(DELAY)
 
# Stars
def draw_stars (canvas):
    x = random.randint(1, CANVAS_WIDTH)
    y = random.randint(1, CANVAS_HEIGHT)
    canvas.create_oval(x, y, x + 2, y + 1, "white")
    
        

if __name__ == '__main__':
    main()