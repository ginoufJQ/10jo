import pandas as pd
import numpy

sum = 0 
#GUI로 좌표별 피더, 부하 입력 받으면서 각각에 대한 값 입력

#용량 입력
Z = [1000,500,1000,500,1000,1500]
FTL = [sum(Z),8500,9500]
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
for i in range(0,7):#6개 지점에 대해 max(RSI)

    FP = "Z{}".format(i)#특정 고장점 선정

    for j in range(1,len(Z)+1):
        if j == FP[-1]:#특정 고장점은 제외
          0
        else:  
            for k in range(j):
                sum = sum 
                #F2랑 같은 라인에 있는거 다 더함, 그리고 분기점 옆에 것도 다 더하기. 고장점은 제외
                #리스트 내 거리를 잡은 담에 진행하면 좋을 것 같은데
                #거리는 문자열의 순서값을 뽑아서 비교하면 될 것 같다
            globals()["RSI_" + SP[0] + "_Z{}".format(j)]  = globals()["FM" + SP[0][-1]] - sum
            sum = 0
            # RSI3에 대해서도 계산(sp[1]), 여기선 sum변수가 달라지겠지
        
    #계산 완료 후,
    #연계 피더 번호만 다르고, 부하 번호 같은 변수끼리 대소 비교
    #RSI 선정

#부하, 피더, 가공된 거리 값을 3차원 배열로, 용량*x*y 로 생성. 
#위 좌표를 가지고 그리드 출력
#      ⚪
#      ┃
# ⚪━⚪━✸━⚪━⚪
# 그리드 특수문자 전각, 반각 문자 변환해서 좌표에 깔끔하게 맞추기