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

for j in range(1, 7):        #Z1 ... Zn의 모든 고장 구간별 고복지 리스트 
    globals()["result_list_" + str(j)] = [ZRI_list[i][j-1] for i in range(len(ZRI_list))]

count_list = []              #Z1 ....Zn의 모든 고장 구간별 고복지 음수 개수 리스트 
for j in range(1, 7):
    result_list = globals()["result_list_" + str(j)]
    count = sum(1 for sublist in result_list for x in sublist if x and x < 0)
    count_list.append(count)

result_lists = []            
for j in range(1, 7):
    result_lists.append(globals()["result_list_" + str(j)])

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



def format_indices_lists(indices_lists):       #고장 원인 부분 숫자에 Z붙여서 다시 리스트에 저장 
    formatted_lists = []
    for indices in indices_lists:
        formatted_indices = [f'(Z{index})' for index in indices]
        formatted_lists.append(formatted_indices)
    return formatted_lists

# ...

# result_lists에서 negative_indices_lists 생성

# negative_indices_lists를 Z 형식으로 변환
formatted_lists = format_indices_lists(negative_indices_lists)
print(formatted_lists)


def find_position(jh, Z, target):      #Z1, Z2, Z3 ...Zn의 좌표값을 찾아줌 
    for sublist in jh:
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

positions = [find_position(jh, Z, target) for target in Z]


def find_position(jh, SF, target):      #F1, F2.....Fn의 좌표값을 찾아줌 
    for sublist in jh:
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

F_positions = [find_position(jh, SF, target) for target in SF]

def find_position(jh, formatted_Z_trouble, target):      #Z1, Z2, Z3 ...Zn의 좌표값을 찾아줌 
    for sublist in jh:
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

formatted_Z_trouble_positions = [find_position(jh, formatted_Z_trouble, target) for target in formatted_Z_trouble]

print(formatted_Z_trouble_positions)


y_coords = [position[0] for position in positions]    #Z의 x좌표값 ->좌표축으로 들어갈 때는 이게 y
x_coords = [position[1] for position in positions]    #Z의 y좌표값 ->좌표축으로 들어갈 때는 이게 x 


# y_F = [position[0] for position in F_positions]    #F의 x좌표값 ->좌표축으로 들어갈 때는 이게 y
# x_F = [position[1] for position in F_positions]    #F의 y좌표값 ->좌표축으로 들어갈 때는 이게 x 

# print('y=',y_F)
# print('x=',x_F)

y_F = [7, 0]    #일단 임의로 설정... 나중에 받아올 때는 위에 꺼로  지금은 일단 임시 
x_F = [12, 7]

y_Z_trouble = [position[0] for position in formatted_Z_trouble_positions]    #복구 불가 지점의 Z 좌표값 
x_Z_trouble = [position[1] for position in formatted_Z_trouble_positions]    

print('y=',y_Z_trouble)
print('x=',x_Z_trouble)

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

        for x, y, formatted_list in zip(x_coords, y_coords, formatted_lists):
            for format_index in formatted_list:
                if x-0.3 <= event.xdata <= x+0.3 and y-0.3 <= event.ydata <= y+0.3:
                    annotation = ax.annotate(f"{formatted_list}", xy=(x, y), xytext=(x+3, y-3),
                                            arrowprops=dict(color='red', arrowstyle='->'), color='red')
                    annotation.set_visible(True)  # 해당 주석을 표시
                    annotations.append(annotation)
        plt.draw()

# 이벤트 처리 함수 연결
plt.connect('motion_notify_event', add_hovering_annotation)  # 커서 가져다 대면 hovering annotation 표시

