# -*- coding: utf8 -*-
import os
import chardet
import time
import shutil
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import tkinter.filedialog as dlg_dir


def selectdir():
    strtemp=dlg_dir.askdirectory(title="选择源文件夹:")
    str_selecteddir.set(strtemp)


def targetdir():
    strtemp=dlg_dir.askdirectory(title="选择目标文件夹:")
    str_targetdir.set(strtemp)


def fenlei():
    if str_selecteddir.get()=='' or str_targetdir.get()=='':
        showinfo('错误！',"请选择源文件夹和目标文件夹！",icon="error")
    else:
        export = ""
        for root,dirs,files in os.walk(str_selecteddir.get()):	
            for f in files:
                try:
                    export=os.path.join(root,f)
                    a1,a2,a3,a4,a5,a6,a7,a8,a9,a10=os.stat(export)
                    b1,b2,b3,b4,b5,b6,b7,b8,b9=time.gmtime(a10)
                    mubiao=str_targetdir.get()+'/'+str(b1)+'年'+str(b2)+'月'
                    if os.path.exists(mubiao)==False:
                        os.mkdir(mubiao)
                    if os.path.isfile(os.path.join(mubiao,f)):
                        os.rename(os.path.join(mubiao,f),os.path.join(mubiao,'《同名区分》'+f))
                              
                    shutil.move(export,mubiao)
                    text_process.insert(INSERT,'★moved...'+export+'...to...'+mubiao+'\n')
                except:
                    showinfo('错误！',"请关闭源文件夹中被打开的文件！",icon="error")
        
        
    







#---------创建界面---------
tk=Tk()
tk.title("文件按月分类存放")
tk.geometry("400x400+100+100")

frame1=Frame(tk)
frame1.pack(fill=BOTH,expand=1)

btn_selectdir=Button(frame1,width=15,height=1,text='选择源文件夹',command=selectdir)
btn_selectdir.place(x=10,y=10)

btn_targetdir=Button(frame1,width=15,height=1,text='选择目标文件夹',command=targetdir)
btn_targetdir.place(x=120,y=10)

btn_fenlei=Button(frame1,width=15,height=1,text='开始分类',command=fenlei)
btn_fenlei.place(x=230,y=10)

lbl_selecteddir=Label(frame1,width=15,height=1,text="所选文件夹：")
lbl_selecteddir.place(x=10,y=40)

lbl_targetdir=Label(frame1,width=15,height=1,text="目标文件夹：")
lbl_targetdir.place(x=10,y=70)

str_selecteddir=StringVar()
ety_selecteddir=Entry(frame1,width=34,textvariable=str_selecteddir)
ety_selecteddir.place(x=120,y=40)

str_targetdir=StringVar()
ety_targetdir=Entry(frame1,width=34,textvariable=str_targetdir)
ety_targetdir.place(x=120,y=70)

text_process=Text(frame1,width=45,height=14,yscrollcommand=1)
text_process.place(x=10,y=100)






tk.mainloop()
