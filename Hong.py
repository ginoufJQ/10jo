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


jh =    [
        [[0,0,0,0,0], [0,1,0,0,0], [0,2,0,0,0], [0,3,0,0,0], [0,4,0,0,0], [0,5,0,0,0], [0,6,0,0,0], [0,7,fd,5500,0], [0,8,0,0,0], [0,9,0,0,0], [0,10,0,0,0], [0,11,0,0,0], [0,12,0,0,0]], 
        [[1,0,0,0,0], [1,1,0,0,0], [1,2,0,0,0], [1,3,0,0,0], [1,4,0,0,0], [1,5,0,0,0], [1,6,0,0,0], [1,7,vline,0,0], [1,8,0,0,0], [1,9,0,0,0], [1,10,0,0,0], [1,11,0,0,0], [1,12,0,0,0]], 
        [[2,0,0,0,0], [2,1,0,0,0], [2,2,0,0,0], [2,3,0,0,0], [2,4,0,0,0], [2,5,0,0,0], [2,6,0,0,0], [2,7,sw,0,0], [2,8,0,0,0], [2,9,0,0,0], [2,10,0,0,0], [2,11,0,0,0], [2,12,0,0,0]], 
        [[3,0,0,0,0], [3,1,0,0,0], [3,2,0,0,0], [3,3,0,0,0], [3,4,0,0,0], [3,5,0,0,0], [3,6,0,0,0], [3,7,vline,1500,0], [3,8,0,0,0], [3,9,0,0,0], [3,10,0,0,0], [3,11,0,0,0], [3,12,0,0,0]], 
        [[4,0,0,0,0], [4,1,0,0,0], [4,2,0,0,0], [4,3,0,0,0], [4,4,0,0,0], [4,5,0,0,0], [4,6,0,0,0], [4,7,sw,0,0], [4,8,0,0,0], [4,9,0,0,0], [4,10,0,0,0], [4,11,0,0,0], [4,12,0,0,0]], 
        [[5,0,0,0,0], [5,1,0,0,0], [5,2,0,0,0], [5,3,0,0,0], [5,4,0,0,0], [5,5,0,0,0], [5,6,0,0,0], [5,7,vline,1000,0], [5,8,0,0,0], [5,9,0,0,0], [5,10,0,0,0], [5,11,0,0,0], [5,12,0,0,0]], 
        [[6,0,0,0,0], [6,1,0,0,0], [6,2,0,0,0], [6,3,0,0,0], [6,4,0,0,0], [6,5,0,0,0], [6,6,0,0,0], [6,7,sw,0,0], [6,8,0,0,0], [6,9,0,0,0], [6,10,0,0,0], [6,11,0,0,0], [6,12,0,0,0]], 
        [[7,0,mf,14000,0], [7,1,hline,0,0], [7,2,sw,0,0], [7,3,hline,1000,0], [7,4,sw,0,0], [7,5,hline,500,0], [7,6,sw,0,0], [7,7,frk1,1000,0], [7,8,sw,0,0], [7,9,hline,500,0], [7,10,sw,0,0], [7,11,hline,0,0], [7,12,fd,4500,0]]
         ]

# 서브피더, 부하, 분기점에 대한 리스트 먼저 만들어줘야 전역변수 쓸 수 있음

# 먼저 5번째 원소 넣은다음에

# 부하, 서브피더, 분기점 리스트 만들기

n1 = na = nb = 0

for i in range(8):
    for j in range(13):
        if jh[i][j][2] == fd and jh[i][j][3] != 14000:
            n1 += 1

for i in range(8):
    for j in range(13):
        if (jh[i][j][2] == hline or jh[i][j][2] == vline) and jh[i][j][3] != 0:
            na += 1

for i in range(8):
    for j in range(13):
        if jh[i][j][2] == frk1:                     #frk1,2,3,4,5에 대해서도 넣기
            nb += 1

n2 = na + nb

# 이제 이 숫자로 리스트 폼 만들고나서 jh에 tag 할당할거임

def F(i):
    return "F"+str(i)

def Load(i):
    return "Z"+str(i)

# def jnuc(i):
#     return "FRK"+str(i)

SF = []
Z = []
FRK = []

for i in range(1,n1+1):
    SF.append(F(i))

for i in range(1, n2+1):
    Z.append(Load(i))

# for i in range(1, n3+1):          #FRK는 jh 5번째 원소에 할당한뒤에 해야할듯 할당이 먼저다!
#     FRK.append()

# print(SF, Z, FRK)


a=b=0

for i in range(8):
    for j in range(13):
        if jh[i][j][2] == fd and jh[i][j][3] != 14000:
            jh[i][j][4] = SF[a]
            a += 1

for i in range(8):
    for j in range(13):
        if ((jh[i][j][2] == hline or jh[i][j][2] == vline) and jh[i][j][3] != 0) or jh[i][j][2] == frk1:
            jh[i][j][4] = Z[b]
            b += 1

for i in range(8):
    for j in range(13):
        if jh[i][j][2] == frk1:
            FRK.append(jh[i][j][4])


# 메인피더의 x좌표, y좌표 구하기
mx=my=0     
for i in range(8):
    for j in range(13):
        if jh[i][j][2] == mf:
            my = jh[i][j][0]
            mx = jh[i][j][1]

