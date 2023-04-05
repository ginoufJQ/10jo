sum = 0
FP = 0
FRK = 0
remove_set = {0}

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



#직선경로
L = ["L1","L2","L3"]
L1 = ["F1","Z1","Z2","Z3","Z4","F3"] 
L2 = ["F2","Z6","Z5","Z3"]     
L3 = list(reversed(L1))

#Main피더
MP = "F1"
#연계피더
SP = ["F2","F3"]

#분기점 (L1과 L2에서 중복된 값 찾기,,)
FRK = list(set(L1).intersection(L2))[0]

#고장점
for i in range(1,7):#6개 지점

    FP = "Z{}".format(i)#특정 고장점
    

    ZRI_F3_Z6 = 0
    ZRI_F3_Z5 = 0
    ZRI_F3_Z4 = 0
    ZRI_F3_Z3 = 0
    ZRI_F3_Z2 = 0
    ZRI_F3_Z1 = 0
    

    L3 = ["F3", "Z4","Z3","Z2","Z1","F1"]

    
        #피더부터 고장점 앞까지 계산.
    if (FP in L3) == True :                       ##L3에 고장점이 있으면(고장점이 분기점인 경우도 여기에 포함됨.)
        number = L3.index(FP) - L3.index("F3")     ## 피더랑 고장점 위치 차이만큼
        sum = globals()['F3']                                   ## F3용량에서
        for l in range(1,number):      
            sum = sum - globals()[L3[l]]           ## F3부터 고장점 앞까지(고장점 포함X)의 부하량을 차례로 빼준다.
            globals()["ZRI_F3_{}".format(L3[l])]=sum  ## 값 입력

        #피더부터 분기점까지 계산.
    else :                                          ##L3에 고장점이 없으면
        number = L3.index(FRK) - L3.index("F3")    ## 피더랑 분기점 위치 차이만큼
        sum = sum = globals()['F3']                          ## F3용량에서
        for l in range(1,number+1):      
            sum = sum - globals()[L3[l]]            ## F3부터 분기점까지(분기점 포함이므로 number+1)의 부하량을 차례로 빼준다.
            globals()["ZRI_F3_{}".format(L3[l])]=sum  ## 값 입력


        ##L3이 아니라 고장점 있는 라인인 L2에서 계산해야함.
        if L2.index(FRK) <  L2.index(FP) :             ##고장점이 분기점 오른쪽에 있으면
            number = L2.index(FP) - L2.index(FRK)      ##분기점이랑 고장점 위치 차이만큼
            sum =  ZRI_F3_Z3                            ##위에서 계산한, 분기점에서의 구간복구지수에서 
                                                    ## 안됨.. sum =  globals()["ZRI_F3_".format(globals()["FRK"])] 
            
            if number == 1 :  # number=1이면 계산 할 필요 없음
                pass
            else :
                for l in range(1,number):
                    sum = sum - globals()[L2[L2.index(FRK)+l]]      ##분기점 이후부터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 오른쪽 방향으로 부하 빼므로 +l)
                    globals()["ZRI_F3_{}".format(L2[L2.index(FRK)+l])]=sum    ##값 입력


        if L2.index(FRK) >  L2.index(FP) :               ##고장점이 분기점 왼쪽에 있으면
            number = L2.index(FRK) -  L2.index(FP)       ## 분기점이랑 고장점 위치 차이만큼
            sum =  ZRI_F3_Z3                             ##위에서 계산한, 분기점에서의 구간복구지수에서 
                                
            if number == 1 : # number=1이면 계산 할 필요 없음
                pass
            else : 
                for l in range(1,number):
                        sum = sum - globals()[L2[L2.index(FRK)-l]]               ##분기점 이후분터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 왼쪽 방향으로 부하 빼므로 -l)
                        globals()["ZRI_F3_{}".format(L2[L2.index(FRK)-l])]=sum      ## 값 입력

    

    ZRI_F3_Z6 ##1500
    ZRI_F3_Z5 ##2000
    ZRI_F3_Z4 ##4000
    ZRI_F3_Z3 ##3000
    ZRI_F3_Z2 ##2500 잘나온다!!!
    ZRI_F3_Z1 
    
    ZRI_F3 = [ZRI_F3_Z1,ZRI_F3_Z2,ZRI_F3_Z3,ZRI_F3_Z4,ZRI_F3_Z5,ZRI_F3_Z6]
    ZRI_F3_R = [n for n in ZRI_F3 if n not in remove_set]  # ZRI_F3에서 0뺀 리스트


    ##################################################### F2의 경우########################
    ZRI_F2_Z6 = 0
    ZRI_F2_Z5 = 0
    ZRI_F2_Z4 = 0
    ZRI_F2_Z3 = 0
    ZRI_F2_Z2 = 0
    ZRI_F2_Z1 = 0

    L2 = ["F2","Z6","Z5","Z3"]     

        #피더부터 고장점 앞까지 계산.
    if (FP in L2 )== True :                       ##L2에 고장점이 있으면(고장점이 분기점인 경우도 여기에 포함됨.)
        number = L2.index(FP) - L2.index("F2")     ## 피더랑 고장점 위치 차이만큼
        sum = sum = globals()['F2']                                    ## F2용량에서
        for l in range(1,number):      
            sum = sum - globals()[L2[l]]           ## F2부터 고장점 앞까지(고장점 포함X)의 부하량을 차례로 빼준다.
            globals()["ZRI_F2_{}".format(L2[l])]=sum  ## 값 입력

        #피더부터 분기점까지 계산.
    else :                                          ##L2에 고장점이 없으면
        number = L2.index(FRK) - L2.index("F2")    ## 피더랑 분기점 위치 차이만큼
        sum = sum = globals()['F2']                  ## F2용량에서
        for l in range(1,number+1):      
            sum = sum - globals()[L2[l]]            ## F2부터 분기점까지(분기점 포함이므로 number+1)의 부하량을 차례로 빼준다.
            globals()["ZRI_F2_{}".format(L2[l])]=sum  ## 값 입력


        ##L2가 아니라 고장점 있는 라인인 L1에서 계산해야함.
        if L1.index(FRK) <  L1.index(FP) :             ##고장점이 분기점 오른쪽에 있으면
            number = L1.index(FP) - L1.index(FRK)      ##분기점이랑 고장점 위치 차이만큼
            sum =  ZRI_F2_Z3                            ##위에서 계산한, 분기점에서의 구간복구지수에서 
                                                    ## 안됨.. sum =  globals()["ZRI_F3_".format(globals()["FRK"])] 
            
            if number == 1 :  # number=1이면 계산 할 필요 없음
                pass
            else :
                for l in range(1,number):
                    sum = sum - globals()[L1[L1.index(FRK)+l]]      ##분기점 이후부터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 오른쪽 방향으로 부하 빼므로 +l)
                    globals()["ZRI_F2_{}".format(L1[L1.index(FRK)+l])]=sum    ##값 입력


        if L1.index(FRK) >  L1.index(FP) :               ##고장점이 분기점 왼쪽에 있으면
            number = L1.index(FRK) -  L1.index(FP)       ## 분기점이랑 고장점 위치 차이만큼
            sum =  ZRI_F2_Z3                             ##위에서 계산한, 분기점에서의 구간복구지수에서 
                                
            if number == 1 : # number=1이면 계산 할 필요 없음
                pass
            else : 
                for l in range(1,number):
                        sum = sum - globals()[L1[L1.index(FRK)-l]]               ##분기점 이후분터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 왼쪽 방향으로 부하 빼므로 -l)
                        globals()["ZRI_F2_{}".format(L1[L1.index(FRK)-l])]=sum      ## 값 입력
    

    ZRI_F2_Z6 ##4000
    ZRI_F2_Z5 ##3000
    ZRI_F2_Z4 ##1500
    ZRI_F2_Z3 ##2000
    ZRI_F2_Z2 ##1500
    ZRI_F2_Z1 


    ZRI_F2 = [ZRI_F2_Z1,ZRI_F2_Z2,ZRI_F2_Z3,ZRI_F2_Z4,ZRI_F2_Z5,ZRI_F2_Z6]
    ZRI_F2_R = [m for m in ZRI_F2 if m not in remove_set]  # ZRI_F2에서 0뺀 리스트
    
    # 0을 뺀 리스트에서 제일 작은 값이 고장점 직전까지 계산값
    # ZRI_F2_R와 ZRI_F3_R MIN 값 비교해서 큰 값이 있는쪽이 ZRI


    if ZRI_F2_R == []:  
        ZRI = ZRI_F3
    elif ZRI_F3_R == []:
        ZRI = ZRI_F2
    else: 
        if min(ZRI_F3_R) > min(ZRI_F2_R):
            ZRI = ZRI_F3 
        else:
            ZRI = ZRI_F2
    
    print("ZRI_F3 = ", ZRI_F3)
    print("ZRI_F2 = ", ZRI_F2)
    print("ZRI = ", ZRI)
    
 
        
   

























































































