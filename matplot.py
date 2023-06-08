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
ZZ = []
FRK = []

for i in range(1,n1+1):
    SF.append(F(i))

for i in range(1, n2+1):
    ZZ.append(Load(i))


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
            jh[i][j][4] = ZZ[b]                                                                                                                                                             # 부하일때 Z1, Z2,,, 태그 할당
            b += 1

for i in range(23):
    for j in range(21):
        if jh[i][j][2] == frk1 or jh[i][j][2] == frk2:  # 종류가 분기점이면
            FRK.append(jh[i][j][4])                                   # 분기점 리스트에 추가한다 # 근데 이거 이제 필요없잖아

for i in range(23):
    for j in range(21):
        if jh[i][j][2] == mf:
            jh[i][j][4] = "F"




sum = 0
FP = 0
FRK = 0


Z = [100,200,300,400,500,600,700,100,200,300,400,500,600,700,100,200,300,400,500,600,700]
del sum
FTL = [14000,10000,9000,8000,7000] ### F1 말단이라 여유용량 0
FM = 14000


for i in range(1, len(Z)+1): 
    globals()["Z{}".format(i)]=Z[i-1]
   
for i in range(1,len(FTL)+1):
    globals()["FM{}".format(i)]=FM

for i in range(1,len(FTL)+1):
    globals()["FTL{}".format(i)]=FTL[i-1]

for i in range(1,len(FTL)+1):
    globals()["F{}".format(i)]=FM-FTL[i-1]
    



#직선경로. 일반화가 필요없음
L = ["Z6","Z7","Z8","Z9","Z10","Z11","Z12","Z13"] ##새로 추가함. 메인피더에 직선으로 달린 부하들
L0 = ["L1","L2","L3","L4"] ##L0로 수정함
L1 = ["F1","Z1","Z2", "Z3","Z5", "Z12","Z11","Z10","Z9","Z8","Z7","Z6","F"]  
L2 = ["F2","Z4","Z10", "Z9","Z8","Z7","Z6","F"]   
L3 = ["F3","Z13", "Z12","Z11","Z10","Z9","Z8","Z7","Z6","F"] 
L4 = ["F4","Z18","Z16","Z14", "Z8","Z7","Z6","F"]     
L5 = ["F5","Z21", "Z20","Z19","Z17", "Z15", "Z13","Z12","Z11","Z10","Z9","Z8","Z7","Z6","F"]  




dml = ['dml1', 'dml2','dml4', 'dml5']

## 직선경로부하로 인한 오류에 쓰임. 굵은가지랑 가까운 쪽부터 부하값 써야함. 반대로 안되게 주의!!!
dml1 = ["Z5","Z3","Z2","Z1"]
dml2 = ['Z4']  
dml4 = ['Z14', 'Z16', 'Z18']  
dml5 = ['Z15', 'Z17', 'Z19','Z20','Z21']  





#Main피더
MP = "F" 
#연계피더
SP = ["F1","F2","F3","F4","F5"] 
#분기점
FRK = [] 
#고장점
FP

# 빈 리스트 생성. 리스트는 Z1~Z6 6개, 6*6 리스트 생성
ZRI_list = []
ZRI_list2 = []

for r in range(len(Z)):
    line = []
    for s in range( len(Z)):
        line.append([])
    ZRI_list.append(line)
    ZRI_list2.append(line)

new_L = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))]



#print(*ZRI_list, sep='\n')
# 빈 리스트 생성, F1~F8





