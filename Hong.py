import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import Image
import mplcursors
import mpldatacursor
from mpldatacursor import HighlightingDataCursor
from matplotlib.collections import LineCollection



#종류 변수 선언
mf = 100           #메인피더
fd = 101          #피더
frk1 = 102        #분기점(ㅗ)
frk2 = 103        #분기점(ㅜ)
frk3 = 104        #분기점(십자모양)
frk4 = 106        #분기점(┘)
frk5 = 107        #분기점(┐)
hline = 108       #수평방향 선로
vline = 109       #수직방향 선로
sw = 110          #개폐기


jh = [
    [[0,0,0,0,0],[0,1,0,0,0],[0,2,0,0,0],[0,3,0,0,0],[0,4,0,0,0],[0,5,0,0,0],[0,6,0,0,0],[0,7,0,0,0],[0,8,0,0,0],[0,9,0,0,0],[0,10,0,0,0],[0,11,0,0,0],[0,12,0,0,0],[0,13,0,0,0],[0,14,0,0,0],[0,15,fd,0,0],[0,16,0,0,0],[0,17,0,0,0],[0,18,0,0,0],[0,19,0,0,0],[0,20,0,0,0]],
    [[1,0,0,0,0],[1,1,0,0,0],[1,2,0,0,0],[1,3,0,0,0],[1,4,0,0,0],[1,5,0,0,0],[1,6,0,0,0],[1,7,0,0,0],[1,8,0,0,0],[1,9,0,0,0],[1,10,0,0,0],[1,11,0,0,0],[1,12,0,0,0],[1,13,0,0,0],[1,14,0,0,0],[1,15,vline,100,0],[1,16,0,0,0],[1,17,0,0,0],[1,18,0,0,0],[1,19,0,0,0],[1,20,0,0,0]],
    [[2,0,0,0,0],[2,1,0,0,0],[2,2,0,0,0],[2,3,0,0,0],[2,4,0,0,0],[2,5,0,0,0],[2,6,0,0,0],[2,7,0,0,0],[2,8,0,0,0],[2,9,0,0,0],[2,10,0,0,0],[2,11,0,0,0],[2,12,0,0,0],[2,13,0,0,0],[2,14,0,0,0],[2,15,sw,0,0],[2,16,0,0,0],[2,17,0,0,0],[2,18,0,0,0],[2,19,0,0,0],[2,20,0,0,0]],
    [[3,0,0,0,0],[3,1,0,0,0],[3,2,0,0,0],[3,3,0,0,0],[3,4,0,0,0],[3,5,0,0,0],[3,6,0,0,0],[3,7,0,0,0],[3,8,0,0,0],[3,9,0,0,0],[3,10,0,0,0],[3,11,0,0,0],[3,12,0,0,0],[3,13,0,0,0],[3,14,0,0,0],[3,15,vline,200,0],[3,16,0,0,0],[3,17,0,0,0],[3,18,0,0,0],[3,19,0,0,0],[3,20,0,0,0]],
    [[4,0,0,0,0],[4,1,0,0,0],[4,2,0,0,0],[4,3,0,0,0],[4,4,0,0,0],[4,5,0,0,0],[4,6,0,0,0],[4,7,0,0,0],[4,8,0,0,0],[4,9,0,0,0],[4,10,0,0,0],[4,11,fd,4000,0],[4,12,0,0,0],[4,13,0,0,0],[4,14,0,0,0],[4,15,sw,0,0],[4,16,0,0,0],[4,17,0,0,0],[4,18,0,0,0],[4,19,0,0,0],[4,20,0,0,0]],
    [[5,0,0,0,0],[5,1,0,0,0],[5,2,0,0,0],[5,3,0,0,0],[5,4,0,0,0],[5,5,0,0,0],[5,6,0,0,0],[5,7,0,0,0],[5,8,0,0,0],[5,9,0,0,0],[5,10,0,0,0],[5,11,vline,0,0],[5,12,0,0,0],[5,13,0,0,0],[5,14,0,0,0],[5,15,vline,300,0],[5,16,0,0,0],[5,17,0,0,0],[5,18,0,0,0],[5,19,0,0,0],[5,20,0,0,0]],
    [[6,0,0,0,0],[6,1,0,0,0],[6,2,0,0,0],[6,3,0,0,0],[6,4,0,0,0],[6,5,0,0,0],[6,6,0,0,0],[6,7,0,0,0],[6,8,0,0,0],[6,9,0,0,0],[6,10,0,0,0],[6,11,sw,0,0],[6,12,0,0,0],[6,13,0,0,0],[6,14,0,0,0],[6,15,sw,0,0],[6,16,0,0,0],[6,17,0,0,0],[6,18,0,0,0],[6,19,0,0,0],[6,20,0,0,0]],
    [[7,0,0,0,0],[7,1,0,0,0],[7,2,0,0,0],[7,3,0,0,0],[7,4,0,0,0],[7,5,0,0,0],[7,6,0,0,0],[7,7,0,0,0],[7,8,0,0,0],[7,9,0,0,0],[7,10,0,0,0],[7,11,vline,400,0],[7,12,0,0,0],[7,13,0,0,0],[7,14,0,0,0],[7,15,vline,500,0],[7,16,0,0,0],[7,17,0,0,0],[7,18,0,0,0],[7,19,0,0,0],[7,20,0,0,0]],
    [[8,0,0,0,0],[8,1,0,0,0],[8,2,0,0,0],[8,3,0,0,0],[8,4,0,0,0],[8,5,0,0,0],[8,6,0,0,0],[8,7,0,0,0],[8,8,0,0,0],[8,9,0,0,0],[8,10,0,0,0],[8,11,sw,0,0],[8,12,0,0,0],[8,13,0,0,0],[8,14,0,0,0],[8,15,sw,0,0],[8,16,0,0,0],[8,17,0,0,0],[8,18,0,0,0],[8,19,0,0,0],[8,20,0,0,0]],
    [[9,0,mf,14000,0],[9,1,hline,0,0],[9,2,sw,0,0],[9,3,hline,600,0],[9,4,sw,0,0],[9,5,hline,700,0],[9,6,sw,0,0],[9,7,frk2,100,0],[9,8,sw,0,0],[9,9,hline,200,0],[9,10,sw,0,0],[9,11,frk1,300,0],[9,12,sw,0,0],[9,13,hline,400,0],[9,14,sw,0,0],[9,15,frk1,500,0],[9,16,sw,0,0],[9,17,frk2,600,0],[9,18,sw,0,0],[9,19,hline,0,0],[9,20,fd,5000,0]],
    [[10,0,0,0,0],[10,1,0,0,0],[10,2,0,0,0],[10,3,0,0,0],[10,4,0,0,0],[10,5,0,0,0],[10,6,0,0,0],[10,7,sw,0,0],[10,8,0,0,0],[10,9,0,0,0],[10,10,0,0,0],[10,11,0,0,0],[10,12,0,0,0],[10,13,0,0,0],[10,14,0,0,0],[10,15,0,0,0],[10,16,0,0,0],[10,17,sw,0,0],[10,18,0,0,0],[10,19,0,0,0],[10,20,0,0,0]],
    [[11,0,0,0,0],[11,1,0,0,0],[11,2,0,0,0],[11,3,0,0,0],[11,4,0,0,0],[11,5,0,0,0],[11,6,0,0,0],[11,7,vline,700,0],[11,8,0,0,0],[11,9,0,0,0],[11,10,0,0,0],[11,11,0,0,0],[11,12,0,0,0],[11,13,0,0,0],[11,14,0,0,0],[11,15,0,0,0],[11,16,0,0,0],[11,17,vline,100,0],[11,18,0,0,0],[11,19,0,0,0],[11,20,0,0,0]],
    [[12,0,0,0,0],[12,1,0,0,0],[12,2,0,0,0],[12,3,0,0,0],[12,4,0,0,0],[12,5,0,0,0],[12,6,0,0,0],[12,7,sw,0,0],[12,8,0,0,0],[12,9,0,0,0],[12,10,0,0,0],[12,11,0,0,0],[12,12,0,0,0],[12,13,0,0,0],[12,14,0,0,0],[12,15,0,0,0],[12,16,0,0,0],[12,17,sw,0,0],[12,18,0,0,0],[12,19,0,0,0],[12,20,0,0,0]],
    [[13,0,0,0,0],[13,1,0,0,0],[13,2,0,0,0],[13,3,0,0,0],[13,4,0,0,0],[13,5,0,0,0],[13,6,0,0,0],[13,7,vline,200,0],[13,8,0,0,0],[13,9,0,0,0],[13,10,0,0,0],[13,11,0,0,0],[13,12,0,0,0],[13,13,0,0,0],[13,14,0,0,0],[13,15,0,0,0],[13,16,0,0,0],[13,17,vline,300,0],[13,18,0,0,0],[13,19,0,0,0],[13,20,0,0,0]],
    [[14,0,0,0,0],[14,1,0,0,0],[14,2,0,0,0],[14,3,0,0,0],[14,4,0,0,0],[14,5,0,0,0],[14,6,0,0,0],[14,7,sw,0,0],[14,8,0,0,0],[14,9,0,0,0],[14,10,0,0,0],[14,11,0,0,0],[14,12,0,0,0],[14,13,0,0,0],[14,14,0,0,0],[14,15,0,0,0],[14,16,0,0,0],[14,17,sw,0,0],[14,18,0,0,0],[14,19,0,0,0],[14,20,0,0,0]],
    [[15,0,0,0,0],[15,1,0,0,0],[15,2,0,0,0],[15,3,0,0,0],[15,4,0,0,0],[15,5,0,0,0],[15,6,0,0,0],[15,7,vline,400,0],[15,8,0,0,0],[15,9,0,0,0],[15,10,0,0,0],[15,11,0,0,0],[15,12,0,0,0],[15,13,0,0,0],[15,14,0,0,0],[15,15,0,0,0],[15,16,0,0,0],[15,17,vline,500,0],[15,18,0,0,0],[15,19,0,0,0],[15,20,0,0,0]],
    [[16,0,0,0,0],[16,1,0,0,0],[16,2,0,0,0],[16,3,0,0,0],[16,4,0,0,0],[16,5,0,0,0],[16,6,0,0,0],[16,7,sw,0,0],[16,8,0,0,0],[16,9,0,0,0],[16,10,0,0,0],[16,11,0,0,0],[16,12,0,0,0],[16,13,0,0,0],[16,14,0,0,0],[16,15,0,0,0],[16,16,0,0,0],[16,17,sw,0,0],[16,18,0,0,0],[16,19,0,0,0],[16,20,0,0,0]],
    [[17,0,0,0,0],[17,1,0,0,0],[17,2,0,0,0],[17,3,0,0,0],[17,4,0,0,0],[17,5,0,0,0],[17,6,0,0,0],[17,7,vline,0,0],[17,8,0,0,0],[17,9,0,0,0],[17,10,0,0,0],[17,11,0,0,0],[17,12,0,0,0],[17,13,0,0,0],[17,14,0,0,0],[17,15,0,0,0],[17,16,0,0,0],[17,17,vline,600,0],[17,18,0,0,0],[17,19,0,0,0],[17,20,0,0,0]],
    [[18,0,0,0,0],[18,1,0,0,0],[18,2,0,0,0],[18,3,0,0,0],[18,4,0,0,0],[18,5,0,0,0],[18,6,0,0,0],[18,7,fd,6000,0],[18,8,0,0,0],[18,9,0,0,0],[18,10,0,0,0],[18,11,0,0,0],[18,12,0,0,0],[18,13,0,0,0],[18,14,0,0,0],[18,15,0,0,0],[18,16,0,0,0],[18,17,sw,0,0],[18,18,0,0,0],[18,19,0,0,0],[18,20,0,0,0]],
    [[19,0,0,0,0],[19,1,0,0,0],[19,2,0,0,0],[19,3,0,0,0],[19,4,0,0,0],[19,5,0,0,0],[19,6,0,0,0],[19,7,0,0,0],[19,8,0,0,0],[19,9,0,0,0],[19,10,0,0,0],[19,11,0,0,0],[19,12,0,0,0],[19,13,0,0,0],[19,14,0,0,0],[19,15,0,0,0],[19,16,0,0,0],[19,17,vline,700,0],[19,18,0,0,0],[19,19,0,0,0],[19,20,0,0,0]],
    [[20,0,0,0,0],[20,1,0,0,0],[20,2,0,0,0],[20,3,0,0,0],[20,4,0,0,0],[20,5,0,0,0],[20,6,0,0,0],[20,7,0,0,0],[20,8,0,0,0],[20,9,0,0,0],[20,10,0,0,0],[20,11,0,0,0],[20,12,0,0,0],[20,13,0,0,0],[20,14,0,0,0],[20,15,0,0,0],[20,16,0,0,0],[20,17,sw,0,0],[20,18,0,0,0],[20,19,0,0,0],[20,20,0,0,0]],
    [[21,0,0,0,0],[21,1,0,0,0],[21,2,0,0,0],[21,3,0,0,0],[21,4,0,0,0],[21,5,0,0,0],[21,6,0,0,0],[21,7,0,0,0],[21,8,0,0,0],[21,9,0,0,0],[21,10,0,0,0],[21,11,0,0,0],[21,12,0,0,0],[21,13,0,0,0],[21,14,0,0,0],[21,15,0,0,0],[21,16,0,0,0],[21,17,vline,0,0],[21,18,0,0,0],[21,19,0,0,0],[21,20,0,0,0]],
    [[22,0,0,0,0],[22,1,0,0,0],[22,2,0,0,0],[22,3,0,0,0],[22,4,0,0,0],[22,5,0,0,0],[22,6,0,0,0],[22,7,0,0,0],[22,8,0,0,0],[22,9,0,0,0],[22,10,0,0,0],[22,11,0,0,0],[22,12,0,0,0],[22,13,0,0,0],[22,14,0,0,0],[22,15,0,0,0],[22,16,0,0,0],[22,17,fd,7000,0],[22,18,0,0,0],[22,19,0,0,0],[22,20,0,0,0]],
]

