#terminal이나 cmd에 "pip install tk" 입력하구 실행해줘~

import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw

#더미 이미지 생성
img = Image.new("RGB",(640,480), (255,255,255))
d = ImageDraw.Draw(img)

img.save('temp.png')

#종류 변수 선언
메인피더 = '\u2610'           #메인피더
연계피더 = '\u2610'           #피더
분기점 = '┴'
수평부하 = '\u2500'     #수평방향 선로
수직부하 = '\u2502'     #수직방향 선로
sw = '\u25CB'           #개폐기
reset = ''

jh = [
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], 
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
]

win = tk.Tk()
win.geometry("1400x900")
win.resizable(True, True)
win.title("10JO")

def on_button_click(button): #frame2 노드 받아오기 /종호좌표계 형태 유지 /frmae1과 협조 필요..

        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][0] = int(button['text'][:button['text'].find(',')])
        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][1] = int(button['text'][button['text'].find(',')+1:])
        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][2] = globals()[number.get()] #문자열 변수화
        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][3] = name_entered.get()
        button.configure(text=globals()[number.get()])
        
        draww()

def on_save_click():
       np.save('jh.npy', jh)
       messagebox.showinfo("시스템 알림", "저장이 완료되었습니다!")
            
def on_load_click():
        global jh

        jh = np.load('jh.npy')
        messagebox.showinfo("시스템 알림", "불러오기가 완료되었습니다!")

        draww()

        return jh

def on_grid_click():
       plt.savefig('grid.png')
       messagebox.showinfo("시스템 알림", "계통도 출력이 완료되었습니다!")

#frame1_____________________________________________________________________________
frame = tk.LabelFrame(win, text='조작 기판', padx=15, pady=15) 
frame.pack(side="left", padx=10, pady=10) 

fframe = tk.LabelFrame(frame, text='입력을 마친 후, 대상 노드를 클릭해주세요.', padx=15, pady=15) 
fframe.pack()

fframe2 = tk.LabelFrame(frame, text='기능 키', padx=15, pady=15) 
fframe2.pack(side="left")

save = ttk.Button(fframe2, text="저장하기")
save.pack(side="top",padx=1, pady=5)
save.config(command=on_save_click)

load = ttk.Button(fframe2, text="불러오기")
load.pack(padx=1, pady=5)
load.config(command=on_load_click)

grid = ttk.Button(fframe2, text="계통도 png로 출력하기")
grid.pack(padx=1, pady=5)
grid.config(command=on_grid_click)

number = tk.StringVar()
number_chosen = ttk.Combobox(fframe, width=15, textvariable=number, state='readonly')
number_chosen['values'] = ("reset","메인피더","연계피더","수평부하","수직부하","분기점","sw") #list 읽을 때, 유니코드로 해석하도록 설계
number_chosen.pack()
number_chosen.current(0)

name = tk.StringVar()
name_entered = ttk.Entry(fframe, width=15, textvariable=name)
name_entered.pack()

#frmae2_________________________________________________
frame2 = tk.LabelFrame(win, text="노드", padx=15, pady=10) 
frame2.pack(fill="both", expand=False, padx=15, pady=10) 

for y in range(9):
   for x in range(15):
      button = tk.Button(frame2, text=f"{y}, {x}")
      button.config(command=lambda button=button: on_button_click(button))
      button.grid(column=x, row=y)

#frmae3 /주혁이형 출력물을 띄웁니다~ ____________________________
frame3 = tk.LabelFrame(win, text="계통도", padx=10, pady=10) 
frame3.pack(fill="both", expand=True, padx=10, pady=10) 

image=tk.PhotoImage(file="temp.png")
label0 = ttk.Label(frame3, image=image)
label0.pack()


def draww():

        global image, jh

        fig, ax = plt.subplots(1,1)

        # x 축의 범위를 0에서 까지로 지정 #행, 열 값을 받아와서 설정 
        plt.xlim(0, 20)
        # y 축의 범위를 0에서 까지로 지정
        plt.ylim(0, 20)
        # x 축의 눈금 단위 나타내지 x
        plt.xticks([])
        # y 축의 눈금 단위 나타내지 x 
        plt.yticks([])
        # x축과 y축 뒤집기
        plt.gca().invert_yaxis()
        # x축 위치 바꾸기
        ax = plt.gca() # 현재 그래프의 축 객체 가져오기
        ax.xaxis.set_ticks_position('top') # x축 위치를 위쪽으로 지정

        for i in range(9):
                for j in range(15):
                        if jh[i][j][2] == reset : #공백 처리 
                                ax.text(j, i, '' , fontsize=12)

                        elif jh[i][j][2] == 메인피더 : #피더 생성 
                                ax.text(j, i, '\u2610' , fontsize=12)

                        elif jh[i][j][2] == 연계피더 : #피더 생성 
                                ax.text(j, i, '\u2610' , fontsize=12)

                        elif jh[i][j][2] == 분기점 :  
                                ax.text(j, i, '┴' , fontsize=12)                
                        
                        elif jh[i][j][2] == 수평부하 : #피더 수평 직선 생성
                                ax.text(j, i, '──' , fontsize=12)

                        elif jh[i][j][2] == 수직부하 : #피더 수직 직선 생성 
                                ax.text(j+0.1, i, '│' , fontsize=12)

                        elif jh[i][j][2] == sw :     #개폐기 생성 
                                ax.text(j+0.03, i, '\u25CB' , fontsize=12)

        #spines 숨기기
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.tick_params(labelbottom=False, labelleft=False)
        plt.tick_params(labeltop=False, labelright=False)
        
        plt.savefig("plt.png")
        image=tk.PhotoImage(file="plt.png")
        os.remove("plt.png")
        os.remove("temp.png")
        label0.configure(image=image)
        
        # label.configure(image=image)
        # canvas = FigureCanvasTkAgg(fig, master=frame3)
        # canvas.draw()
        # canvas.get_tk_widget().pack()
        # canvas.get_tk_widget().destroy()

name_entered.focus()
win.mainloop()