from tkinter import *
import random
import time

speed = 2
p_speed = 2
##pause = 1

def pause():
##    global pause
##    pause=1
    global p_speed
    global speed
    speed = 
    p_speed = 0


def espeed():
    global p_speed
    global speed
    speed=.5
    p_speed=1
##    global pause
##    pause=0

def mspeed():
    global p_speed
    global speed
    speed=2
    p_speed=3
##    global pause
##    pause=0

def hspeed():
    global p_speed
    global speed
    speed=3
    p_speed=3
##    global pause
##    pause=0

def impspeed():
    global p_speed
    global speed
    speed=15
    p_speed=30
##    global pause
##    pause=0

def dspeed():
    global p_speed
    global speed
    speed=10
    p_speed=.5
##    global pause
##    pause=0

def restart_game():
    global balls
    for b in balls:
        b.alive = True
        pos = b.canvas.coords(b.id)
        b.canvas.move(b.id, 245-pos[0], 100-pos[1])
    
class Ball:
    
    def __init__(self, canvas, paddles, color):
        self.canvas = canvas
        self.paddles = paddles
        self.id = canvas.create_oval(50, 50, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3,]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.alive = True

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
            self.y = speed
        if pos[3] >= self.canvas_height:
            self.alive = False
        if self.hit_paddle(pos) == True:
            self.y = -speed
        if pos[0] <=0:
            self.x = speed
        if pos[2] >= self.canvas_width:
            self.x = -speed

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
        self.canvas.bind_all('<KeyPress-Down>', self.stop)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = -self.x
        elif pos[2] >= self.canvas_width:
            self.x = -self.x

    def turn_left(self, evt):
        self.x =  -p_speed
        if self.ghost:
            self.ghost.turn_right(evt)

    def turn_right(self, evt):
        self.x = p_speed
        if self.ghost:
            self.ghost.turn_left(evt)

    def stop(self, evt):
        self.x = 0

tk = Tk()
btnp = Button(tk, text="Pause", command=pause)
btn = Button(tk, text="Easy", command=espeed)
btn2 = Button(tk, text="Medium", command=mspeed)
btn3 = Button(tk, text="Hard", command=hspeed)
btn4 = Button(tk, text="Demonic", command=dspeed)
btn5 = Button(tk, text="Impossible", command=impspeed)
btnq = Button(tk, text="Quit", command=tk.destroy)
btn1 = Button(tk, text="Restart", command=restart_game)
btnq.pack({"side": "left"})
btnp.pack({"side": "left"})
btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn1.pack({"side": "left"})
tk.title('Bounce')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

def menu(evt):
    tk = Tk()
    btnp = Button(tk, text="Pause", command=pause)
    btn = Button(tk, text="Easy", command=espeed)
    btn2 = Button(tk, text="Medium", command=mspeed)
    btn3 = Button(tk, text="Hard", command=hspeed)
    btn4 = Button(tk, text="Demonic", command=dspeed)
    btn5 = Button(tk, text="Impossible", command=impspeed)
    btnq = Button(tk, text="Quit", command=tk.destroy)
    btn1 = Button(tk, text="Restart", command=restart_game)
    btnq.pack({"side": "left"})
    btnp.pack({"side": "left"})
    btn.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    btn1.pack()
    tk.title('Bounce')
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    tk.update()
    

canvas.bind_all('<KeyPress-m>', menu)

paddle2 = Paddle(canvas, 'green')
paddle = Paddle(canvas, 'blue',paddle2)
ball  = Ball(canvas, [paddle,paddle2], 'red')
ball2 = Ball(canvas, [paddle,paddle2], 'yellow')
balls = [ball,ball2]

##if pause==0:

##  while True:
##        if ball.alive:
##        ball.draw()
##        paddle2.draw()
##        ball2.draw()
##        paddle.draw()
##    tk.update_idletasks()
##    tk.update()
##    time.sleep(0.01)
##
##  while False:
##        if ball.alive:
##            canvas.create_text(220, 250, text='Game Over', font=('Times', 30))

while True:
    if ball.alive:
        ball.draw()
        paddle2.draw()
        ball2.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

while False:
    if ball.alive:
        canvas.create_text(220, 250, text='Game Over', font=('Times', 30))