########################################################################
for b in range(1, len(Z)+1):   ###고장점 Z1~Z6 6개 지점
    FP = "Z{}".format(b) 


    for f in range(1,len(SP)+1) :  # 연계피더 개수만큼 구간복구지수를 구해야 함
    
    
        if (FP in globals()["L" + str(f)] )== True :                       ##L1(연계피더 라인)에 고장점이 있으면
            number = globals()["L" + str(f)].index(FP) - globals()["L" + str(f)].index("F" + str(f))     ## 피더랑 고장점 위치 차이만큼
            sum = globals()["F" + str(f)]                                   ## F1(연계피더)용량에서
            for l in range(1,number):      
                sum = sum - globals()[globals()["L" + str(f)][l]]           ## F1(연계피더)부터 고장점 앞까지(고장점 포함X)의 부하량을 차례로 빼준다.
                globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])]=sum  ## 값 입력        
                

                
            
                col = globals()["L" + str(f)] [l]
                new_col = col.replace('Z','')
                ZRI_list[b-1][int(new_col)-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])] ) ##리스트에 값 추가
                                                                    ### Z4라고 하면 int(new_col)-1 = 3이 되어 네번째 리스트에 들어감
                new_L[b-1][f-1][int(new_col)-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L"+str(f)] [l])])    

        else :   
           pass
        
        


                              
                ###L1,L2,L3... 값 = globals()["L" + str(f)]  
                ###F1,F2,F3... 값 = globals()["F" + str(f)] 
                ###F1,F2,F3... 문자 = "F" + str(f)  

################################# 최대값으로 ZRI 결정 ################################################


for n in range(len(ZRI_list)):
  for m in range(len(ZRI_list[n])):
    if ZRI_list[n][m]:
      ZRI_list[n][m] = [max(ZRI_list[n][m])]
      ZRI_list2[n][m] = [max(ZRI_list[n][m])]
    else:
      ZRI_list[n][m] = []
      ZRI_list2[n][m] = []



#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#print(*ZRI_list, sep='\n')

#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#print(*new_L, sep='\n')

mg = [[[] for x in range(len(SP))] for y in range(len(Z))]


for e in range(1, len(Z)+1):
   for k in range(1, len(SP)+1):
      for g in range(1, len(Z)+1):
         for h in new_L[e-1][k-1][g-1]:
            if h in ZRI_list[e-1][g-1]:
                mg[e-1][k-1].append(h)       ### 피더K의 여유용량을 mg리스트에 넣음 
            else :
               pass

for len1 in range(1,len(mg)+1):      ### Z1~Z12에서 고장났을때가 행
  for len2 in range(1, len(mg[len1-1])+1):      ### Z1~Z12의 고복지가 열
    if mg[len1-1][len2-1]: 
      mg[len1-1][len2-1] = [min(mg[len1-1][len2-1])]     ### 연계되는 피더의 여유용량
    else:
      mg[len1-1][len2-1] = [globals()['F' + str(len2)]]       ### 연계안되는 피더의 여유용량


FRK_list= []
for N in range( len(SP) ):
        FRK_list.append([])

for i in range(1 ,len(SP)+1) :
    intersection = [x for x in globals()['L' + str(i)] if x in L]  # L이랑 L1~L8 안의 값을 차례대로 비교를 할껀데, 가장 먼저 겹치는 게 F1~F8의 분기점임!!!! 
    FRK_list[i-1].append(intersection[0]) ###리스트에 값 입력

###FRK_list 출력. 연계피더의 분기점 리스트 생성
df = pd.DataFrame({'각 연계피더의 분기점': FRK_list}, index=['F1', 'F2', 'F3', 'F4','F5'])
#print(df)




#####각 분기점의 부하를 감당하는 피더를 찾는다 
#-----------> ZRI_list[각 고장점][분기점]에서 분기점의 고장복구지수를 찾고,
# ----------->  new_L[각 고장점][연계피더][분기점]에서 어떤 피더가 감당하는지 찾음  
# -----------> FRK_list[연계피더][0]는 연계피더의 분기점
FRK_feeder_list=  [[[] for x in range(len(SP))] for y in range(len(Z))]

for i in range(len(Z)) :   # 각 고장점에 대해서 검사
    for l in range(len(SP)) :  # 각 연계피더의 분기점에 대해서 검사. 연계피더 F1의 분기점,F2의 분기점.... F8까지 검사
        for k in (   (int(FRK_list[l][0].replace('Z','')))-1,  (int(FRK_list[l][0].replace('Z','')))-1 ) : # 분기점 위치
            for j in range(len(SP)) :       # 어떤 연계피더가 공급하는지 모두 검사
                    if ZRI_list[i][k] == new_L[i][j][k] :  
                         if ZRI_list[i][k] != []:
                                FRK_feeder_list[i][l] = "F"+ str(j+1)  ##리스트에 입력
        
### FRK_feeder_list 출력. 각 고장시에 연계피더의 분기점부하를 감당하고 있는 연계피더






FRK_fdm_list=  [[[] for x in range(len(SP))] for y in range(len(Z))]

for i in range(len(Z)) :
    for j in range(len(SP)) :
        if FRK_feeder_list[i][j] != []:
            FRK_fdm_list[i][j] =   mg[i][int(FRK_feeder_list[i][j].replace('F',''))-1]

### FRK_fdm_list 출력. 분기점을 감당하는 연계피더의 마진용량 리스트 생성




# ----------> 여유용량에서 부하 빼서 ZRI_list 다시 반환



for k in range (len(dml)) :  # 굵은가지에서 나오는 잔가지 갯수만큼
    for j in range (len(Z)) :  ## 고장점이 1부터 12까지
        for i in range (len(globals()[dml[k]])) : # dml8의 부하 갯수 3개
            if ZRI_list[j][int(globals()[dml[k]][i].replace('Z',''))-1 ] != [] : # 값이 존재할 때 
               if FRK_fdm_list[j][int(dml[k].replace('dml',''))-1] != [] : ## 값이 존재할 때. int(dml[k].replace('dml',''))-1 ## dml8이면 7
                if ZRI_list[j][int(globals()[dml[k]][i].replace('Z',''))-1][0] < 0 : #음수가 나오면
                    if i  == 0 :
                        ZRI_list[j][int(globals()[dml[k]][i].replace('Z',''))-1][0]  = FRK_fdm_list[j][int(dml[k].replace('dml',''))-1][0] - globals()[globals()[dml[k]][i]] # F8분기점의 여유용량에서 'Z10'빼고, 거기에서 Z11빼고, 거기에서 Z12빼고..
                    if i  >= 1 :
                        if  ZRI_list[j][int(globals()[dml[k]][i-1].replace('Z',''))-1 ][0]  - globals()[globals()[dml[k]][i]] >= 0 : 
                            ZRI_list[j][int(globals()[dml[k]][i].replace('Z',''))-1 ][0]  = ZRI_list[j][int(globals()[dml[k]][i-1].replace('Z',''))-1 ][0]  - globals()[globals()[dml[k]][i]]





#####################################################선로증설

mg = [[[] for x in range(len(SP))] for y in range(len(Z))]
flow = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))]
# mg = []

