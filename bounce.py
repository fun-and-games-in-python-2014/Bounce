from tkinter import *
import random
import time

speed = 2
p_speed = 2

def pause():
    global p_speed
    global speed
    speed=0
    p_speed=0

def espeed():
    global p_speed
    global speed
    speed=.5
    p_speed=1

def mspeed():
    global p_speed
    global speed
    speed=2
    p_speed=3

def hspeed():
    global p_speed
    global speed
    speed=3
    p_speed=3

def impspeed():
    global p_speed
    global speed
    speed=15
    p_speed=30

def dspeed():
    global p_speed
    global speed
    speed=10
    p_speed=.5

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
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
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -speed
        if pos[0] <=0:
            self.x = speed
        if pos[2] >= self.canvas_width:
            self.x = -speed

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x =0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -p_speed

    def turn_right(self, evt):
        self.x = p_speed

tk = Tk()
btnp = Button(tk, text="Pause", command=pause)
btn = Button(tk, text="Easy", command=espeed)
btn2 = Button(tk, text="Medium", command=mspeed)
btn3 = Button(tk, text="Hard", command=hspeed)
btn4 = Button(tk, text="Demonic", command=dspeed)
btn5 = Button(tk, text="Impossible", command=impspeed)
btnq = Button(tk, text="Quit", command=tk.destroy)
btnq.pack()
btnp.pack()
btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
tk.title('Bounce')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
