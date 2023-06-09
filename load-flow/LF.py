#%%     Radial distribution network load flow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import cmath
from LFClasses import Branch 
from LFClasses import Bus 
#from LFClasses4 import Slack 

np.set_printoptions(precision=6, suppress=True) #과학적 표기법 무시!

#%%     Data reading 
Iine_Connectsions=np.array(pd.read_excel('load-flow/sb_busss.xlsx', sheet_name="Sheet1"))
Loads=np.array(pd.read_excel('load-flow/sb_busss.xlsx', sheet_name="Sheet2"))
Data_Settings=np.array(pd.read_excel('load-flow/sb_busss.xlsx', sheet_name="Sheet3"))

#%%     Initialization

Bus_numbers=Iine_Connectsions.shape[0]-1

DNBranch = [0 for x in range(0,Bus_numbers)]
DNBus = [0 for x in range(0,Bus_numbers)]

for BN in range(0,Bus_numbers):
    DNBranch[BN] = Branch (BN,Iine_Connectsions,Data_Settings)
    DNBus[BN] = Bus(BN,Loads,Data_Settings,Iine_Connectsions)

for BN in range(0,Bus_numbers):
    DNBus[BN].suppling_branch = DNBranch[BN]
    if DNBus[BN].suppling_branch.from_bus !=0:
        DNBus[BN].parent_bus = DNBus[DNBus[BN].suppling_branch.from_bus-1]
    else:
        DNBus[BN].parent_bus = Bus(0,Loads,Data_Settings,Iine_Connectsions) 
        
for BN in range(0,Bus_numbers):
    for A in range(0,Bus_numbers):
        if ((DNBus[A].suppling_branch.from_bus != 0) and (DNBus[A].suppling_branch.from_bus == BN+1)):
            DNBus[BN].children_buses.append (DNBus[A])
                
 #%%     Nodal current calculation
deviation = 1
deviation_max=0.0001
while deviation>deviation_max:
    deviation=0
    
    for BN in range (0,Bus_numbers):
        DNBus[BN].current = complex(0,DNBranch[BN].capacitaance*DNBus[BN].voltage)
        DNBus[BN].current += np.conj( DNBus[BN].injection/DNBus[BN].voltage)
        DNBranch[BN].current = DNBus[BN].current   
        
 #%%     Backward sweep—section current calculation
    for BN in  DNBus[: : -1]: 
        for cildbus in BN.children_buses:
            BN.suppling_branch.current += cildbus.suppling_branch.current            
      
 #%%     Forward sweep—nodal voltage calculation
    for BN in  DNBus:
       BN.voltage=BN.parent_bus.voltage-BN.suppling_branch.current*BN.suppling_branch.impedance
                  
 #%%     Convergence Criterion 
    for BN in  DNBus:
        deviation += abs(BN.voltage-BN.previous_voltage)
        BN.previous_voltage=BN.voltage
        
    # print(deviation)
        
 #%%     Post-processing 

CC = np.array([abs(DNBranch[x].current) for x in range(0,Bus_numbers)])*1000000/13200
VV = np.array([abs(DNBus[x].voltage) for x in range(0,Bus_numbers)])*13200

print( "=========위배한 것들, 전류전압순===============" )
print(CC[CC > 352])
print(VV[VV < 0.95*13200])

if len(CC[CC > 352]) | len(VV[VV < 0.95*13200]) != 0:
    print("제약조건 이탈!")
    #위배 있을 경우

else:
    print("이상없음")
    #위배 없는 경우

print( "==========조류해석 결과, 전류전압순================" )
print (pd.DataFrame(CC))
print (pd.DataFrame(VV))

plt.scatter( range(0,Bus_numbers),VV)
plt.xlabel('bus')
plt.ylabel('Voltage')
plt.title('Voltage')
plt.axhline(13200*0.95, 0, 1, color='red', linestyle='--', linewidth=2)
plt.ylim([13200*0.93, 13200])
plt.show()

plt.scatter( range(0,Bus_numbers),CC)
plt.xlabel('br')
plt.ylabel('Current')
plt.title('Current')
plt.ylim([0, 352*1.05])
plt.axhline(352, 0, 1, color='red', linestyle='--', linewidth=2)
plt.show()

#%% 배열합
print(Iine_Connectsions[3]**2 + Iine_Connectsions[4]**2)
print(sum(CC*np.sqrt( Iine_Connectsions[3]**2 + Iine_Connectsions[4]**2)))