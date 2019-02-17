# -*- coding: utf8 -*-
import psutil
from tkinter import *
import threading

k = 0


def fun_timer():
    global k
    temp = psutil.sensors_temperatures()
    var1.set(temp['acpitz'][0])
    var2.set(temp['radeon'][0])
    var3.set(temp['coretemp'][0])
    var4.set(temp['coretemp'][1])
    var5.set(k)
    k += 1
    global timer
    timer = threading.Timer(1, fun_timer)
    timer.start()


timer = threading.Timer(1, fun_timer)


def start():
    global timer
    timer.start()


# gu
window = Tk()
window.title('show sensor')
window.geometry('500x500')

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
label = Label(window, textvariable=var1, bg='green', font=('Arial', 12), width=50, height=2)
label.pack()
label = Label(window, textvariable=var2, bg='green', font=('Arial', 12), width=50, height=2)
label.pack()
label = Label(window, textvariable=var3, bg='green', font=('Arial', 12), width=50, height=2)
label.pack()
label = Label(window, textvariable=var4, bg='green', font=('Arial', 12), width=50, height=2)
label.pack()
label = Label(window, textvariable=var5, bg='green', font=('Arial', 12), width=50, height=2)
label.pack()
# window.protocol('WM_SHOW_WINDOW', start)
button = Button(window, text='start', width=15, height=2, command=start)     # 点击按钮式执行的命令
button.pack()    # 按钮位置
window.mainloop()

# from pyspectator.processor import Cpu
# from time import sleep
# cpu = Cpu(monitoring_latency=1)
#
# while True:
#     print (cpu.temperature)
#     sleep(1)