# 서브피더, 부하, 분기점에 대한 리스트 먼저 만들어줘야 전역변수 쓸 수 있음
# 먼저 5번째 원소 넣은다음에


################################ 부하, 서브피더, 분기점 리스트 만들기

n1 = na = nb = 0

# 연계피더 개수 찾는 구문(F1, F2, F3,,, 매기기 위해서)
for i in range(23):
    for j in range(21):
        if jh[i][j][2] == fd and jh[i][j][3] != 14000:
            n1 += 1

# 부하 개수 찾는 구문(Z1, Z2, Z3,,, 매기기 위해서)
for i in range(23):
    for j in range(21):
        if (jh[i][j][2] == hline or jh[i][j][2] == vline) and jh[i][j][3] != 0:
            na += 1

# 분기점 개수 찾는 구문(Z1, Z2, Z3,,, 매기기 위해서)
for i in range(23):
    for j in range(21):
        if jh[i][j][2] == frk1 or jh[i][j][2] == frk2:     
            nb += 1

n2 = na + nb

#print(n1, n2, na, nb)   # 이제 이 숫자로 리스트 폼 만들고나서 jh에 tag 할당할거임


######################### 태그 만들기
def F(i):
    return "F"+str(i)

def Load(i):
    return "Z"+str(i)