for e in range(1, len(Z)+1):
   for k in range(1, len(SP)+1):
      for g in range(1, len(Z)+1):
         for h in new_L[e-1][k-1][g-1]:
            if h in ZRI_list[e-1][g-1]:
                mg[e-1][k-1].append(h)
                flow[e-1][k-1][g-1].append(h)
            else :
               pass

for len1 in range(1,len(mg)+1):
  for len2 in range(1, len(mg[len1-1])+1):
    if mg[len1-1][len2-1]:
      mg[len1-1][len2-1] = [min(mg[len1-1][len2-1])]
    else:
      mg[len1-1][len2-1] = [globals()['F' + str(len2)]]

UR_ZRI = [] # 복구불가능지점의 ZRI의 값
UR_L = [[ [] for col2 in range(len(Z))] for row2 in range(len(Z))] # 복구불가능지점 부하량

new_ZRI = 0 # 복구불가능지점의 새로운 ZRI 값
new_ZRI_list = [[[ [] for col3 in range(len(Z))] for row3 in range(len(SP))] for depth3 in range(len(Z))] # 복구불가능지점에 대한 각 고장점과 연계피더에 대한 ZRI 값이 담긴 list 
new_ZRI_UR_L_list = [[[ [] for col4 in range(len(Z))] for row4 in range(len(SP))] for depth4 in range(len(Z))] 
new_ZRI_list2 = [[[ [] for col5 in range(len(Z))] for row5 in range(len(SP))] for depth5 in range(len(Z))]

for p in range(1, len(Z)+1):   
  for q in range(1, len(Z)+1):
     if ZRI_list[p-1][q-1]:
        if ZRI_list[p-1][q-1] < [0]:
          UR_ZRI.append((p, q, ZRI_list[p-1][q-1])) # ZRI_list에서 음수인 값을 찾아서 UR_ZRI 리스트에 인덱스값과 해당 음수값을 저장
          UR_L[p-1][q-1].append(globals()['Z'+str(q)]) # 복구불가능지점의 부하량을 고장점별로 UR_L 리스트에 저장
        else:
          pass
     else:
        pass
     

     
# mg_value  연계피더 값
# UR_L_value 복구불가능지점 부하량


