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
L3 = list(reversed(L1))

#Main피더
MP = "F1"

#연계피더
SP = ["F2","F3"]

#분기점
FRK = list(set(L1) & set(L2))






###################################### 방법 1 #################################
#직선경로
L = ["L1","L2","L3"]
L1 = ["F1","Z1","Z2","Z3","Z4","F3"]
L2 = ["F2","Z6","Z5","Z3"]
L3 = list(reversed(L1))

FRK = list(set(L1) & set(L2))

for i in range(1,7):#6개 지점에 대해 max(RSI)  

    FP = "Z{}".format(i)#특정 고장점

    # F2부터 분기점까지
    for j in range(1,L2.index(FRK)+1):
        F2_FRK = F2_FRK-globals()[L2[j]]
        globals()["ZRI_F2_{}".format(L2[j])]=F2_FRK
    
    # F3에서 분기점까지
    if L3.index(FRK) < L3.index(FP):
        for k in range(1,L3.index(FRK)+1):
        F3_FRK = F3_FRK-globals()[L3[k]]
        globals()["ZRI_F3_{}".format(L3[k])]=F3_FRK

    # F1에서 분기점까지
    else:
        for k in range(1,L1.index(FRK)+1):
        F3_FRK = F3_FRK-globals()[L3[k]]
        globals()["ZRI_F3_{}".format(L3[k])]=F3_FRK

    # 연계점에서 구간복구지수
    if F2_FRK < F3_FRK:
        ZRI = F3_FRK
    else:
        ZRI = F2_FRK


    if L3.index(FRK) < L3.index(FP):                                  
        sum = ZRI                                               
        for m in range(1,L3.index(FP)-L3.index(FRK)):
                ZRI = ZRI - globals()[L3[L3.index(FRK)]]               
                globals()["ZRI_F3_{}".format(L3[L3.index(FRK)])]= ZRI  

~~~~~
    


  
       
################################# 방법2 ############################
import pandas as pd
import numpy


#직선경로
L = ["L1","L2","L3"]
L1 = ["F1","Z1","Z2","Z3","Z4","F3"]
L2 = ["F2","Z6","Z5","Z3"]
L3 = list(reversed(L1))

FRK = list(set(L1) & set(L2))

#고장이 일어났을 때,
for i in range(1,7):#6개 지점에 대해 max(RSI)  

    FP = "Z{}".format(i)#특정 고장점

if L1.index(FP) < L1.index(FRK):
    ZRI1 = L3[:L3.index(FRK)]
    ZRI2 = L2[:L2.index(FRK)]
    ZRI3 = L3[L3.index(FRK):L3.index(FP)-1]
    if 2*ZRI1[0]-sum(ZRI1) < 2*ZRI2[0]-sum(ZRI2):
       ZRI = ZRI1 + ZRI3
    else :
       ZRI = ZRI2 + ZRI3

if L1.index(FP) > L1.index(FRK):
    ZRI1 = L1[:L1.index(FRK)]
    ZRI2 = L2[:L2.index(FRK)]
    ZRI3 = L1[L1.index(FRK):L3.index(FP)-1]
    if 2*ZRI1[0]-sum(ZRI1) < 2*ZRI2[0]-sum(ZRI2):
        ZRI = ZRI1 + ZRI3
    else :
        ZRI = ZRI2 + ZRI3
    
else:
    ZRI1 = L1[:L1.index(FRK)]
    ZRI2 = L3[:L3.index(FRK)]
    ZRI3 = L2[:]



























###################################### 방법 1 #################################
#직선경로
L = ["L1","L2","L3"]
L1 = ["F1","Z1","Z2","Z3","Z4","F3"]
L2 = ["F2","Z6","Z5","Z3"]
L3 = list(reversed(L1))

FRK = list(set(L1) & set(L2))

for i in range(1,7):#6개 지점에 대해 max(RSI)  

    FP = "Z{}".format(i)#특정 고장점

    # F2부터 분기점까지
    for j in range(1,L2.index(FRK)+1):
        F2_FRK = F2_FRK-globals()[L2[j]]
        globals()["ZRI_F2_{}".format(L2[j])]=F2_FRK
    
    # F3에서 분기점까지
    if L3.index(FRK) < L3.index(FP):
        for k in range(1,L3.index(FRK)+1):
        F3_FRK = F3_FRK-globals()[L3[k]]
        globals()["ZRI_F3_{}".format(L3[k])]=F3_FRK

    # F1에서 분기점까지
    else:
        for k in range(1,L1.index(FRK)+1):
        F3_FRK = F3_FRK-globals()[L3[k]]
        globals()["ZRI_F3_{}".format(L3[k])]=F3_FRK

    # 연계점에서 구간복구지수
    if F2_FRK < F3_FRK:
        ZRI = F3_FRK
    else:
        ZRI = F2_FRK


    if L3.index(FRK) < L3.index(FP):                                  
        sum = ZRI                                               
        for m in range(1,L3.index(FP)-L3.index(FRK)):
                ZRI = ZRI - globals()[L3[L3.index(FRK)]]               
                globals()["ZRI_F3_{}".format(L3[L3.index(FRK)])]= ZRI  


    


  
       
################################# 방법2 ############################
import pandas as pd
import numpy


#직선경로
L = ["L1","L2","L3"]
L1 = ["F1","Z1","Z2","Z3","Z4","F3"]
L2 = ["F2","Z6","Z5","Z3"]
L3 = list(reversed(L1))

FRK = list(set(L1) & set(L2))

#고장이 일어났을 때,
for i in range(1,7):#6개 지점에 대해 max(RSI)  

    FP = "Z{}".format(i)#특정 고장점

if L1.index(FP) < L1.index(FRK):
    ZRI1 = L3[:L3.index(FRK)]
    ZRI2 = L2[:L2.index(FRK)]
    ZRI3 = L3[L3.index(FRK):L3.index(FP)-1]
    if 2*ZRI1[0]-sum(ZRI1) < 2*ZRI2[0]-sum(ZRI2):
       ZRI = ZRI1 + ZRI3
    else :
       ZRI = ZRI2 + ZRI3

if L1.index(FP) > L1.index(FRK):
    ZRI1 = L1[:L1.index(FRK)]
    ZRI2 = L2[:L2.index(FRK)]
    ZRI3 = L1[L1.index(FRK):L3.index(FP)-1]
    if 2*ZRI1[0]-sum(ZRI1) < 2*ZRI2[0]-sum(ZRI2):
        ZRI = ZRI1 + ZRI3
    else :
        ZRI = ZRI2 + ZRI3
    
else:
    ZRI1 = L1[:L1.index(FRK)]
    ZRI2 = L3[:L3.index(FRK)]
    ZRI3 = L2[:]


