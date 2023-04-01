
Z1 = 1000 #고장 전 Z1이 1000이라고 가정
Z2 = 500
Z3 = 1000
Z4 = 500
Z5 = 1000
Z6 = 1500

FM1 = 14000
FM2 = 14000
FM3 = 14000

FTL1 = Z1 + Z2 + Z3 + Z4 + Z5 + Z6
FTL2 = 8500
FTL3 = 9500

F1 = FM1 - FTL1
F2 = FM2 - FTL2
F3 = FM3 - FTL3

#Z1에서 고장 발생
RSI2_Z6 = F2 - Z6 
RSI2_Z5 = F2 - Z6 - Z5
RSI2_Z3 = F2 - Z6 - Z5 - Z3
RSI2_Z2 = F2 - Z6 - Z5 - Z3 - Z2
RSI2_Z4 = F2 - Z6 - Z5 - Z3 - Z4


RSI3_Z4 = F3 - Z4
RSI3_Z3 = F3 - Z4 - Z3
RSI3_Z2 = F3 - Z4 - Z3 - Z2
RSI3_Z5 = F3 - Z4 - Z3 - Z5
RSI3_Z6 = F3 - Z4 - Z3 - Z5 - Z6 



if RSI2_Z6 >= RSI3_Z6 :
    RSI_Z6 = RSI2_Z6
else :
    RSI_Z6 = RSI3_Z6

if RSI2_Z5 >= RSI3_Z5 :
    RSI_Z5 = RSI2_Z5
else :
    RSI_Z5 = RSI3_Z5

if RSI2_Z4 >= RSI3_Z4 :
    RSI_Z4 = RSI2_Z4
else :
    RSI_Z4 = RSI3_Z4

if RSI2_Z3 >= RSI3_Z3 :
    RSI_Z3 = RSI2_Z3
else :
    RSI_Z3 = RSI3_Z3

if RSI2_Z2 >= RSI3_Z2 :
    RSI_Z2 = RSI2_Z2
else :
    RSI_Z2 = RSI3_Z2


RSI_Z4 = -1000 #4번 복구 불가능하면..
print(RSI_Z6)
print(RSI_Z5)
print(RSI_Z4)
print(RSI_Z3)
print(RSI_Z2)


list_RSI = [RSI_Z6 , RSI_Z5,RSI_Z4,RSI_Z3, RSI_Z2]

number = 7
for n in list_RSI :
    number = number - 1
    if n >= 0 :
        print("%d번 부하는 복구 가능합니다." % number)
    else : 
        print("%d번 부하는 복구 불가능합니다." % number)


        


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
sum = 0
FP = 0
FRK = 0


#용량 입력
Z = [1000,500,1000,500,1000,1500]
del sum
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
#



#직선경로
L = ["L1","L2","L3"]
L1 = ["F1","Z1","Z2","Z3","Z4","F3"] ##가로
L2 = ["F2","Z6","Z5","Z3"]     ##세로
L3 = ["F3", "Z4","Z3","Z2","Z1","F1"]

#Main피더
MP = "F1"
#연계피더
SP = ["F2","F3"]

#분기점
FRK = "Z3"

#고장점
FP = "Z1"





############# F3의 경우에...
L3 = ["F3", "Z4","Z3","Z2","Z1","F1"]


if (FP in L3 )== True :                             ##L3에 분기점이 있으면..
    number = L3.index(FP) - L3.index("F3")          ## 피더이랑 고장점 위치 차이
    sum = F3                                         ## F3용량에서
    for l in range(1,number):      
        sum = sum - globals()[L3[l]]                 ## F3후부터 고장점 앞까지의 부하량을 차례로 빼준다....
        globals()["ZRI_F3_{}".format(L3[l])]=sum      ## 부하량 하나 빼고 값 입력하고, 하나 빼고 값 입력하고..


else :                                                ##L3에 분기점이 없으면..
    number = L3.index(FP) - L3.index("F3")          ## 피더이랑 고장점 위치 차이
    sum = F3                                         ## F3용량에서
    for l in range(1,number):      
        sum = sum - globals()[L3[l]]                 ## F3후부터 고장점 앞까지의 부하량을 차례로 빼준다....
        globals()["ZRI_F3_{}".format(L3[l])]=sum      ## 부하량 하나 빼고 값 입력하고, 하나 빼고 값 입력하고..



    if L3.index(FRK) <  L3.index(FP) :                                  ##고장점이 분기점 오른쪽에 있으면..
        number = L3.index(FP) - L3.index(FRK)                            ## 분기점이랑 고장점 위치 차이
        sum =  ZRI_F3_Z3                                                 ##분기점에서의 구간복구지수를 가져와서.. 
          for l in range(1,number):
                sum = sum - globals()[L3[L3.index(FRK)+l]]                ##분기점 이후분터 고장점 앞까지 부하량을 차례로 빼준다....
                globals()["ZRI_F3_{}".format(L3[L3.index(FRK)+l])]=sum       ## 부하량 하나 빼고 값 입력하고, 하나 빼고 값 입력하고..


    if L3.index(FRK) >  L3.index(FP) :                               ##고장점이 분기점 왼쪽에 있으면..
        number = L3.index(FRK) -  L3.index(FP)                        ## 분기점이랑 고장점 위치 차이
        sum =  ZRI_F3_Z3                                             ##분기점에서의 구간복구지수를 가져와서.. 
        for l in range(1,number):
                sum = sum - globals()[L3[L3.index(FRK)-l]]               ##분기점 이후분터 고장점 앞까지 부하량을 차례로 빼준다....
                globals()["ZRI_F3_{}".format(L3[L3.index(FRK)-l])]=sum      ## 부하량 하나 빼고 값 입력하고, 하나 빼고 값 입력하고..


ZRI_F3_Z4
ZRI_F3_Z3
ZRI_F3_Z2













Calculate_ZRI(node)
    if node is leaf
        node.ZRI = connected_BF_margin-node.load
    else   
        FOR all child_node
            Calculate_ZRI(child_node)
        end for
    node.ZRI = max(child_node.ZRI)-node.load
    end if