SF = []
Z = []
FRK = []

for i in range(1,n1+1):
    SF.append(F(i))

for i in range(1, n2+1):
    Z.append(Load(i))


########################## 배열의 각 5번째 원소에 태그 할당하기
a=b=0

for i in range(23):
    for j in range(21):
        if jh[i][j][2] == fd:   # 종류가 피더이면 연계피더
            jh[i][j][4] = SF[a] # 연계피더일때 F1, F2,,, 태그 할당
            a += 1

for i in range(23):
    for j in range(21):
        if ((jh[i][j][2] == hline or jh[i][j][2] == vline) and jh[i][j][3] != 0) or jh[i][j][2] == frk1 or jh[i][j][2] == frk2:    # 종류가 선로이면서 용량이 0이 아니거나 / 분기점일때 부하로 본다
            jh[i][j][4] = Z[b]                                                                                                                                                             # 부하일때 Z1, Z2,,, 태그 할당
            b += 1

for i in range(23):
    for j in range(21):
        if jh[i][j][2] == frk1 or jh[i][j][2] == frk2:  # 종류가 분기점이면
            FRK.append(jh[i][j][4])                                   # 분기점 리스트에 추가한다 # 근데 이거 이제 필요없잖아

for i in range(23):
    for j in range(21):
        if jh[i][j][2] == mf:
            jh[i][j][4] = "F"


