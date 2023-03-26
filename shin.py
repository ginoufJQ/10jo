
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


        