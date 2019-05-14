from tkinter import *
from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk
import sys


class Game:
    def __init__(self):
        self.tk = Tk()
        self.times = 0
        sw = self.tk.winfo_screenwidth()
        sh = self.tk.winfo_screenheight()
        image = Image.open(r'02.jpg')
        background_image = ImageTk.PhotoImage(image)
        ww = background_image.width()
        wh = background_image.height()
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.tk.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.tk.title('欢迎进入弹弹弹')
        background_label = Label(self.tk, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.tk.resizable(False, False)
        self.tk.wm_attributes("-topmost", 1)  # at top
        btn1 = Button(self.tk, text='减少难度', background='#FFFF67',
                      activebackground='#3EC23B', command=self.test1)
        btn2 = Button(self.tk, text='增加难度', background='#FFFF67',
                      activebackground='#3EC23B', command=self.test2)

        btn1.place(x=380, y=10, width=80, height=30)
        btn2.place(x=500, y=10, width=80, height=30)
        self.canvas = Canvas(self.tk, width=500, height=400,
                             bd=0, highlightthickness=0, background='#FFFFFF')
        self.canvas.place(x=190, y=90, width=500, height=400)

        self.tk.update()
        self.xunhuan()

    def xunhuan(self):
        try:
            paddle = Paddle(self.canvas, 'green', 100)
            ball = Ball(self.canvas, paddle, '#D11C43', 0)
            while True:
                if ball.hit_bottom == False:
                    ball.draw()
                    paddle.draw()
                else:
                    b = messagebox.askyesno(
                        '失败', message="您的分数为：" + str(ball.score) + "\n是否重新开始游戏?")
                    if bool(b) is True:
                        paddle.canvas.delete(paddle.id)
                        self.sever()
                    else:
                        sys.exit()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01 + self.times)
        except:
            sys.exit('游戏已退出!')

    def sever(self):
        self.xunhuan()

    def test1(self):
        self.times += 0.001

    def test2(self):
        self.times -= 0.001


class Ball:
    def __init__(self, canvas, paddle, color, score):
        self.score = 0
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(
            20, 20, 35, 35, fill=color, outline='green')
        self.canvas.move(self.id, 245, 100)
        startx = [-3, -2, -1, 1, 2, 3]
        random.shuffle(startx)
        self.x = startx[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        b = messagebox.askyesno('game', '游戏是否开始?')
        if bool(b) is True:
            self.draw()
        else:
            sys.exit()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or self.hit_paddle(pos) == True:
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score += 1
                return True
        return False


class Paddle:
    def __init__(self, canvas, color, width):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, width, 10, fill=color)
        self.x = 0
        self.y = 0
        self.canvas.move(self.id, 200, 300)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<Key-Left>", self.turn_left)
        self.canvas.bind_all("<Key-Right>", self.turn_right)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] + self.x >= 0 and pos[2] + self.x <= self.canvas_width:
            self.canvas.move(self.id, self.x, 0)

    def turn_left(self, event):
        self.x = -4

    def turn_right(self, event):
        self.x = 4


def main():
    game = Game()


if __name__ == '__main__':
    main()