##################################### 라인 리스트 만들기

# 메인피더의 x좌표, y좌표 구하기
mx=my=0     
for i in range(23):
    for j in range(21):
        if jh[i][j][2] == mf:     # 종류가 메인피더일때
            my = jh[i][j][0]      # 행번호 저장
            mx = jh[i][j][1]      # 열번호 저장

#print(my,mx)

# 중복항을 포함한 프로토타입의 LL+"n" 리스트 생성
for i in range(1, n1+1):
    globals()['LL' + str(i)] = []

# 연계피더 개수만큼 빈 L리스트 생성
L0 = []                                       # 리스트 이름을 저장할 빈 리스트

for i in range(1, n1+1):
    L_name = 'L' + str(i)                     # 리스트 이름 생성
    L0.append(L_name)                         # 리스트 이름을 L 리스트에 추가
    exec("%s = []" % L_name)                  # 리스트 생성

# print(L0)

# 라인리스트 만드는 로직
p=1
for i in range(23):
    for j in range(21):
        if jh[i][j][2] == fd:      # jh에서 연계피더를 찾아
            x_num = abs(j - mx)                  # 행방향으로 L'p'리스트에 넣어줘야할 개수
            y_num = abs(my - i)                  # 열방향으로 L'p'리스트에 넣어줘야할 개수 
            if i <= my:          
                for q in range(i, i + y_num):
                    if jh[q][j][3] > 0 or jh[q][j][2] == fd:
                        globals()["LL" + str(p)].append(jh[q][j][4])
                for r in range(x_num, -1, -1):
                    if jh[my][r][3] > 0:    
                        globals()["LL" + str(p)].append(jh[my][r][4])
            if i > my:
                for q in range(i, i - y_num, -1):
                    if jh[q][j][3] > 0 or jh[q][j][2] == fd:
                        globals()["LL" + str(p)].append(jh[q][j][4])
                for r in range(x_num, -1, -1):
                    if jh[my][r][3] > 0:    
                        globals()["LL" + str(p)].append(jh[my][r][4])
            p+=1
        

