import pandas as pd
import numpy

#용량 입력
Z = [1000,
     500,
     1000,
     500,
     1000,
     1500]
FTL = [sum(Z),
       8500,
       9500]
FM = 14000

for i in range(1,7):
    globals()["Z{}".format(i)]=Z[i-1]

for i in range(1,4):
    globals()["FM{}".format(i)]=FM

for i in range(1,4):
    globals()["FTL{}".format(i)]=FTL[i-1]

for i in range(1,4):
    globals()["F{}".format(i)]=FM-FTL[i-1]

#직선경로
L = ["L1","L2","L3"]
L1 = ["F1","Z1","Z2","Z3","Z4","F3"]
L2 = ["F2","Z6","Z5","Z3"]
L3 = L2.reverse()

#Main피더
MP = "F1"

#연계피더
SP = ["F2","F3"]

#분기점
FRK = ["Z3"]

#고장이 일어났을 때,
for i in range(0,7):#모든 고장 지점에 대해 max(RSI)
    #연계 피더가 각 부하의 거리를 산정
    #위 값을 비교하여 큰 값을 RSI로 산정
    FP = "Z{}".format(i)#특정 고장점 선정
    #연계 계통 연결
    for j in len(Z)+1:#특정 고장점에 대한 고장 부하 외 모든 RSI 선정
        if j == 1:
          0
        else:  
            globals()["RSI_" + SP[0] + "_Z{}".format(j)]  = globals()[SP[0]] - 어느구간의 Z합 
        # RSI3도 계산
    #연계 피더 번호만 다르고, 부하 번호 같은 변수끼리 대소 비교
    #RSI 선정

#부하, 피더, 가공된 거리 값을 3차원 배열로, 용량*x*y 로 생성. 
#이 좌표를 가지고 그리드 출력