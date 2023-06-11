import pandas as pd

sum = 0
FP = 0
FRK = 0


Z = [100,200,300,400,500,600,700,100,200,300,400,500,600,700,100,200,300,400,500,600,700]
del sum
FTL = [14000, 10000,9000,8000,7000] ### F1 말단이라 여유용량 0
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

# 빈 리스트 생성. 리스트는 Z1~Z6 6개, 6*6 리스트 생성
ZRI_list = []
ZRI_list2 = []

for r in range(len(Z)):
    line = []
    for s in range( len(Z)):
        line.append([])
    ZRI_list.append(line)
    ZRI_list2.append(line)

new_L = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))]



#print(*ZRI_list, sep='\n')
# 빈 리스트 생성, F1~F8





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
                new_L[b-1][f-1][int(new_col)-1].append( globals()["ZRI_" + "F" + str(f) + "_{}".format(globals()["L"+str(f)] [l])])    

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
      ZRI_list2[n][m] = [max(ZRI_list[n][m])]
    else:
      ZRI_list[n][m] = []
      ZRI_list2[n][m] = []



#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#print(*ZRI_list, sep='\n')

#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#print(*new_L, sep='\n')

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


FRK_list= []
for N in range( len(SP) ):
        FRK_list.append([])

for i in range(1 ,len(SP)+1) :
    intersection = [x for x in globals()['L' + str(i)] if x in L]  # L이랑 L1~L8 안의 값을 차례대로 비교를 할껀데, 가장 먼저 겹치는 게 F1~F8의 분기점임!!!! 
    FRK_list[i-1].append(intersection[0]) ###리스트에 값 입력

###FRK_list 출력. 연계피더의 분기점 리스트 생성



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






FRK_fdm_list=  [[[] for x in range(len(SP))] for y in range(len(Z))]

for i in range(len(Z)) :
    for j in range(len(SP)) :
        if FRK_feeder_list[i][j] != []:
            FRK_fdm_list[i][j] =   mg[i][int(FRK_feeder_list[i][j].replace('F',''))-1]

### FRK_fdm_list 출력. 분기점을 감당하는 연계피더의 마진용량 리스트 생성




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





#####################################################선로증설############################################


flow = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))]
# mg = []

for e in range(1, len(Z)+1):
   for k in range(1, len(SP)+1):
      for g in range(1, len(Z)+1):
         for h in new_L[e-1][k-1][g-1]:
            if h in ZRI_list[e-1][g-1]:
                mg[e-1][k-1].append(h)
                flow[e-1][k-1][g-1].append(h)
            else :
               pass

for len1 in range(1,len(mg)+1):
  for len2 in range(1, len(mg[len1-1])+1):
    if mg[len1-1][len2-1]:
      mg[len1-1][len2-1] = [min(mg[len1-1][len2-1])]
    else:
      mg[len1-1][len2-1] = [globals()['F' + str(len2)]]


UR_ZRI = [] # 복구불가능지점의 ZRI의 값
UR_L = [[ [] for col2 in range(len(Z))] for row2 in range(len(Z))] # 복구불가능지점 부하량

new_ZRI = 0 # 복구불가능지점의 새로운 ZRI 값
new_ZRI_list = [[[ [] for col3 in range(len(Z))] for row3 in range(len(SP))] for depth3 in range(len(Z))] # 복구불가능지점에 대한 각 고장점과 연계피더에 대한 ZRI 값이 담긴 list 
new_ZRI_UR_L_list = [[[ [] for col4 in range(len(Z))] for row4 in range(len(SP))] for depth4 in range(len(Z))] 
new_ZRI_list2 = [[[ [] for col5 in range(len(Z))] for row5 in range(len(SP))] for depth5 in range(len(Z))]

for p in range(1, len(Z)+1):   
  for q in range(1, len(Z)+1):
     if ZRI_list[p-1][q-1]:
        if ZRI_list[p-1][q-1] < [0]:
          UR_ZRI.append((p, q, ZRI_list[p-1][q-1])) # ZRI_list에서 음수인 값을 찾아서 UR_ZRI 리스트에 인덱스값과 해당 음수값을 저장
          UR_L[p-1][q-1].append(globals()['Z'+str(q)]) # 복구불가능지점의 부하량을 고장점별로 UR_L 리스트에 저장
        else:
          pass
     else:
        pass

    

     