# 중복항 제거하는 반복문 (분기점 부하가 중복됨)
for i in range(1, p):
    for value in globals()["LL" + str(i)]:
        if value not in globals()["L" + str(i)]:
            globals()["L" + str(i)].append(value)


############################ L리스트 만들기(간선 부하들 = 굵은가지 부하들)
L = []          # 일단 빈 리스트 생성

for i in range(23):
    for j in range(21):
        if i == my and (jh[i][j][2] == hline or jh[i][j][2] == vline or jh[i][j][2] == frk1 or jh[i][j][2] == frk2) and jh[i][j][3] != 0:
            L.append(jh[i][j][4])


# print(L1)
# print(L2)
# print(L3)
# print(L4)
# print(L5)
# print(L)


############################ dml 리스트 만들기
dml = []        # 일단 dml1, 2, 4, 5 담을 빈 리스트 선언

for i in range(23):
    for j in range(21):
        if jh[i][j][2] == fd and i != my:     # 분기점을 가진 연계피더 찾아
            index = jh[i][j][4][1]            # 연계피더의 tag정보에서 숫자만 추출
            dml_name = 'dml' + str(index)                   # 그 숫자로 dml1, 2, 4, 5 리스트 이름 생성
            dml.append(dml_name)                            # dml에 dml1, 2, 4, 5 넣음
            exec("%s = []" % dml_name)                      # dml1, 2, 4, 5는 빈 리스트로 생성 # 이후에 부하 tag 넣을거임

for i in range(23):
    for j in range(21):
        if jh[i][j][2] == fd and i != my:
            index = jh[i][j][4][1]
            y_num_dml = abs(my - i)
            if i < my:
                for p in range(i + y_num_dml, i, -1):
                    if jh[p][j][2] == vline and jh[p][j][3] > 0:
                        globals()['dml' + str(index)].append(jh[p][j][4])
            if i > my:
                for p in range(i - y_num_dml, i):
                    if jh[p][j][2] == vline and jh[p][j][3] > 0:
                        globals()['dml' + str(index)].append(jh[p][j][4])


# print(dml1)
# print(dml2)
# print(dml4)
# print(dml5)


ZRI_list =[[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
            [[-100], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
            [[-100], [-300], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
            [[-100], [-300], [-600], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
            [[-100], [-300], [-600], [3600], [-1100], [], [3900], [4600], [3100], [3300], [3500], [3900], [4400], [4700], [4800], [5400], [4900], [5600], [5200], [5700], [6300]],
            [[-100], [-300], [-600], [3600], [-1100], [], [], [4600], [3100], [3300], [3500], [3900], [4400], [4700], [4800], [5400], [4900], [5600], [5200], [5700], [6300]],
            [[-100], [-300], [-600], [3600], [-1100], [], [], [], [3100], [3300], [3500], [3900], [4400], [4700], [4800], [5400], [4900], [5600], [5200], [5700], [6300]],
            [[-100], [-300], [-600], [3600], [-1100], [], [], [], [], [3300], [3500], [3900], [4400], [], [4800], [], [4900], [], [5200], [5700], [6300]],
            [[-100], [-300], [-600], [3600], [-1100], [], [], [], [], [], [3500], [3900], [4400], [], [4800], [], [4900], [], [5200], [5700], [6300]],       
            [[-100], [-300], [-600], [], [-1100], [], [], [], [], [], [], [3900], [4400], [], [4800], [], [4900], [], [5200], [5700], [6300]],
            [[-100], [-300], [-600], [], [-1100], [], [], [], [], [], [], [], [4400], [], [4800], [], [4900], [], [5200], [5700], [6300]],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [4800], [], [4900], [], [5200], [5700], [6300]],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [5400], [], [5600], [], [], []],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [4900], [], [5200], [5700], [6300]],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [5600], [], [], []],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [5200], [5700], [6300]],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [5700], [6300]],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [6300]],
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]]

