import pandas as pd
from sklearn.preprocessing import MinMaxScaler


sum = 0
FP = 0
FRK = 0


#용량 입력
Z = [500,500,1000,700,1200,1100,600,1000,500,1000,2000,3000]
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


#직선경로. 일반화가 필요없음
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

# 빈 리스트 생성. 리스트는 Z1~Z12 12개, 6*6 리스트 생성
ZRI_list = []

for r in range( len(Z)):
    line = []
    for s in range( len(Z)):
        line.append([])
    ZRI_list.append(line)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*ZRI_list, sep='\n')

new_L = []  # Z갯수 12 * F 갯수 8 행렬. 그안에 또 12개의 리스트.
new_L = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))] 
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*new_L, sep='\n')

########################################################################
for b in range(1, len(Z)+1):   ###고장점 Z1~Z12 12개 지점
    FP = "Z{}".format(b) 


    for f in range(1,len(SP)+1) :  # 연계피더 개수만큼 구간복구지수를 구해야 함
    
    
        if (FP in globals()["L" + str(f)] )== True :                       ##L1~L8(연계피더 라인)에 고장점이 있으면
            number = globals()["L" + str(f)].index(FP) - globals()["L" + str(f)].index("F" + str(f))     ## 피더랑 고장점 위치 차이만큼
            sum = globals()["F" + str(f)]                                   ## F1~F8(연계피더)용량에서
            for l in range(1,number):      
                sum = sum - globals()[globals()["L" + str(f)][l]]           ## F1~F8(연계피더)부터 고장점 앞까지(고장점 포함X)의 부하량을 차례로 빼준다.
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

####최대값으로 ZRI 결정


for n in range(len(ZRI_list)): ## ZRI_list의 행
  for m in range(len(ZRI_list[n])): ## ZRI_list의 열
    if ZRI_list[n][m]: 
      ZRI_list[n][m] = [max(ZRI_list[n][m])] ## 각 부하 ZRI의 최대값으로 결정
    else:
      ZRI_list[n][m] = []
     

############

###ZRI_list 출력
df = pd.DataFrame(ZRI_list, columns = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'])
print(df)


###new_L 출력
df = pd.DataFrame(new_L, columns = ['F1','F2','F3','F4','F5','F6','F7','F8'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'])
print(df)


################### 선로의 여유용량을 구함

mg = [[[] for x in range(len(SP))] for y in range(len(Z))]


for e in range(1, len(Z)+1):
   for k in range(1, len(SP)+1):
      for g in range(1, len(Z)+1):
         for h in new_L[e-1][k-1][g-1]:
            if h in ZRI_list[e-1][g-1]:
                mg[e-1][k-1].append(h)       ### 피더K의 여유용량을mg리스트에 넣음 
            else :
               pass

for len1 in range(1,len(mg)+1):      ### Z1~Z12에서 고장났을때가 행
  for len2 in range(1, len(mg[len1-1])+1):      ### Z1~Z12의 고복지가 열
    if mg[len1-1][len2-1]: 
      mg[len1-1][len2-1] = [min(mg[len1-1][len2-1])]     ### 연계되는 피더의 여유용량
    else:
      mg[len1-1][len2-1] = [globals()['F' + str(len2)]]       ### 연계안되는 피더의 여유용량

### mg 출력
df = pd.DataFrame(mg, columns =  ['F1','F2','F3','F4','F5','F6','F7','F8'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'])
print(df)

########################## 선로 증설시의 뉴복지

new_ZRI_list = []
new_ZRI_list  = [[[] for x in range(len(Z))] for y in range(len(Z))]

ZRI_list[2][3] = [-99999]

##하다 말았음
for o in range(len(SP)+1) : 
    for n in range(len(Z)+1) :
        for m in range(len(Z)+1) :
            if ZRI_list[n][m][0] < 0 :  ##고복지 값이 음수이면..
             new_ZRI_list[n][m].append(ZRI_list[n][m][0] - mg[n][o][m])    ### (고장 전의 고복지 값) - (피더의 여유용량)  입력
##하다 말았음


###ZRI_list 출력
df = pd.DataFrame(ZRI_list, columns = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'])
print(df)


###new_ZRI_list 출력
df = pd.DataFrame(new_ZRI_list, columns = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'])
print(df)


##############################################



### 그


#scaler = MinMaxScaler()

#scaler.fit(ZRI_list[])
#ZRI_list_scaled = scaler.transform(ZRI_list)

#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#print(ZRI_list_scaled)