# mg_value  연계피더 값
# UR_L_value 복구불가능지점 부하량


for b1 in range(1, len(Z)+1):  #고장점 1~12에서 고장날 때
    for f1 in range(1,len(SP)+1) : 
      mg_value = mg[b1-1][f1-1] #연계피더 1~8 값 중 하나 선택
      for l1 in range(1,len(Z)+1):
        UR_L_value = UR_L[b1-1][l1-1] #복구불가능지점 부하량 리스트에서 부하량 하나 선택
        if UR_L[b1-1][l1-1]: #만약 복구불가능지점이라면 (리스트에 값이 있다면)
          new_ZRI = mg_value[0] - UR_L_value[0] # 앞에서 선택한 mg_value 값에서 UR_L_value 값 빼기 (연계피더 - 복구불가능지점 부하량)
          new_ZRI_list[b1-1][f1-1][l1-1].append(new_ZRI) # 이것을 new_ZRI_list 리스트에 저장
          new_ZRI_list2[b1-1][f1-1][l1-1].append(new_ZRI)
          new_ZRI_UR_L_list[b1-1][f1-1][l1-1].append(new_ZRI) # 복구 불가능지점의 ZRI만 따로 볼려고 만듦
        else:          # 만약 복구불가능지점이 아니라면 원래 ZRI 값을 리스트에 저장
          if ZRI_list[b1-1][l1-1] == []: 
            pass
          else:
            new_ZRI_list[b1-1][f1-1][l1-1].append(ZRI_list[b1-1][l1-1][0])      
            new_ZRI_list2[b1-1][f1-1][l1-1].append(ZRI_list[b1-1][l1-1][0])   




##############################################정규화(f3)#############################

for p in range(1, len(Z)+1):   
  for q in range(1,len(SP)+1) : 
      new_ZRI_list2[p-1][q-1] = [[0]  if x==[] else x for x in new_ZRI_list2[p-1][q-1]] # min max 값 찾기 위해 []인 값을 모두 [0]으로 만들어 new_ZRI_list2에 넣기
      ZRI_list2[p-1] = [[0]  if x==[] else x for x in ZRI_list2[p-1]]  #min max 값 찾기 위해 []인 값을 모두 [0]으로 만들어 ZRI_list2에저장                                                                 


min_val = min([min([min(i) for i in j]) for j in new_ZRI_list2])[0] #new_ZRI_list2에서 min 값 찾기
max_val = max([max([max(i) for i in j]) for j in new_ZRI_list2])[0] #new_ZRI_list2에서 max 값 찾기
norm_new_ZRI_list = [[[ [] for col6 in range(len(Z))] for row6 in range(len(SP))] for depth6 in range(len(Z))] #min max 정규화 리스트

min_val1 = min([min(x) for x in ZRI_list2])[0] #ZRI_list2에서 min 값 찾기
max_val1 = max([max(x) for x in ZRI_list2])[0] #ZRI_list2에서 max 값 찾기
norm_ZRI_list = [[ [] for col7 in range(len(Z))] for row7 in range(len(Z))] # min max 정규화 리스트


for p1 in range(1, len(Z)+1):  
  for q1 in range(1, len(SP)+1): 
    for r1 in range(1, len(Z)+1):
      if new_ZRI_list[p1-1][q1-1][r1-1] == []:  #만약 new_ZRI_list 값이 []이면 계산 안함
          pass
      else:
          x = new_ZRI_list[p1-1][q1-1][r1-1][0]    #new_ZRI_list 값이 있으면 정규화 함
          norm_new_ZRI_list[p1-1][q1-1][r1-1].append((x - min_val) / (max_val - min_val)) #계산된 정규화 값 norm_new_ZRI_list에 넣기