for i in range(2):     #F랑 Z 좌표 비교해서 ㄴ ㄱ ┌ ┛ 4가지 모양 
    if x_Z_trouble[i] <= x_F[i] and y_Z_trouble[i] >= y_F[i]:
        plt.vlines(x_Z_trouble[i],y_F[i], y_Z_trouble[i], color='red', linestyles='solid', linewidth=0.5)
        plt.hlines(y_F[i], x_Z_trouble[i], x_F[i], color='red', linestyles='solid', linewidth=0.5)

    elif x_Z_trouble[i] <= x_F[i] and y_Z_trouble[i] <= y_F[i]:
        plt.hlines(y_Z_trouble[i], x_Z_trouble[i], x_F[i], color='red', linestyles='solid', linewidth=0.5)
        plt.vlines(x_F[i], y_Z_trouble[i], y_F[i], color='red', linestyles='solid', linewidth=0.5)

    elif x_Z_trouble[i] >= x_F[i] and y_Z_trouble[i] >= y_F[i]:
        plt.hlines(y_Z_trouble, x_F[i], x_Z_trouble, color='red', linestyles='solid', linewidth=0.5)
        plt.vlines(x_F, y_F, y_Z_trouble, color='red', linestyles='solid', linewidth=0.5)
        
    elif x_Z_trouble[i] >= x_F[i] and y_Z_trouble[i] <= y_F[i]:
        plt.hlines(y_F, x_F[i], x_Z_trouble, color='red', linestyles='solid', linewidth=0.5)
        plt.vlines(x_Z_trouble, y_Z_trouble, y_F, color='red', linestyles='solid', linewidth=0.5)    





for i in range(8):
        for j in range(13):
                

                if jh[i][j][2] == mf : #메인피더 생성 
                        rect = plt.Rectangle((j-0.2,i-0.2), 0.5, 0.5, facecolor='none', edgecolor='black', linewidth=0.5)
                        ax.add_patch(rect)
                        ax.text(j-0.6, i+0.3, 'F', fontsize='10', color='black', alpha=1)
                        

                elif jh[i][j][2] == fd : #연계피더 생성 
                        rect = plt.Rectangle((j-0.25,i-0.2), 0.5, 0.5, facecolor='none', edgecolor='black', linewidth=0.5)
                        ax.add_patch(rect)
                        ax.text(j+0.3, i+0.25, jh[i][j][4], fontsize='10', color='black', alpha=1)
                        

                elif jh[i][j][2] == frk1 :   #분기점(ㅗ)
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.2*count_list[z_count-1]) #개수에 따라서 투명도 변경 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')

                elif jh[i][j][2] == frk2 :   #분기점(ㅜ)      
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.2*count_list[z_count-1]) 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == frk3 :    #분기점(십자모양)  
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.2*count_list[z_count-1]) 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == frk4 :    #분기점(┘)
                        plt.hlines(i,j-0.6, j, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i-0.6, i, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.2*count_list[z_count-1]) 
                                else :                      #아닌 경우에는 표시하지x 
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == frk5 :    #분기점(┐)
                        plt.hlines(i,j-0.6, j, color='black',linestyles='solid', linewidth=0.5 )
                        plt.vlines(j, i, i+0.6, color='black', linestyles='solid', linewidth=0.5)
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.2*count_list[z_count-1]) 
                       
                                    ax.text(j,i,'')   

                elif jh[i][j][2] == hline : #수평 직선 생성
                        plt.hlines(i,j-0.6, j+0.6, color='black',linestyles='solid', linewidth=0.5 )
                        
                        if jh[i][j][4]==0:  #Z1, Z2 이런 명칭이 할당되지 않을 때는 공백 처리 
                                ax.text(j,i,'')
                        else:               #Z1, Z2 이런 명칭 할당된 거 읽어와서 표시하기 
                                ax.text(j-0.3,i+0.7, jh[i][j][4], fontsize='9', color='black', alpha=1.0)
                                z_count +=1 #Z1, Z2 이런 식으로 나올 때마다 숫자 1씩 상승 => 고복지 음수 개수 리스트에서 위치 찾을 때 필요 
                                

                                if count_list[z_count-1]>=1: #고복지 음수 개수가 1개 이상일 때, warning 표시 
                                    extent = (j-0.3, j+0.3, i-0.3, i+0.3) 
                                    plt.imshow(img, extent=extent, alpha=0.2*count_list[z_count-1]) 
    

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
                                    plt.imshow(img, extent=extent, alpha= 0.2*count_list[z_count-1]) 
                                    
                                    #annotation = ax.annotate(f"'Z{negative_indices_lists[z_count-1][0]}'", xy=(j, i), xytext=(j+3, i-6),
                                    #            arrowprops=dict(color='red', arrowstyle='->'), color='red')
                                    
                                 
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