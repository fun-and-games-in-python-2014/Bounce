from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddles, color):
        self.canvas = canvas
        self.paddles = paddles
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3,]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        for paddle in self.paddles:
            paddle_pos = self.canvas.coords(paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <=0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2

class Paddle:
    def __init__(self, canvas, color, ghost=None):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x =0
        self.ghost = ghost
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = -self.x
        elif pos[2] >= self.canvas_width:
            self.x = -self.x

    def turn_left(self, evt):
        self.x = -2
        if self.ghost:
            self.ghost.turn_right(evt)

    def turn_right(self, evt):
        self.x = 2
        if self.ghost:
            self.ghost.turn_left(evt)

tk = Tk()
tk.title('Bounce')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle2 = Paddle(canvas, 'green')
paddle = Paddle(canvas, 'blue',paddle2)
ball  = Ball(canvas, [paddle,paddle2], 'red')
ball2 = Ball(canvas, [paddle,paddle2], 'yellow')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle2.draw()
        ball2.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
