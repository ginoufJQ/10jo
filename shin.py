import pandas as pd
from sklearn.preprocessing import MinMaxScaler


sum = 0
FP = 0
FRK = 0


#용량 입력
Z = [10,20,30,40,50,60,70,10,20,30,40,50,60,70,10,20,30,40,50,60,70]
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




###########################  계통 바뀌어도 이 윗부분만 수정하면 됨! (df 출력시에 컬럼이랑 인덱스는 바꿔줘야함)###########################




# 빈 리스트 생성. 리스트는 Z1~Z12 12개, 6*6 리스트 생성
ZRI_list = []

for r in range( len(Z)):
    line = []
    for s in range( len(Z)):
        line.append([])
    ZRI_list.append(line)

new_L = []  # Z갯수 12 * F 갯수 8 행렬. 그안에 또 12개의 리스트.
new_L = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))] 


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
df = pd.DataFrame(ZRI_list, columns = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'])
print(df)


###new_L 출력
df = pd.DataFrame(new_L, columns = ['F1','F2','F3','F4','F5'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'])
print(df)


################### 선로의 여유용량을 구함

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

### mg 출력
df = pd.DataFrame(mg, columns =  ['F1','F2','F3','F4','F5'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'])
print(df)

########################## 선로 증설시의 뉴복지

# new_ZRI_list = []
# new_ZRI_list  = [[[] for x in range(len(Z))] for y in range(len(Z))]



# ###ZRI_list 출력
# df = pd.DataFrame(ZRI_list, columns = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'], 
#                                 index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'])
# print(df)


# ###new_ZRI_list 출력
# df = pd.DataFrame(new_ZRI_list, columns = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'], 
#                                 index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12'])
# print(df)


###############################직선경로부하로 계산해서 문제상황 일어나는 경우 알고리즘###############


FRK_list= []
for N in range( len(SP) ):
        FRK_list.append([])

for i in range(1 ,len(SP)+1) :
    intersection = [x for x in globals()['L' + str(i)] if x in L]  # L이랑 L1~L8 안의 값을 차례대로 비교를 할껀데, 가장 먼저 겹치는 게 F1~F8의 분기점임!!!! 
    FRK_list[i-1].append(intersection[0]) ###리스트에 값 입력

###FRK_list 출력. 연계피더의 분기점 리스트 생성
df = pd.DataFrame({'각 연계피더의 분기점': FRK_list}, index=['F1', 'F2', 'F3', 'F4','F5'])
print(df)




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
df = pd.DataFrame(FRK_feeder_list, columns =  ['F1','F2','F3','F4','F5'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'])
print(df)





FRK_fdm_list=  [[[] for x in range(len(SP))] for y in range(len(Z))]

for i in range(len(Z)) :
    for j in range(len(SP)) :
        if FRK_feeder_list[i][j] != []:
            FRK_fdm_list[i][j] =   mg[i][int(FRK_feeder_list[i][j].replace('F',''))-1]

### FRK_fdm_list 출력. 분기점을 감당하는 연계피더의 마진용량 리스트 생성
df = pd.DataFrame(FRK_fdm_list, columns =  ['F1','F2','F3','F4','F5'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'])
print(df)




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


###ZRI_list 출력
df = pd.DataFrame(ZRI_list, columns = ['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'])
print(df)



### FRK_fdm_list 출력. 분기점을 감당하는 연계피더의 마진용량 리스트 생성
df = pd.DataFrame(FRK_fdm_list, columns =  ['F1','F2','F3','F4','F5'], 
                                index=['Z1','Z2','Z3','Z4','Z5','Z6','Z7','Z8','Z9','Z10','Z11','Z12','Z13','Z14','Z15','Z16','Z17','Z18','Z19','Z20','Z21'])
print(df)


#############################################################################################

#scaler = MinMaxScaler()

#scaler.fit(ZRI_list[])
#ZRI_list_scaled = scaler.transform(ZRI_list)

#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#print(ZRI_list_scaled)

