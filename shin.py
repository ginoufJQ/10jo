
sum = 0
FP = 0
FRK = 0


#용량 입력
Z = [500,500,1000,700,1200,1100,600,1000,500,900,700,800]
del sum
FTL = [7200,9600,9600,7500,7900,10000,9000,9500]
FM = 14000

for i in range(1, len(Z)+1): 
    globals()["Z{}".format(i)]=Z[i-1]
   
for i in range(1,len(FTL)+1):
    globals()["FM{}".format(i)]=FM

for i in range(1,len(FTL)+1):
    globals()["FTL{}".format(i)]=FTL[i-1]

for i in range(1,len(FTL)+1):
    globals()["F{}".format(i)]=FM-FTL[i-1]
    
# F1~F8[6800,4400,4400,6500,6100,4000,5000,4500]




#직선경로. 일반화가 필요함!!!!!!!!!!!!!!!!!!!!!!!
L = ["L1","L2","L3","L4","L5","L6","L7","L8"]
L1 = ["F1","Z1","Z6", "Z5","Z4","Z3","Z2","F"]   
L2 = ["F2","Z6", "Z5","Z4","Z3","Z2","F"] 
L3 = ["F3","Z8","Z7","Z6", "Z5","Z4","Z3","Z2","F"]     
L4 = ["F4","Z9", "Z8","Z7","Z6", "Z5","Z4","Z3","Z2","F"]  
L5 = ["F5","Z9", "Z8","Z7","Z6", "Z5","Z4","Z3","Z2","F"]   
L6 = ["F6","Z9", "Z8","Z7","Z6", "Z5","Z4","Z3","Z2","F"]  
L7 = ["F7","Z11","Z10","Z4","Z3","Z2","F"]  
L8 = ["F8","Z12", "Z11","Z10","Z4","Z3","Z2","F"]  




#Main피더
MP = "F" 
#연계피더
SP = ["F1","F2","F3","F4","F5","F6","F7","F8"] 
#분기점
FRK = ["Z3"] 
#고장점
FP

# 빈 리스트 생성. 리스트는 Z1~Z6 6개, 6*6 리스트 생성
ZRI_list = []

for r in range( len(Z)):
    line = []
    for s in range( len(Z)):
        line.append([])
    ZRI_list.append(line)
 

print(*ZRI_list, sep='\n')

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
    else:
      ZRI_list[n][m] = []
   


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*ZRI_list, sep='\n')



















#아 이 아래 겁나 열심히했는데 없어도되네 간단해져서 개빡침;ㅠ

        
        
        
                                                              ##L1(연계피더 라인)에 고장점이 없으면
            # number = globals()["L" + str(f)].index(FRK[0]) - globals()["L" + str(f)].index("F" + str(f))    ## 피더랑 분기점 위치 차이만큼
            # sum = globals()["F" + str(f)]                                  ## F1(연계피더)용량에서
            # for l in range(1,number+1):      
            #     sum = sum - globals()[globals()["L" + str(f)][l]]            ## F1(연계피더)부터 분기점까지(분기점 포함이므로 number+1)의 부하량을 차례로 빼준다.
            #     globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])]=sum   ## 값 입력
            #     ZRI_list[b-1][int(str(globals()["L" + str(f)] [l])[1])-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L" + str(f)] [l])] ) ##리스트에 값 추가


            # ##L1(현재 계산중인 연계피더 라인)이 아니라 L2(다른 연계피더의 라인중에서 고장점 있는 라인)를 찾아야 함. 
            # for a in range(0,len(SP)) :       ##L1,L2(모든 연계피더 라인) 중에서 고장점 찾기.  
            #     if FP in globals()[L[a]] :   ### 고장점 있는 L2... = globals()[L[a]]
            #         if globals()[L[a]].index(FRK[0]) <  globals()[L[a]].index(FP) :             ##고장점이 분기점 오른쪽에 있으면
            #             number = globals()[L[a]].index(FP) - globals()[L[a]].index(FRK[0])      ##분기점이랑 고장점 위치 차이만큼
            #             sum =  globals()["ZRI_" + "F" + str(f) + "_" + FRK[0]]                   ##위에서 계산한, 분기점에서의 구간복구지수에서 
    
            #             if number == 1 :  # number=1이면 계산 할 필요 없음
            #                 pass
            #             else:
            #                 for l in range(1,number):
            #                     sum = sum - globals()[globals()[L[a]][globals()[L[a]].index(FRK[0])+l]]      ##분기점 이후부터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 오른쪽 방향으로 부하 빼므로 +l)
            #                     globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])+l])]=sum    ##값 입력     
            #                     ZRI_list[b-1][int(str(globals()[L[a]][globals()[L[a]].index(FRK[0])+l])[1])-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])+l])] ) ##리스트에 값 추가

            #         if globals()[L[a]].index(FRK[0]) >  globals()[L[a]].index(FP) :               ##고장점이 분기점 왼쪽에 있으면
            #             number = globals()[L[a]].index(FRK[0]) -  globals()[L[a]].index(FP)       ## 분기점이랑 고장점 위치 차이만큼
            #             sum =  globals()["ZRI_" + "F" + str(f) + "_" + FRK[0]]                             ##위에서 계산한, 분기점에서의 구간복구지수에서 

            #             if number == 1 : # number=1이면 계산 할 필요 없음
            #                 pass
            #             else : 
            #                 for l in range(1,number):
            #                         sum = sum - globals()[globals()[L[a]][globals()[L[a]].index(FRK[0])-l]]               ##분기점 이후분터 고장점 앞까지 부하량을 차례로 빼준다.(분기점 왼쪽 방향으로 부하 빼므로 -l)
            #                         globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])-l])]=sum  ## 값 입력
            #                         ZRI_list[b-1][int(str(globals()[L[a]][globals()[L[a]].index(FRK[0])-l])[1])-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()[L[a]][globals()[L[a]].index(FRK[0])-l])] ) ##리스트에 값 추가