for b1 in range(1, len(Z)+1):  #고장점 1~12에서 고장날 때
    for f1 in range(1,len(SP)+1) : 
      mg_value = mg[b1-1][f1-1] #연계피더 1~8 값 중 하나 선택
      for l1 in range(1,len(Z)+1):
        UR_L_value = UR_L[b1-1][l1-1] #복구불가능지점 부하량 리스트에서 부하량 하나 선택
        if UR_L[b1-1][l1-1]: #만약 복구불가능지점이라면 (리스트에 값이 있다면)
          new_ZRI = mg_value[0] - UR_L_value[0] # 앞에서 선택한 mg_value 값에서 UR_L_value 값 빼기 (연계피더 - 복구불가능지점 부하량)
          new_ZRI_list[b1-1][f1-1][l1-1].append(new_ZRI) # 이것을 new_ZRI_list 리스트에 저장
          new_ZRI_list2[b1-1][f1-1][l1-1].append(new_ZRI)
          new_ZRI_UR_L_list[b1-1][f1-1][l1-1].append(new_ZRI) # 복구 불가능지점의 ZRI만 따로 볼려고 만듦
        else:          # 만약 복구불가능지점이 아니라면 원래 ZRI 값을 리스트에 저장
          if ZRI_list[b1-1][l1-1] == []: 
            pass
          else:
            new_ZRI_list[b1-1][f1-1][l1-1].append(ZRI_list[b1-1][l1-1][0])      
            new_ZRI_list2[b1-1][f1-1][l1-1].append(ZRI_list[b1-1][l1-1][0])   


""" print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*mg, sep='\n')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*UR_L, sep='\n')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

for i0 in range(len(new_ZRI_list)): #3차원 리스트인 new_ZRI_list 줄바꿔서 출력,,
   for j0 in range(len(new_ZRI_list[i0])):
      print(new_ZRI_list[i0][j0])
   print() 

print("---------------------")

for i0 in range(len(new_ZRI_list2)): #3차원 리스트인 new_ZRI_list 줄바꿔서 출력,,
   for j0 in range(len(new_ZRI_list2[i0])):
      print(new_ZRI_list2[i0][j0])
   print()       """




##############################################정규화(f3)#############################

for p in range(1, len(Z)+1):   
  for q in range(1,len(SP)+1) : 
      new_ZRI_list2[p-1][q-1] = [[0]  if x==[] else x for x in new_ZRI_list2[p-1][q-1]] # min max 값 찾기 위해 []인 값을 모두 [0]으로 만들어 new_ZRI_list2에 넣기
      ZRI_list2[p-1] = [[0]  if x==[] else x for x in ZRI_list2[p-1]]  #min max 값 찾기 위해 []인 값을 모두 [0]으로 만들어 ZRI_list2에저장                                                                 


min_val = min([min([min(i) for i in j]) for j in new_ZRI_list2])[0] #new_ZRI_list2에서 min 값 찾기
max_val = max([max([max(i) for i in j]) for j in new_ZRI_list2])[0] #new_ZRI_list2에서 max 값 찾기
norm_new_ZRI_list = [[[ [] for col6 in range(len(Z))] for row6 in range(len(SP))] for depth6 in range(len(Z))] #min max 정규화 리스트

min_val1 = min([min(x) for x in ZRI_list2])[0] #ZRI_list2에서 min 값 찾기
max_val1 = max([max(x) for x in ZRI_list2])[0] #ZRI_list2에서 max 값 찾기
norm_ZRI_list = [[ [] for col7 in range(len(Z))] for row7 in range(len(Z))] # min max 정규화 리스트


for p1 in range(1, len(Z)+1):  
  for q1 in range(1, len(SP)+1): 
    for r1 in range(1, len(Z)+1):
      if new_ZRI_list[p1-1][q1-1][r1-1] == []:  #만약 new_ZRI_list 값이 []이면 계산 안함
          pass
      else:
          x = new_ZRI_list[p1-1][q1-1][r1-1][0]    #new_ZRI_list 값이 있으면 정규화 함
          norm_new_ZRI_list[p1-1][q1-1][r1-1].append((x - min_val) / (max_val - min_val)) #계산된 정규화 값 norm_new_ZRI_list에 넣기

for p2 in range(1, len(Z)+1):  
    for r2 in range(1, len(Z)+1):
      if ZRI_list[p2-1][r2-1] == []:  #만약 ZRI_list 값이 []이면 계산 안함
          pass
      else:
          x1 = ZRI_list[p2-1][r2-1][0]    #ZRI_list 값이 있으면 정규화 함
          norm_ZRI_list[p2-1][r2-1].append((x1 - min_val1) / (max_val1 - min_val1)) #계산된 정규화 값 norm_ZRI_list에 넣기





