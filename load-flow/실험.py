import numpy as np
import pandas as pd

new_L = np.array((pd.read_csv('./new_L.csv')))

c = [[0 for j in range(new_L.shape[1]-1)] for i in range(new_L.shape[0])] #2차원 배열 선언

for i in range(0,new_L.shape[0]): #row
    for j in range(1,new_L.shape[1]): #col