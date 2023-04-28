
sum = 0
FP = 0
FRK = 0


#용량 입력
Z = [1000,500,1000,500,1000,1500]
del sum
FTL = [8500,9500]
FM = 14000

for i in range(1,7): 
    globals()["Z{}".format(i)]=Z[i-1]
   
for i in range(1,4):
    globals()["FM{}".format(i)]=FM

for i in range(1,4):
    globals()["FTL{}".format(i)]=FTL[i-1]

for i in range(1,3):
    globals()["F{}".format(i)]=FM-FTL[i-1]
    



#직선경로
L = ["L1","L2"]
L1 = ["F1","Z6","Z5", "Z3"]   
L2 = ["F2", "Z4","Z3","Z2","Z1","F"] 




#Main피더
MP = "F" 
#연계피더
SP = ["F2","F3"] 

#분기점
FRK = ["Z3"] 
FRK[0]

#고장점
FP

ZRI_list = [[[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]]]   # 빈 리스트 생성. 리스트는 Z1~Z6 6개, 6*6 리스트 생성


########################################################################
for b in range(1,7):   ###고장점 Z1~Z6 6개 지점
    FP = "Z{}".format(b) 
    for f in range(1,len(SP)+1) :  # 연계피더 개수만큼 구간복구지수를 구해야 함
                                                                        ###L1,L2,L3... 값 = globals()["L" + str(f)]  
                                                                        ###F1,F2,F3... 값 = globals()["F" + str(f)] 
                                                                        ###F1,F2,F3... 문자 = "F" + str(f)  
            #피더부터 고장점 앞까지 계산.
        if (FP in globals()["L" + str(f)] )== True :                       ##L1(연계피더 라인)에 고장점이 있으면(고장점이 분기점인 경우도 여기에 포함됨.)
            number = globals()["L" + str(f)].index(FP) - globals()["L" + str(f)].index("F" + str(f))     ## 피더랑 고장점 위치 차이만큼
            sum = globals()["F" + str(f)]                                   ## F1(연계피더)용량에서
            for l in range(1,number):      
                sum = sum - globals()[globals()["L" + str(f)][l]]           ## F1(연계피더)부터 고장점 앞까지(고장점 포함X)의 부하량을 차례로 빼준다.
                globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])]=sum  ## 값 입력
                ZRI_list[b-1][int(str(globals()["L" + str(f)] [l])[1])-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])] ) ##리스트에 값 추가
                                                                    ### Z4라고 하면 int(str(globals()["L" + str(f)] [l])[1])-1 = 3이 되어 네번째 리스트에 들어감

            #피더부터 분기점까지 계산.
        else :                                                         ##L1(연계피더 라인)에 고장점이 없으면
            number = globals()["L" + str(f)].index(FRK[0]) - globals()["L" + str(f)].index("F" + str(f))    ## 피더랑 분기점 위치 차이만큼
            sum = globals()["F" + str(f)]                                  ## F1(연계피더)용량에서
            for l in range(1,number+1):      
                sum = sum - globals()[globals()["L" + str(f)][l]]            ## F1(연계피더)부터 분기점까지(분기점 포함이므로 number+1)의 부하량을 차례로 빼준다.
                globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])]=sum   ## 값 입력
                ZRI_list[b-1][int(str(globals()["L" + str(f)] [l])[1])-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])] ) ##리스트에 값 추가


            ##L1(현재 계산중인 연계피더 라인)이 아니라 L2(다른 연계피더의 라인중에서 고장점 있는 라인)를 찾아야 함. 
            for a in range(0,len(SP)) :       ##L1,L2(모든 연계피더 라인) 중에서 고장점 찾기.  
                if FP in globals()[L[a]] :   ### 고장점 있는 L2... = globals()[L[a]]
                    if globals()[L[a]].index(FRK[0]) <  globals()[L[a]].index(FP) :             ##고장점이 분기점 오른쪽에 있으면
                        number = globals()[L[a]].index(FP) - globals()[L[a]].index(FRK[0])      ##분기점이랑 고장점 위치 차이만큼
                        sum =  globals()["ZRI_" + "F" + str(f) + "_" + FRK[0]]                   ##위에서 계산한, 분기점에서의 구간복구지수에서 
    
                        if number == 1 :  # number=1이면 계산 할 필요 없음
                            pass
                        else:
                            for l in range(1,number):
                                sum = sum - globals()[globals()[L[a]][globals()[L[a]].index(FRK[0])+l]]      ##분기점 이후부터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 오른쪽 방향으로 부하 빼므로 +l)
                                globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])+l])]=sum    ##값 입력     
                                ZRI_list[b-1][int(str(globals()[L[a]][globals()[L[a]].index(FRK[0])+l])[1])-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])+l])] ) ##리스트에 값 추가

                    if globals()[L[a]].index(FRK[0]) >  globals()[L[a]].index(FP) :               ##고장점이 분기점 왼쪽에 있으면
                        number = globals()[L[a]].index(FRK[0]) -  globals()[L[a]].index(FP)       ## 분기점이랑 고장점 위치 차이만큼
                        sum =  globals()["ZRI_" + "F" + str(f) + "_" + FRK[0]]                             ##위에서 계산한, 분기점에서의 구간복구지수에서 

                        if number == 1 : # number=1이면 계산 할 필요 없음
                            pass
                        else : 
                            for l in range(1,number):
                                    sum = sum - globals()[globals()[L[a]][globals()[L[a]].index(FRK[0])-l]]               ##분기점 이후분터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 왼쪽 방향으로 부하 빼므로 -l)
                                    globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])-l])]=sum  ## 값 입력
                                    ZRI_list[b-1][int(str(globals()[L[a]][globals()[L[a]].index(FRK[0])-l])[1])-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])-l])] ) ##리스트에 값 추가