#########결과값 출력############
""" print("--------------------")
print(*ZRI_list, sep='\n') #고복지 값

print("--------------------")
print(*norm_ZRI_list, sep='\n') #고복지 정규화 값

print("--------------------")
for i0 in range(len(new_ZRI_list)): #3차원 리스트인 new_ZRI_list 줄바꿔서 출력
   for j0 in range(len(new_ZRI_list[i0])):
      print(new_ZRI_list[i0][j0])
   print()


print("--------------------")
for i0 in range(len(norm_new_ZRI_list)): #3차원 리스트인 norm_new_ZRI_list 줄바꿔서 출력 (정규화)
   for j0 in range(len(norm_new_ZRI_list[i0])):
      print(norm_new_ZRI_list[i0][j0])
   print()  """

################################# 목적함수F ####################################

#####고장취약지점에서 어떤 고장점에서 고장이 났을 때 ZRI가 더 적은지##### 그때 고장지점이랑 고장취약지점 구함

UR_list = [] #고장취약지점리스트 (중복있음)
UR = [] #고장취약지점 (중복없음)

UR_ZRI_min_list = [[[] for x in range(len(Z))] for y in range(len(Z))] # 고장이 났을 때 고장취약구간의 모든 ZRI 나타냄 (0 포함 : min 구하기 위해서)
UR_ZRI_min = [] # 고장취약구간의 ZRI 중 가장 작은 값 
UR_ZRI_min_inf_list = []


for p in range(1,len(UR_ZRI)+1):
    UR_list.append(UR_ZRI[p-1][1])
    UR = list(set(UR_list)) 

for r in range (1, len(Z)+1):
    for q in range(1, len(UR)+1):
        UR_ZRI_min_list[UR[q-1]-1][r-1].append(ZRI_list2[r-1][UR[q-1]-1])
        if UR_ZRI_min_list[UR[q-1]-1][r-1] == []:
           pass
        else:
           UR_ZRI_min = [min(row) for row in UR_ZRI_min_list] 

for r in range (1, len(Z)+1):
    for q in range(1, len(UR)+1):
        if UR_ZRI_min[UR[q-1]-1][0] == UR_ZRI_min_list[UR[q-1]-1][r-1][0]:
           UR_ZRI_min_inf_list.append((r, UR[q-1])) #고장점, 취약구간 ##[((2, 3), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7))]
        else:
           pass

UR_ZRI_min_inf = []
for item in UR_ZRI_min_inf_list:
    if item[1] not in [x[1] for x in UR_ZRI_min_inf]:
        UR_ZRI_min_inf.append(item) #(고장점, 취약구간) ##[(2,3), (2,7)] 로 같은 ZRI(최소 ZRI)를 가지는 취약구간 제거

#################################목적함수######################################


######### 선로증설X ##########
f1_1 = 0
f2_1 = 0
w1 = 0.3
w2 = 0.5
w3 = 0.9

F1 = [[] for x in range(len(Z))]  #선로증설안했을때목적함수

for b in range(1, len(UR_ZRI_min_inf)+1):
    f3_1 = norm_ZRI_list[UR_ZRI_min_inf[b-1][0]-1][UR_ZRI_min_inf[b-1][1]-1][0]
    F1[UR_ZRI_min_inf[b-1][1]-1].append(-(f1_1*w1) -(f2_1*w2) +(f3_1*w3))



######## 선로증설O ###############
f3_2_list = [[[] for x in range(len(Z))] for y in range(len(Z))]
f3_2_list2 = [[[] for x in range(len(Z))] for y in range(len(Z))]
f3_2_list3 = [[[] for x in range(len(Z))] for y in range(len(Z))]

for d in range(1, len(UR_ZRI_min_inf)+1):
    for c in range(1, len(SP)+1):
        f3_2_list[UR_ZRI_min_inf[d-1][0]-1][UR_ZRI_min_inf[d-1][1]-1].append(norm_new_ZRI_list[UR_ZRI_min_inf[d-1][0]-1][c-1][UR_ZRI_min_inf[d-1][1]-1][0])

