#terminal이나 cmd에 "pip install tk" 입력하구 실행해줘~

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

#종류 변수 선언
fd = '\u2610'           #피더
hline_fd = '\u2500'     #피더에 연결된 수평방향 선로
vline_fd = '\u2502'     #피더에 연결된 수직방향 선로
hline_load = '\u2500'   #부하에 연결된 수평방향 선로
vline_load = '\u2502'   #부하에 연결된 수직방향 선로
sw = '\u25CB'           #개폐기

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
win.geometry("980x900")
win.resizable(True, True)
win.title("10JO")

def on_button_click(button): #frame2 노드 받아오기 /종호좌표계 형태 유지 /frmae1과 협조 필요..
        # print(int(button['text'][:button['text'].find(',')]))
        # print(int(button['text'][button['text'].find(',')+1:]))

        # jh 리스트 생성
        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][0] = int(button['text'][:button['text'].find(',')])
        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][1] = int(button['text'][button['text'].find(',')+1:])
        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][2] = globals()[number.get()] #문자열 변수화
        jh[int(button['text'][:button['text'].find(',')])][int(button['text'][button['text'].find(',')+1:])][3] = name_entered.get()
        
        #여기서부턴 주혁이형 알고리즘 넣기..
        draww()
        
#frame1
frame = tk.LabelFrame(win, text='입력을 마친 후, 대상 노드를 클릭해주세요.', padx=15, pady=15) 
frame.pack(padx=10, pady=10) 

ttk.Label(frame, text="종류를 선택해주세요.").grid(column=0, row=0)

number = tk.StringVar()
number_chosen = ttk.Combobox(frame, width=15, textvariable=number, state='readonly')
number_chosen['values'] = ("0","fd","hline_fd","vline_fd", "hline_load", "vline_load", "sw") #list 읽을 때, 유니코드로 해석하도록 설계
number_chosen.grid(column=0, row=1)
number_chosen.current(0)

ttk.Label(frame, text="용량을 입력해주세요.").grid(column=1, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(frame, width=15, textvariable=name)
name_entered.grid(column=1, row=1)

#frmae2
frame2 = tk.LabelFrame(win, text="노드", padx=15, pady=10) 
frame2.pack(fill="both", expand=False, padx=15, pady=10) 

# grid 자동 생성
for y in range(9):
   for x in range(15):
      button = tk.Button(frame2, text=f"{y}, {x}")
      button.config(command=lambda button=button: on_button_click(button))
      button.grid(column=x, row=y)

#frmae3 /주혁이형 출력물을 띄웁니다~
frame3 = tk.LabelFrame(win, text="계통도", padx=10, pady=10) 
frame3.pack(fill="both", expand=True, padx=10, pady=10) 


def draww():

        fig, ax = plt.subplots()

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
                        if jh[i][j][2] == 0 : #공백 처리 
                                plt.plot([])
                        
                        elif jh[i][j][2] == fd : #피더 생성 
                                ax.text(j, i, '\u2610' , fontsize=12)
                        
                        elif jh[i][j][2] == hline_fd : #피더 수평 직선 생성
                                ax.text(j, i, '──' , fontsize=12)

                        elif jh[i][j][2] == vline_fd : #피더 수직 직선 생성 
                                ax.text(j+0.1, i, '│' , fontsize=12)

                        elif jh[i][j][2] == hline_load : #부하 수평 직선 생성 
                                ax.text(j, i, '──' , fontsize=12)

                        elif jh[i][j][2] == vline_load : #부하 수직 직선 생성 
                                ax.text(j, i, '│' , fontsize=12)

                        else :                          #개폐기 생성 
                                ax.text(j+0.03, i, '\u25CB' , fontsize=12)

        #spines 숨기기
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.tick_params(labelbottom=False, labelleft=False)
        plt.tick_params(labeltop=False, labelright=False)

        # if canvas: canvas.get_tk_widget().pack_forget()

        
        canvas = FigureCanvasTkAgg(fig, master=frame3)
        canvas.draw()
        canvas.get_tk_widget().pack()
        

name_entered.focus()
win.mainloop()