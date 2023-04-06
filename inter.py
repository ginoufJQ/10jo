import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("600x400")
win.resizable(False, False)
win.title("10JO")

def click_me():
    list = [0,0,name_entered.get(),number.get()]
    print(list)

frame = tk.LabelFrame(win, text='', padx=15, pady=15) 
frame.pack(padx=10, pady=10) 

ttk.Label(frame, text="종류를 선택해주세요.").grid(column=0, row=0)

number = tk.StringVar()
number_chosen = ttk.Combobox(frame, width=15, textvariable=number, state='readonly')
number_chosen['values'] = ("Feeder", "Load", "Switch", "Line")
number_chosen.grid(column=0, row=1)
number_chosen.current(0)

ttk.Label(frame, text="용량을 입력해주세요.").grid(column=1, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(frame, width=15, textvariable=name)
name_entered.grid(column=1, row=1)

action = ttk.Button(frame, text="확인", command=click_me)
action.grid(column=2, row=1)

frame2 = tk.LabelFrame(win, text="계통도", padx=10, pady=10) 
frame2.pack(fill="both", expand=True, padx=10, pady=10) 
ttk.Label(frame2, text="다음칸에 주혁이형 알고리즘!").place(x=0, y=100)

# grid 자동 생성
for r in range(3):
   for c in range(4):
      Tkinter.Label(root, text='R%s/C%s'%(r,c),
         borderwidth=1 ).grid(row=r,column=c
                              
b1=tk.Button(frame2)
b2=tk.Button(frame2)
b3=tk.Button(frame2)
b4=tk.Button(frame2)
b5=tk.Button(frame2)
b6=tk.Button(frame2)
b7=tk.Button(frame2)
b8=tk.Button(frame2)
b9=tk.Button(frame2)
b10=tk.Button(frame2)
b11=tk.Button(frame2)
b12=tk.Button(frame2)
b13=tk.Button(frame2)
b14=tk.Button(frame2)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=3, column=3)
b5.grid(row=3, column=4)
b6.grid(row=3, column=5)
b7.grid(row=3, column=6)
b8.grid(row=3, column=7)
b9.grid(row=3, column=8)
b10.grid(row=3, column=9)
b11.grid(row=3, column=10)
b12.grid(row=3, column=11)
b13.grid(row=3, column=12)
b14.grid(row=3, column=13)

name_entered.focus()

win.mainloop()