F = [[('선로증설함', 0.4, 5)], [('선로증설함', 0.39874125874125876, 5)], [('선로증설함', 0.3974825174825175, 5)], [], [('선로증설함', 0.35972027972027976, 5)], [], [], 
[], [], [], [], [], [], [], [], [], [], [], [], [], []]


for j in range(1, len(ZRI_list)+1):        #Z1 ... Zn의 모든 고장 구간별 고복지 리스트 
    globals()["result_list_" + str(j)] = [ZRI_list[i][j-1] for i in range(len(ZRI_list))]




count_list = []              #Z1 ....Zn의 모든 고장 구간별 고복지 음수 개수 리스트 
for j in range(1, len(ZRI_list)+1):
    result_list = globals()["result_list_" + str(j)]
    count = sum(1 for sublist in result_list for x in sublist if x and x < 0)
    count_list.append(count)

result_lists = []            
for j in range(1, len(ZRI_list)+1):
    result_lists.append(globals()["result_list_" + str(j)])


print(count_list)    

negative_indices_lists = []  #고장의 원인을 넣은 리스트 

for result_list in result_lists:  #음수가 되는 부분을 찾아서 위치를 찾기 
    negative_indices = [index + 1 for index, sublist in enumerate(result_list) for value in sublist if value < 0]
    negative_indices_lists.append(negative_indices)


Z_trouble = [index + 1 for index, sublist in enumerate(negative_indices_lists) if sublist] #고장 복구 불가 부분 반환 



def format_indices_lists(indices_lists):
    formatted_lists = []
    for indices in indices_lists:
        formatted_indices = [f'Z{index}' for index in indices]
        formatted_lists.append(formatted_indices)
    return formatted_lists

formatted_Z_trouble = format_indices_lists([Z_trouble])[0] #고장 복구 불가 부분 Zn꼴로 저장 
print(formatted_Z_trouble)



# negative_indices_lists를 Z 형식으로 변환, 복구 불가 원인 출력 
formatted_lists = format_indices_lists(negative_indices_lists)
print(formatted_lists)


def find_position(jh, Z, target):      #Z1, Z2, Z3 ...Zn의 좌표값을 찾아줌(진짜 좌표축에 넣을 때는 x,y 바꿔야됨) 
    for sublist in jh:                  #ex) [1,2]가 추출되면 사실상 좌표축에는 (2,1) 이렇게 들어가야 됨 
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

positions = [find_position(jh, Z, target) for target in Z]

y_coords = [position[0] for position in positions]    #Z의 x좌표값 ->좌표축으로 들어갈 때는 이게 y
x_coords = [position[1] for position in positions]    #Z의 y좌표값 ->좌표축으로 들어갈 때는 이게 x 


def find_position(jh, SF, target):      #F1, F2.....Fn의 좌표값을 찾아줌 
    for sublist in jh:
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

F_positions = [find_position(jh, SF, target) for target in SF]

print(F_positions)


def find_position(jh, formatted_Z_trouble, target):      #복구 불가인 Z의 좌표값을 찾아줌 
    for sublist in jh:
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

formatted_Z_trouble_positions = [find_position(jh, formatted_Z_trouble, target) for target in formatted_Z_trouble]

print(formatted_Z_trouble_positions)

y_Z_trouble = [position[0] for position in formatted_Z_trouble_positions]    #복구 불가 지점의 Z 좌표값 
x_Z_trouble = [position[1] for position in formatted_Z_trouble_positions]    

print(x_Z_trouble)
print(y_Z_trouble)

F_extracted = [] 

for sublist in F:   #선로 증설할 시, 연계피더 찾아서 F를 붙여서 빈 리스트에 저장 ex) F + 5 = 'F5'로 저장 
    if sublist and sublist[0][0] == '선로증설함':
        F_extracted.append(f'F{sublist[0][2]}')

print(F_extracted)
     
def find_position(jh, F_extracted, target):  #선로증설 연계 피더 좌표를 jh배열에서 찾아줌 
    for sublist in jh:
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

sub_F_positions = [find_position(jh, F_extracted, target) for target in F_extracted]

y_sub_F = [position[0] for position in sub_F_positions]   #각각 놔눠서 저장 
x_sub_F = [position[1] for position in sub_F_positions]   #각각 나눠서 저장 

