#terminal이나 cmd에 "pip install tk" 입력하구 실행해줘~

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("980x900")
win.resizable(True, True)
win.title("10JO")

def on_button_click(button): #frame2 노드 받아오기 /종호좌표계 형태 유지 /frmae1과 협조 필요..
        print(button['text'])
        #list 생성하기 / 여긴 종호가 하자??
        list = [button['text'][:button['text'].find(',')],button['text'][button['text'].find(','):],name_entered.get(),number.get()]
        print(list)
        #여기서부턴 주혁이형 알고리즘 넣기..

#frame1
frame = tk.LabelFrame(win, text='입력을 마친 후, 대상 노드를 클릭해주세요.', padx=15, pady=15) 
frame.pack(padx=10, pady=10) 

ttk.Label(frame, text="종류를 선택해주세요.").grid(column=0, row=0)

number = tk.StringVar()
number_chosen = ttk.Combobox(frame, width=15, textvariable=number, state='readonly')
number_chosen['values'] = ("","Feeder", "Load", "Switch", "Line") #공백은 리스트에서 0으로 변환하자
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

name_entered.focus()

win.mainloop()