for d in range(1, len(UR_ZRI_min_inf_list)+1):
    for c in range(1, len(SP)+1):
        f3_2_list2[UR_ZRI_min_inf_list[d-1][0]-1][UR_ZRI_min_inf_list[d-1][1]-1].append((c,norm_new_ZRI_list[UR_ZRI_min_inf_list[d-1][0]-1][c-1][UR_ZRI_min_inf_list[d-1][1]-1][0]))
        f3_2_list3[UR_ZRI_min_inf_list[d-1][0]-1][UR_ZRI_min_inf_list[d-1][1]-1].append(norm_new_ZRI_list[UR_ZRI_min_inf_list[d-1][0]-1][c-1][UR_ZRI_min_inf_list[d-1][1]-1][0])

for n in range(len(f3_2_list)):
  for m in range(len(f3_2_list[n])):
    if f3_2_list[n][m]:
      f3_2_list[n][m] = [max(f3_2_list[n][m])]
    else:
      f3_2_list[n][m] = []

for n in range(1, len(Z)+1):
  for m in range(1, len(Z)+1):
      if f3_2_list3[n-1][m-1]:
        f3_2_list3[n-1][m-1] = [max(f3_2_list3[n-1][m-1])]
      else:
        f3_2_list3[n-1][m-1] = []
 

feeder_max = [[] for x in range(len(Z))]  # 선로 증설하는데 선택된 연계피더 리스트 (취약구간에 대해서)
feeder_max_inf = [[] for x in range(len(Z))] 
feeder_max_inf_2 = [[[] for x in range(len(Z))] for y in range(len(Z))] 
new_flow = [] # 선로 증설 후 각 연계피더가 담당하는 부하

for n in range(1, len(Z)+1):
  for m in range(1, len(Z)+1):
    for o in range(1, len(SP)+1):
        if f3_2_list3[n-1][m-1]:
            if f3_2_list3[n-1][m-1][0] == f3_2_list2[n-1][m-1][o-1][1]:
                feeder_max_inf_2[n-1][m-1].append((mg[n-1][o-1][0], f3_2_list2[n-1][m-1][o-1][0]))
            else:
                pass
        else:
            pass

for n in range(1, len(Z)+1):
  for m in range(1, len(Z)+1):
    for o in range(1, len(SP)+1):
        if f3_2_list[n-1][m-1]:
            if f3_2_list[n-1][m-1][0] == f3_2_list2[n-1][m-1][o-1][1]:
              feeder_max[m-1].append(f3_2_list2[n-1][m-1][o-1][0])
              feeder_max_inf[m-1].append((mg[n-1][o-1][0], f3_2_list2[n-1][m-1][o-1][0]))
            else:
               pass
        else:
            pass


new_flow = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))] # # 뉴복지에서 각 연계피더가 담당하는 부하 (고장점마다 연계피더가 담당하는 부하량)


for i in range(1, len(Z)+1):
  for j in range(1, len(SP)+1):
     for k in range(1, len(Z)+1):
          if flow[i-1][j-1][k-1] == []:
             pass
          else:
             if flow[i-1][j-1][k-1] < [0] : 
              new_flow[i-1][feeder_max_inf_2[i-1][k-1][0][1]-1][k-1].append(feeder_max_inf_2[i-1][k-1][0][0] - abs(flow[i-1][j-1][k-1][0]))
             else:
              new_flow[i-1][j-1][k-1].append(flow[i-1][j-1][k-1][0])
           

    
f1_2 = 0
f2_2 = 1
F2 = [[] for x in range(len(Z))]  #선로증설했을때목적함수


for b in range(1, len(UR_ZRI_min_inf)+1): 
        f3_2 = norm_new_ZRI_list[UR_ZRI_min_inf[b-1][0]-1][feeder_max[UR_ZRI_min_inf[b-1][1]-1][0]-1][UR_ZRI_min_inf[b-1][1]-1][0]
        F2[UR_ZRI_min_inf[b-1][1]-1].append((-f1_2*w1) -(f2_2*w2) +(f3_2*w3))


###########################최종 F 구하기####################
F = [[] for x in range(len(Z))] #최종F, 선로증설여부


for i in range (1, len(Z)+1):
      if F1[i-1] == F2[i-1]:
         pass
      else:
        if F1[i-1] > F2[i-1]:
            F[i-1].append(("선로증설안함", F1[i-1][0]))
        else:
            F[i-1].append(("선로증설함", F2[i-1][0], feeder_max[i-1][0]))