print(y_sub_F) #y_sub_F[i]
print(x_sub_F) #x_sub_F[i]


fig, ax = plt.subplots(1,1)

# x 축의 범위를 0에서 까지로 지정 #행, 열 값을 받아와서 설정 
plt.xlim(-1, 30)
# y 축의 범위를 0에서 까지로 지정
plt.ylim(-1, 30)
# x 축의 눈금 단위 나타내지 x
plt.xticks([])
# y 축의 눈금 단위 나타내지 x 
plt.yticks([])
# x축과 y축 뒤집기
plt.gca().invert_yaxis()
# x축 위치 바꾸기
ax = plt.gca() # 현재 그래프의 축 객체 가져오기
ax.xaxis.set_ticks_position('top') # x축 위치를 위쪽으로 지정

img = Image.open('./image.png') #이미지 불러오기 

z_count = 0     

# 주석을 저장할 변수
annotations = []

# hovering annotation 추가 함수
def add_hovering_annotation(event):
    if event.inaxes == ax:
        # 모든 주석을 숨김
        for annotation in annotations:
            annotation.set_visible(False)
        #차례대로 x,y 좌표 맵핑해서 주석이랑 1대1 매칭 
        for x, y, formatted_list in zip(x_coords, y_coords, formatted_lists):
            for format_index in formatted_list:
                if x-0.3 <= event.xdata <= x+0.3 and y-0.3 <= event.ydata <= y+0.3:
                    annotation = ax.annotate(f"{formatted_list}", xy=(x, y), xytext=(x+1, y-1),
                                            arrowprops=dict(color='red', arrowstyle='->'), color='red'
                                            , fontsize='7')
                    annotation.set_visible(True)  # 해당 주석을 표시
                    annotations.append(annotation)
        plt.draw()

# 이벤트 처리 함수 연결
plt.connect('motion_notify_event', add_hovering_annotation)  # 커서 가져다 대면 hovering annotation 표시


# 그래프를 숨기기 위한 함수
def hide_graph(lines):
    for line in lines:
        line.set_visible(False)

# 그래프를 표시하는 함수
def show_graph(lines):
    for line in lines:
        line.set_visible(True)


# 그래프 그리기
lines_to_hide = []  # 숨길 선들을 저장하는 리스트

for i in range(len(x_sub_F)):     # F랑 Z 좌표 비교해서 ㄴ ㄱ ┌  ┛ 4가지 모양 선로 증설
    if   x_Z_trouble[i] <= x_sub_F[i] and y_Z_trouble[i] >= y_sub_F[i]:  #Z랑 F의 x, y 좌표를 비교해가지고 적절한 선로 모양으로 증설 
                line1 = plt.vlines(x_Z_trouble[i],y_sub_F[i], y_Z_trouble[i], color='red', linestyles='solid', linewidth=0.5)
                line2 = plt.hlines(y_sub_F[i], x_Z_trouble[i], x_sub_F[i], color='red', linestyles='solid', linewidth=0.5)
                lines_to_hide.extend([line1, line2])

    elif x_Z_trouble[i] <= x_sub_F[i] and y_Z_trouble[i] <= y_sub_F[i]:
                line1 = plt.hlines(y_Z_trouble[i], x_Z_trouble[i], (x_sub_F[i]+x_Z_trouble[i])/2, color='red', linestyles='solid', linewidth=0.5)
                line2 = plt.vlines((x_sub_F[i]+x_Z_trouble[i])/2, y_Z_trouble[i], y_sub_F[i], color='red', linestyles='solid', linewidth=0.5)
                line3 = plt.hlines(y_sub_F[i], (x_sub_F[i]+x_Z_trouble[i])/2, x_sub_F[i], color='red', linestyles='solid', linewidth=0.5)
                lines_to_hide.extend([line1, line2, line3])

    elif x_Z_trouble[i] >= x_sub_F[i] and y_Z_trouble[i] >= y_sub_F[i]:
                line1 = plt.hlines(y_Z_trouble[i], x_sub_F[i], x_Z_trouble[i], color='red', linestyles='solid', linewidth=0.5)
                line2 = plt.vlines(x_sub_F[i], y_sub_F[i], y_Z_trouble[i], color='red', linestyles='solid', linewidth=0.5)
                lines_to_hide.extend([line1, line2])

    elif x_Z_trouble[i] >= x_sub_F[i] and y_Z_trouble[i] <= y_sub_F[i]:
                line1 = plt.hlines(y_sub_F[i], x_sub_F[i], x_Z_trouble[i], color='red', linestyles='solid', linewidth=0.5)
                line2 = plt.vlines(x_Z_trouble[i], y_Z_trouble[i], y_sub_F[i], color='red', linestyles='solid', linewidth=0.5)
                lines_to_hide.extend([line1, line2])
             

