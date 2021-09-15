from tkinter import *
import math


def main():
    root = Tk()
    canvas = Canvas()

    x = 0
    y = 1000

    for i in range(20):
        canvas.create_line(x+80*math.sqrt(2), 0, 1000, y - 80*math.sqrt(2))
        canvas.create_line(0, x+80*math.sqrt(2), y - 80*math.sqrt(2), 1000)
        x += 80*math.sqrt(2)
        y -= 80*math.sqrt(2)

    x = 0
    y = 0

    for j in range(20):
        if j % 2 == 0:
            canvas.create_line(x + 80*math.sqrt(2), 0, 0, y + 80*math.sqrt(2), dash=(80, 80), dashoff=0)
        else:
            canvas.create_line(x + 80*math.sqrt(2), 0, 0, y + 80*math.sqrt(2), dash=(80, 80))
        x += 80*math.sqrt(2)
        y += 80*math.sqrt(2)

    canvas.create_line(0, 0, 1000, 1000)

    canvas['bg'] = 'brown'
    canvas.config(width=1000, height=1000)
    canvas.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
