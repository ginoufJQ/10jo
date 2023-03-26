import pandas as pd
import numpy

#용량 입력
Z = [1000,
     500,
     1000,
     500,
     1000,
     1500]
FTL = [sum(Z),
       8500,
       9500]
FM = 14000
FRK = ["Z3"]

for i in range(0,7):
    globals()["Z{}".format(i)]=Z[i-1]

for i in range(0,4):
    globals()["FM{}".format(i)]=FM

for i in range(0,4):
    globals()["FTL{}".format(i)]=FTL[i-1]

for i in range(0,4):
    globals()["F{}".format(i)]=FM-FTL[i-1]

#문자열과 변수명 스위칭 << 변수명으로 된 리스트를 생성하여 거리 산정에 이용할 생각
list = ["Z1", "Z2"]
print(globals()[list[0]])

#Z1에서 고장 발생
#메인 피더 끊김
#연계 계통 연결
#연계 피더가 각 부하의 거리를 산정
#위 값을 비교하여 큰 값을 RSI로 산정