# 그래프 숨기기
hide_graph(lines_to_hide)

# 마우스 클릭 이벤트 처리 함수
def on_mouse_click(event):
    if event.xdata is None or event.ydata is None:
        return

    # 마우스 좌표
    x = event.xdata
    y = event.ydata

    # 숨긴 선들을 다시 표시
    show_graph(lines_to_hide)

    
    for line in lines_to_hide:
        segments = line.get_segments()
        for segment in segments:
            x_values = segment[:, 0]
            y_values = segment[:, 1]
            if np.any(np.isclose(x, x_values)) and np.any(np.isclose(y, y_values)):
                line.set_visible(False)
                break
        else:
            line.set_visible(True)

    # 그래프 업데이트
    plt.draw()


# 마우스 버튼 뗄 때 선을 숨김
def on_mouse_release(event):
    hide_graph(lines_to_hide)
    plt.draw()

# 마우스 버튼 뗄 때 이벤트 연결 -> 버튼을 꾹 누르고 있다가 떼면 즉시 선이 사라짐 
fig = plt.gcf()
fig.canvas.mpl_connect('button_release_event', on_mouse_release)

# 마우스 클릭 이벤트 연결 -> 버튼을 꾹 누르고 있으면 선이 표시 
fig.canvas.mpl_connect('button_press_event', on_mouse_click) 

#jh리스트 읽어서 계통도 표시하기 
for i in range(len(jh)): #jh 리스트 행 길이만큼 반복 
        for j in range(len(jh[0])): #jh 리스트 열 길이만큼 반복 
                

                if jh[i][j][2] == mf : #메인피더 생성 
                        rect = plt.Rectangle((j-0.3,i-0.2), 0.5, 0.5, facecolor='none', edgecolor='black', linewidth=0.5)
                        ax.add_patch(rect)
                        ax.text(j-0.75, i+0.3, 'F', fontsize='7', color='black', alpha=1)
                        

                elif jh[i][j][2] == fd : #연계피더 생성 
                        rect = plt.Rectangle((j-0.25,i-0.2), 0.5, 0.5, facecolor='none', edgecolor='black', linewidth=0.5)
                        ax.add_patch(rect)
                        ax.text(j+0.4, i+0.3, jh[i][j][4], fontsize='7', color='black', alpha=1)
                        

                elif jh[i][j][2] == frk1 :   #분기점(ㅗ)
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.4,i+0.9, jh[i][j][4], fontsize='7', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.1*count_list[z_count-1]) #개수에 따라서 투명도 변경 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')

                elif jh[i][j][2] == frk2 :   #분기점(ㅜ)      
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.4,i-0.2, jh[i][j][4], fontsize='7', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.1*count_list[z_count-1]) 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == frk3 :    #분기점(십자모양)  
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='7', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.1*count_list[z_count-1]) 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == frk4 :    #분기점(┘)
                        plt.hlines(i,j-0.6, j, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='7', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.1*count_list[z_count-1]) 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == frk5 :    #분기점(┐)
                        plt.hlines(i,j-0.6, j, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='7', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.1*count_list[z_count-1]) 
                       
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == hline : #수평 직선 생성
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.9, jh[i][j][4], fontsize='7', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.1*count_list[z_count-1]) 
    

                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   
                                        

                elif jh[i][j][2] == vline : #수직 직선 생성 
                        plt.vlines(j, i-0.6, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:
                                ax.text(j,i,'')
                        else:    
                                ax.text(j+0.1,i+0.3, jh[i][j][4], fontsize='7', color='black', alpha=1.0)
                                z_count +=1 
                                 
                                if count_list[z_count-1]>=1:
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha= 0.1*count_list[z_count-1]) 
                                                                                                
                                else :  
                                    ax.text(j,i,'')
                                      
                                       
                elif jh[i][j][2] == sw :    #개폐기 생성 
                        ax.add_artist(plt.Circle((j, i), 0.3, alpha=0.5, facecolor='none', edgecolor='black'))
                                

#spines 사용해서 좌표축이랑 좌표 눈금 모두 숨기기
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.tick_params(labelbottom=False, labelleft=False)
plt.tick_params(labeltop=False, labelright=False)

#그래프 띄우기 
plt.show() 