print(*ZRI_list, sep='\n')



################################# 최대값으로 ZRI 결정 ################################################

# ㅡㅡㅡ 일반화 부탁 ㅡㅡㅡㅡ
ZRI_list[0][0] = [max(ZRI_list[0][0])]
ZRI_list[0][1] = [max(ZRI_list[0][1])]
ZRI_list[0][2] = [max(ZRI_list[0][2])]
ZRI_list[0][3] = [max(ZRI_list[0][3])]
ZRI_list[0][4] = [max(ZRI_list[0][4])]
ZRI_list[0][5] = [max(ZRI_list[0][5])]

ZRI_list[1][0] = [max(ZRI_list[1][0])]
ZRI_list[1][1] = [max(ZRI_list[1][1])]
ZRI_list[1][2] = [max(ZRI_list[1][2])]
ZRI_list[1][3] = [max(ZRI_list[1][3])]
ZRI_list[1][4] = [max(ZRI_list[1][4])]
ZRI_list[1][5] = [max(ZRI_list[1][5])]

ZRI_list[2][0] = [max(ZRI_list[2][0])]
ZRI_list[2][1] = [max(ZRI_list[2][1])]
ZRI_list[2][2] = [max(ZRI_list[2][2])]
ZRI_list[2][3] = [max(ZRI_list[2][3])]
ZRI_list[2][4] = [max(ZRI_list[2][4])]
ZRI_list[2][5] = [max(ZRI_list[2][5])]

ZRI_list[3][0] = [max(ZRI_list[3][0])]
ZRI_list[3][1] = [max(ZRI_list[3][1])]
ZRI_list[3][2] = [max(ZRI_list[3][2])]
ZRI_list[3][3] = [max(ZRI_list[3][3])]
ZRI_list[3][4] = [max(ZRI_list[3][4])]
ZRI_list[3][5] = [max(ZRI_list[3][5])]

ZRI_list[4][0] = [max(ZRI_list[4][0])]
ZRI_list[4][1] = [max(ZRI_list[4][1])]
ZRI_list[4][2] = [max(ZRI_list[4][2])]
ZRI_list[4][3] = [max(ZRI_list[4][3])]
ZRI_list[4][4] = [max(ZRI_list[4][4])]
ZRI_list[4][5] = [max(ZRI_list[4][5])]

ZRI_list[5][0] = [max(ZRI_list[5][0])]
ZRI_list[5][1] = [max(ZRI_list[5][1])]
ZRI_list[5][2] = [max(ZRI_list[5][2])]
ZRI_list[5][3] = [max(ZRI_list[5][3])]
ZRI_list[5][4] = [max(ZRI_list[5][4])]
ZRI_list[5][5] = [max(ZRI_list[5][5])]


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*ZRI_list, sep='\n')