for p2 in range(1, len(Z)+1):  
    for r2 in range(1, len(Z)+1):
      if ZRI_list[p2-1][r2-1] == []:  #만약 ZRI_list 값이 []이면 계산 안함
          pass
      else:
          x1 = ZRI_list[p2-1][r2-1][0]    #ZRI_list 값이 있으면 정규화 함
          norm_ZRI_list[p2-1][r2-1].append((x1 - min_val1) / (max_val1 - min_val1)) #계산된 정규화 값 norm_ZRI_list에 넣기






################################# 목적함수F ####################################

#####고장취약지점에서 어떤 고장점에서 고장이 났을 때 ZRI가 더 적은지##### 그때 고장지점이랑 고장취약지점 구함

UR_list = [] #고장취약지점리스트 (중복있음)
UR = [] #고장취약지점 (중복없음)

UR_ZRI_min_list = [[[] for x in range(len(Z))] for y in range(len(Z))] # 고장이 났을 때 고장취약구간의 모든 ZRI 나타냄 (0 포함 : min 구하기 위해서)
UR_ZRI_min = [] # 고장취약구간의 ZRI 중 가장 작은 값 
UR_ZRI_min_inf_list = []


for p in range(1,len(UR_ZRI)+1):
    UR_list.append(UR_ZRI[p-1][1])
    UR = list(set(UR_list)) 

for r in range (1, len(Z)+1):
    for q in range(1, len(UR)+1):
        UR_ZRI_min_list[UR[q-1]-1][r-1].append(ZRI_list2[r-1][UR[q-1]-1])
        if UR_ZRI_min_list[UR[q-1]-1][r-1] == []:
           pass
        else:
           UR_ZRI_min = [min(row) for row in UR_ZRI_min_list] 

for r in range (1, len(Z)+1):
    for q in range(1, len(UR)+1):
        if UR_ZRI_min[UR[q-1]-1][0] == UR_ZRI_min_list[UR[q-1]-1][r-1][0]:
           UR_ZRI_min_inf_list.append((r, UR[q-1])) #고장점, 취약구간 ##[((2, 3), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7))]
        else:
           pass

UR_ZRI_min_inf = []
for item in UR_ZRI_min_inf_list:
    if item[1] not in [x[1] for x in UR_ZRI_min_inf]:
        UR_ZRI_min_inf.append(item) #(고장점, 취약구간) ##[(2,3), (2,7)] 로 같은 ZRI(최소 ZRI)를 가지는 취약구간 제거

#################################목적함수######################################


######### 선로증설X ##########
f1_1 = 0
f2_1 = 0
w1 = 0.3
w2 = 0.7 #0.5
w3 = 0.8 #0.9

F1 = [[] for x in range(len(Z))]  #선로증설안했을때목적함수

for b in range(1, len(UR_ZRI_min_inf)+1):
    f3_1 = norm_ZRI_list[UR_ZRI_min_inf[b-1][0]-1][UR_ZRI_min_inf[b-1][1]-1][0]
    F1[UR_ZRI_min_inf[b-1][1]-1].append(-(f1_1*w1) -(f2_1*w2) +(f3_1*w3))



################ 선로증설O ########################
f3_2_list = [[[] for x in range(len(Z))] for y in range(len(Z))]
f3_2_list2 = [[[] for x in range(len(Z))] for y in range(len(Z))]
f3_2_list3 = [[[] for x in range(len(Z))] for y in range(len(Z))]

for d in range(1, len(UR_ZRI_min_inf)+1):
    for c in range(1, len(SP)+1):
        f3_2_list[UR_ZRI_min_inf[d-1][0]-1][UR_ZRI_min_inf[d-1][1]-1].append(norm_new_ZRI_list[UR_ZRI_min_inf[d-1][0]-1][c-1][UR_ZRI_min_inf[d-1][1]-1][0])

for d in range(1, len(UR_ZRI_min_inf_list)+1):
    for c in range(1, len(SP)+1):
        f3_2_list2[UR_ZRI_min_inf_list[d-1][0]-1][UR_ZRI_min_inf_list[d-1][1]-1].append((c,norm_new_ZRI_list[UR_ZRI_min_inf_list[d-1][0]-1][c-1][UR_ZRI_min_inf_list[d-1][1]-1][0]))
        f3_2_list3[UR_ZRI_min_inf_list[d-1][0]-1][UR_ZRI_min_inf_list[d-1][1]-1].append(norm_new_ZRI_list[UR_ZRI_min_inf_list[d-1][0]-1][c-1][UR_ZRI_min_inf_list[d-1][1]-1][0])