#####################################출력###############################

""" print(*ZRI_list2, sep="\n")
print("------------------")
print(*UR_ZRI_min_list, sep="\n")
print("------------------")
print(UR_ZRI_min)
print("------------------") 

print("--------------------")
for i0 in range(len(norm_new_ZRI_list)): #3차원 리스트인 norm_new_ZRI_list 줄바꿔서 출력 (정규화)
   for j0 in range(len(norm_new_ZRI_list[i0])):
      print(norm_new_ZRI_list[i0][j0])
   print() 

print("--------------------")
print(UR_ZRI_min_inf_list)
print("------------------")

print(UR_ZRI_min_inf)
print("------------------")
print(*f3_2_list,sep="\n")
print("------------------")
print(f3_2,)
print("------------------")"""

""" print(*f3_2_list, sep='\n')
print("-------------------")
print(*f3_2_list2, sep='\n')
print("-------------------")
print(*f3_2_list3, sep='\n')""" 
""" 
print(*norm_ZRI_list, sep="\n")
print("-------------------")
for i0 in range(len(norm_new_ZRI_list)): #3차원 리스트인 norm_new_ZRI_list 줄바꿔서 출력 (정규화)
   for j0 in range(len(norm_new_ZRI_list[i0])):
      print(norm_new_ZRI_list[i0][j0])
   print() 
 """

print("-------------------")
#print(feeder_max) # 선로 증설하는데 선택된 연계피더 리스트 (취약구간에 대해서) -> (연계피더)
print("-------------------") 
#print(feeder_max_inf) # 선로 증설하는데 선택된 연계피더 리스트 (취약구간에 대해서) -> (연계피더 용량, 연계피더)
print("---------------------")

""" for i0 in range(len(flow)):          # 구복지에서 각 연계피더가 담당하는 부하 (고장점마다 연계피더가 담당하는 부하량)
   for j0 in range(len(flow[i0])):
      print(flow[i0][j0])
   print()   

print("---------------------")

for i0 in range(len(new_flow)):     # 뉴복지에서 각 연계피더가 담당하는 부하 (고장점마다 연계피더가 담당하는 부하량)
   for j0 in range(len(new_flow[i0])):
      print(new_flow[i0][j0])
   print()  
 """
print("------------------------------")
#print(F1) # 선로증설안했을때 취약구간에 대한 목적함수

print("------------------------------")
#print(F2) # 선로증설했을때 취약구간에 대한 목적함수


print("------------------------------")
#print(F) # 최종 취약구간에 대한 목적함수
print("------------------------------")

print(ZRI_list)
print(Z)




for j in range(1, len(ZRI_list)+1):
    globals()["result_list_" + str(j)] = [ZRI_list[i][j-1] for i in range(len(ZRI_list))]


count_list = []  # Z1 ....Zn의 모든 고장 구간별 고복지 음수 개수 리스트
for j in range(1, len(ZRI_list) + 1):
    result_list = globals()["result_list_" + str(j)]
    count = len([x for sublist in result_list for x in sublist if isinstance(x, int) and x < 0])
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


def find_position(jh, ZZ, target):      #Z1, Z2, Z3 ...Zn의 좌표값을 찾아줌(진짜 좌표축에 넣을 때는 x,y 바꿔야됨) 
    for sublist in jh:                  #ex) [1,2]가 추출되면 사실상 좌표축에는 (2,1) 이렇게 들어가야 됨 
        for item in sublist:
            if item[4] == target:
                return item[:2]
    return None

positions = [find_position(jh, ZZ, target) for target in ZZ]

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
                line1 = plt.hlines(y_Z_trouble[i], (x_sub_F[i]+x_Z_trouble[i])/2, x_Z_trouble[i], color='red', linestyles='solid', linewidth=0.5)
                line2 = plt.vlines((x_sub_F[i]+x_Z_trouble[i])/2, y_Z_trouble[i], y_sub_F[i], color='red', linestyles='solid', linewidth=0.5)
                line3 = plt.hlines(y_sub_F[i], x_sub_F[i], (x_sub_F[i]+x_Z_trouble[i])/2, color='red', linestyles='solid', linewidth=0.5)
                lines_to_hide.extend([line1, line2, line3])
             

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
                        

                elif jh[i][j][2] == fd and jh[i][j][3] != 0: #연계피더 생성 
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