# 연계피더 개수만큼 빈 L리스트 생성
L = []                                        # 리스트 이름을 저장할 빈 리스트

for i in range(1, n1+1):
    L_name = 'L' + str(i)                     # 리스트 이름 생성
    L.append(L_name)                          # 리스트 이름을 L 리스트에 추가
    exec("%s = []" % L_name)                  # 리스트 생성




p=1
for i in range(8):
    for j in range(13):
        if jh[i][j][2] == fd:                   # jh에서 연계피더를 찾아           
            if p == int(str(jh[i][j][4])[-1]):  # 연계피더의 번호와 p가 일치한다면?
                x_num = abs(j - mx)                  # 행방향으로 L'p'리스트에 넣어줘야할 개수
                y_num = abs(my - i)                  # 열방향으로 L'p'리스트에 넣어줘야할 개수
                for q in range(min(y_num+1, 8)):  # 행의 범위는 0부터 7까지
                        if jh[q][j][3] > 0:
                                globals()["L" + str(p)].append(jh[q][j][4])   
                for r in range(x_num+1, 0, -1):
                        if jh[my][max(r, 0)][3] > 0:  # 열의 범위는 0부터 12까지
                                globals()["L" + str(p)].append(jh[my][max(r, 0)][4]) 
p += 1

ZRI_list = [[[], [-2500], [3000], [4000], [3000], [4000]],
            [[], [], [3000], [-4000], [3000], [4000]],
            [[], [], [], [4000], [-3000], [4000]],
            [[], [], [2000], [], [3000], [4000]],
            [[], [], [3000], [-4000], [], [4000]],
            [[], [], [3000], [4000], [2000], []]]

for j in range(1, 7):
    globals()[f"result_list_{j}"] = [ZRI_list[i][j-1] for i in range(len(ZRI_list))]

count_list = []
for j in range(1, 7):
    result_list = globals()[f"result_list_{j}"]
    count = sum(1 for sublist in result_list for x in sublist if x and x < 0)
    count_list.append(count)

                 

fig, ax = plt.subplots(1,1)

# x 축의 범위를 0에서 까지로 지정 #행, 열 값을 받아와서 설정 
plt.xlim(-1, 20)
# y 축의 범위를 0에서 까지로 지정
plt.ylim(-1, 20)
# x 축의 눈금 단위 나타내지 x
plt.xticks([])
# y 축의 눈금 단위 나타내지 x 
plt.yticks([])
# x축과 y축 뒤집기
plt.gca().invert_yaxis()
# x축 위치 바꾸기
ax = plt.gca() # 현재 그래프의 축 객체 가져오기
ax.xaxis.set_ticks_position('top') # x축 위치를 위쪽으로 지정

img = Image.open('./image.png')
z_count = 0

for i in range(8):
        for j in range(13):
                

                if jh[i][j][2] == mf : #메인피더 생성 
                        rect = plt.Rectangle((j-0.2,i-0.2), 0.5, 0.5, facecolor='none', edgecolor='black', linewidth=0.5)
                        ax.add_patch(rect)
                        ax.text(j-0.6, i+0.3, 'F', fontsize='10', color='black', alpha=1)
                        

                elif jh[i][j][2] == fd : #연계피더 생성 
                        rect = plt.Rectangle((j-0.25,i-0.2), 0.5, 0.5, facecolor='none', edgecolor='black', linewidth=0.5)
                        ax.add_patch(rect)
                        ax.text(j+0.3, i+0.3, jh[i][j][4], fontsize='10', color='black', alpha=1)
                        

                elif jh[i][j][2] == frk1 :   #분기점(ㅗ)
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i, color='black', linestyles='solid', linewidth=0.5)
                        

                elif jh[i][j][2] == frk2 :   #분기점(ㅜ)      
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i, i+0.6, color='black', linestyles='solid', linewidth=0.5)

                elif jh[i][j][2] == frk3 :    #분기점(십자모양)  
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i+0.6, color='black', linestyles='solid', linewidth=0.5)

                elif jh[i][j][2] == frk4 :    #분기점(┘)
                        plt.hlines(i,j-0.6, j, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i, color='black', linestyles='solid', linewidth=0.5)

                elif jh[i][j][2] == frk5 :    #분기점(┐)
                        plt.hlines(i,j-0.6, j, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i, i+0.6, color='black', linestyles='solid', linewidth=0.5)

                elif jh[i][j][2] == hline : #수평 직선 생성
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent) 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   
                                        
                

                elif jh[i][j][2] == vline : #수직 직선 생성 
                        plt.vlines(j, i-0.6, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:
                                ax.text(j,i,'')
                        else:    
                                ax.text(j+0.1,i+0.3, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 
                                 

                                if count_list[z_count-1]>=1:
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent) 
                                else :  
                                    ax.text(j,i,'')
                                           
                        
                
                elif jh[i][j][2] == sw :    #개폐기 생성 
                        ax.add_artist(plt.Circle((j, i), 0.3, alpha=0.5, facecolor='none', edgecolor='black'))
                                
                        

#spines 숨기기
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.tick_params(labelbottom=False, labelleft=False)
plt.tick_params(labeltop=False, labelright=False)

plt.show()
