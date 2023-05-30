import pandas as pd


sum = 0
FP = 0
FRK = 0


#용량 입력
Z = [500,500,5000,700,1200,1100,600,1000,500,900,700,800] # Z3=1000 값을 Z3=5000으로 바꿔서 해봄
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


#####################################################선로증설

mg = [[[] for x in range(len(SP))] for y in range(len(Z))]
# mg = []

for e in range(1, len(Z)+1):
   for k in range(1, len(SP)+1):
      for g in range(1, len(Z)+1):
         for h in new_L[e-1][k-1][g-1]:
            if h in ZRI_list[e-1][g-1]:
                mg[e-1][k-1].append(h)
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
          UR_ZRI.append(ZRI_list[p-1][q-1]) # ZRI_list에서 음수인 값을 찾아서 UR_ZRI 리스트에 인덱스값과 해당 음수값을 저장
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
          


""" print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*mg, sep='\n')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(*UR_L, sep='\n')

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

for i0 in range(len(new_ZRI_list)): #3차원 리스트인 new_ZRI_list 줄바꿔서 출력,,
   for j0 in range(len(new_ZRI_list[i0])):
      print(new_ZRI_list[i0][j0])
   print() 

print("---------------------")

for i0 in range(len(new_ZRI_list2)): #3차원 리스트인 new_ZRI_list 줄바꿔서 출력,,
   for j0 in range(len(new_ZRI_list2[i0])):
      print(new_ZRI_list2[i0][j0])
   print()       """




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





#########결과값 출력############
print("--------------------")
print(*ZRI_list, sep='\n') #고복지 값

print("--------------------")
print(*norm_ZRI_list, sep='\n') #고복지 정규화 값

print("--------------------")
for i0 in range(len(new_ZRI_list)): #3차원 리스트인 new_ZRI_list 줄바꿔서 출력
   for j0 in range(len(new_ZRI_list[i0])):
      print(new_ZRI_list[i0][j0])
   print()


print("--------------------")
for i0 in range(len(norm_new_ZRI_list)): #3차원 리스트인 norm_new_ZRI_list 줄바꿔서 출력 (정규화)
   for j0 in range(len(norm_new_ZRI_list[i0])):
      print(norm_new_ZRI_list[i0][j0])
   print() 