for n in range(len(f3_2_list)):
  for m in range(len(f3_2_list[n])):
    if f3_2_list[n][m]:
      f3_2_list[n][m] = [max(f3_2_list[n][m])]
    else:
      f3_2_list[n][m] = []

for n in range(1, len(Z)+1):
  for m in range(1, len(Z)+1):
      if f3_2_list3[n-1][m-1]:
        f3_2_list3[n-1][m-1] = [max(f3_2_list3[n-1][m-1])]
      else:
        f3_2_list3[n-1][m-1] = []
 

feeder_max = [[] for x in range(len(Z))]  # 선로 증설하는데 선택된 연계피더 리스트 (취약구간에 대해서)
feeder_max_inf = [[] for x in range(len(Z))] 
feeder_max_inf_2 = [[[] for x in range(len(Z))] for y in range(len(Z))] 
new_flow = [] # 선로 증설 후 각 연계피더가 담당하는 부하

for n in range(1, len(Z)+1):
  for m in range(1, len(Z)+1):
    for o in range(1, len(SP)+1):
        if f3_2_list3[n-1][m-1]:
            if f3_2_list3[n-1][m-1][0] == f3_2_list2[n-1][m-1][o-1][1]:
                feeder_max_inf_2[n-1][m-1].append((mg[n-1][o-1][0], f3_2_list2[n-1][m-1][o-1][0]))
            else:
                pass
        else:
            pass

for n in range(1, len(Z)+1):
  for m in range(1, len(Z)+1):
    for o in range(1, len(SP)+1):
        if f3_2_list[n-1][m-1]:
            if f3_2_list[n-1][m-1][0] == f3_2_list2[n-1][m-1][o-1][1]:
              feeder_max[m-1].append(f3_2_list2[n-1][m-1][o-1][0])
              feeder_max_inf[m-1].append((mg[n-1][o-1][0], f3_2_list2[n-1][m-1][o-1][0]))
            else:
               pass
        else:
            pass


new_flow = [[[ [] for col in range(len(Z))] for row in range(len(SP))] for depth in range(len(Z))] # # 뉴복지에서 각 연계피더가 담당하는 부하 (고장점마다 연계피더가 담당하는 부하량)


for i in range(1, len(Z)+1):
  for j in range(1, len(SP)+1):
     for k in range(1, len(Z)+1):
          if flow[i-1][j-1][k-1] == []:
             pass
          else:
             if flow[i-1][j-1][k-1] < [0] : 
              new_flow[i-1][feeder_max_inf_2[i-1][k-1][0][1]-1][k-1].append(feeder_max_inf_2[i-1][k-1][0][0] - abs(flow[i-1][j-1][k-1][0]))
             else:
              new_flow[i-1][j-1][k-1].append(flow[i-1][j-1][k-1][0])
           

    
f1_2 = 0
f2_2 = 1
F2 = [[] for x in range(len(Z))]  #선로증설했을때목적함수


for b in range(1, len(UR_ZRI_min_inf)+1): 
        f3_2 = norm_new_ZRI_list[UR_ZRI_min_inf[b-1][0]-1][feeder_max[UR_ZRI_min_inf[b-1][1]-1][0]-1][UR_ZRI_min_inf[b-1][1]-1][0]
        F2[UR_ZRI_min_inf[b-1][1]-1].append((-f1_2*w1) -(f2_2*w2) +(f3_2*w3))


###########################################최종 F 구하기#########################################################
F = [[] for x in range(len(Z))] #최종F, 선로증설여부


for i in range (1, len(Z)+1):
      if F1[i-1] == F2[i-1]:
         pass
      else:
        if F1[i-1] > F2[i-1]:
            F[i-1].append(("선로증설안함", F1[i-1][0]))
        else:
            F[i-1].append(("선로증설함", F2[i-1][0], feeder_max[i-1][0]))




#####################################출력###############################
print(F1)
print(F2)
print(F)