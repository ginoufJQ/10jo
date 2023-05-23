
sum = 0
FP = 0
FRK = 0


#용량 입력
Z = [150,200,250,200,200,400,300,300,300,500,300,100,300,500,600,400,100,300,500,600,400,400,400,300,300,200,500,300,150,100,200,100]
# sum = 0
# for i in range(0,33):
#     sum = sum +  Z[i]
#     sum

del sum
FTL = [7200,9600,9600,7500,7900,10000,9000,9500,9500]
FM = 14000

for i in range(1, len(Z)+1): 
    globals()["Z{}".format(i)]=Z[i-1]
   
for i in range(1,len(FTL)+1):
    globals()["FM{}".format(i)]=FM

for i in range(1,len(FTL)+1):
    globals()["FTL{}".format(i)]=FTL[i-1]

for i in range(1,len(FTL)+1):
    globals()["F{}".format(i)]=FM-FTL[i-1]
    
# F1~F9 [6800,4400,4400,6500,6100,4000,5000,4500,4500]




#직선경로. 일반화할 필요X
L = ["L1","L2","L3","L4","L5","L6","L7","L8","L9"]
L1 = ["F1","Z1","Z3","Z5","Z8","Z17","Z23","Z28","Z29","Z31","Z30",     "Z22","Z15","Z14","Z13", "Z12","Z11","Z10","Z9","F"]   
L2 = ["F2","Z2","Z4", "Z6","Z14","Z13", "Z12","Z11","Z10","Z9","F"] 
L3 = ["F3","Z7","Z23","Z28","Z29", "Z31","Z30",     "Z22","Z15","Z14","Z13", "Z12","Z11","Z10","Z9","F"]     
L4 = ["F4","Z16","Z15","Z14","Z13", "Z12","Z11","Z10","Z9", "F"]  
L5 = ["F5","Z20","Z19", "Z18", "Z17","Z23","Z28","Z29", "Z31","Z30",     "Z22","Z15","Z14","Z13", "Z12","Z11","Z10","Z9","F"]   
L6 = ["F6","Z26","Z25","Z28","Z29", "Z31","Z30",     "Z22","Z15","Z14","Z13", "Z12","Z11","Z10","Z9","F"]  
L7 = ["F7","Z21","Z10","Z9","F"]  
L8 = ["F8","Z27", "Z24", "Z19" , "Z18", "Z17","Z23","Z28","Z29", "Z31","Z30",     "Z22","Z15","Z14","Z13", "Z12","Z11","Z10","Z9","F"]  
L9 = ["F9", "Z32", "Z31","Z30",     "Z22","Z15","Z14","Z13", "Z12","Z11","Z10","Z9","F"]


#Main피더
MP = "F" 
#연계피더
SP = ["F1","F2","F3","F4","F5","F6","F7","F8","F9"] 
#분기점
# FRK = ["Z3"] 
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
   
\

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*ZRI_list, sep='\n')

hasattr