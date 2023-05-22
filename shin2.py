import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tips =

# 등고선 시각화
fig, ax = plt.subplots()  # 수정된 부분
sns.kdeplot(data=tips, x='total_bill', y='tip', shade=True, ax=ax)  # 수정된 부분
ax.set_title('Kernel Density Plot')

# x축과 y축의 범위 설정
plt.xlim(0, 5)
plt.ylim(10, 30)

# 그래프 표시
plt.show()














###########################

from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt

# 이미지 로드
image = Image.open("C:/Users/신소범/Desktop/전기공학종합설계/IEEE.JPG")

# 흑백 이미지로 변환
image_gray = image.convert("L")

# 이미지 데이터 추출
data = list(image_gray.getdata())

# 데이터를 2D 형식으로 변환
data_2d = np.reshape(data, (image.height, image.width))

# Heatmap 생성
sns.heatmap(data_2d, cmap='hot', cbar=False)

# 그래프 표시
plt.show()


import geopandas as gpd

# 인구밀도 데이터 로드
population_data = gpd.read_file("C:/Users/신소범/Desktop/전기공학종합설계/광주인구밀도/AL_29_D164_20230125.shp")

# 이미지와 인구밀도 데이터 조합
merged_data = gpd.sjoin(population_data, image, how='inner', op='intersects')

import seaborn as sns
import matplotlib.pyplot as plt

# 인구밀도를 기반으로 Heatmap 생성
ax = plt.subplots()
ax = sns.kdeplot(data=merged_data, x='x', y='y', weights='인구밀도', shade=True)
ax.set_title('Population Density Heatmap')

# 그래프 표시
plt.show()




##단순한 히트맵...


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터프레임 생성
data = {
    'x': [10, 20, 30, 40, 50],
    'y': [5, 10, 15, 20, 25],
    'population': [1000, 500, 2000, 1500, 3000]
}

df = pd.DataFrame(data)

# 피벗 테이블 생성
pivot_table = df.pivot('y', 'x', 'population')

# 열 지도 생성
sns.heatmap(data=pivot_table, cmap='YlGnBu', annot=True, fmt='g')

# 그래프 표시
plt.show()





########왜안겹쳐져~~


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# 데이터프레임 생성
data = {
    'x': [10, 20, 30, 40, 50],
    'y': [5, 10, 15, 20, 25],
    'population': [1000, 500, 2000, 1500, 3000]
}
df = pd.DataFrame(data)

# 피벗 테이블 생성
pivot_table = df.pivot('y', 'x', 'population')

# 이미지 로드
image_path = "C:/Users/신소범/Desktop/전기공학종합설계/IEEE.JPG"  # 이미지 파일 경로
image = Image.open(image_path)
resized_image = image.resize((100, 50))  # 이미지의 크기를 (300, 200)으로 리사이징

# 이미지와 히트맵 겹치기
fig, ax = plt.subplots(figsize=(10, 6))  # figsize로 크기 조절
ax.imshow(image)

# 히트맵 생성
sns.heatmap(data=pivot_table, cmap='coolwarm_r', annot=True, fmt='g', alpha=0.5, ax=ax)

# 축 설정
ax.set_xlim(0, image.size[0])
ax.set_ylim(image.size[1], 0)
ax.axis('off')

# 그래프 표시
plt.show()


###########################



import numpy as np
import matplotlib.pyplot as plt

# 2차원 그리드 데이터 생성
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 색상을 나타내는 Z 데이터 생성
Z = np.sin(np.sqrt(X**2 + Y**2))

# 등고선 그래프 그리기
plt.imshow(Z, cmap='viridis', extent=[-5, 5, -5, 5], origin='lower')

# 컬러바 추가
cbar = plt.colorbar()
cbar.set_label('Value')

# 그래프 표시
plt.show()



###########################
import numpy as np
import matplotlib.pyplot as plt

# 리스트 데이터 생성
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
values = np.sin(x[:, np.newaxis]) + np.cos(y)

# 등고선 그래프 그리기
plt.imshow(values, cmap='viridis', extent=[min(x), max(x), min(y), max(y)], origin='lower')

# 컬러바 추가
cbar = plt.colorbar()
cbar.set_label('Value')

# 그래프 표시
plt.show()






###########################


#산점도



import numpy as np
import matplotlib.pyplot as plt

# 전력계통 좌표
x = [1, 2, 3, 4, 5]
y = [2, 2, 2, 4, 2]

# 고장취약성 데이터
vulnerability = [-1400, 500, 400, 4500, 3000]

# 고장취약성에 따른 색상 지정
colors = vulnerability


# 점의 가장자리 색상 지정
edge_colors = 'none'

# 산점도 플롯 그리기
plt.scatter(x, y, c=colors, cmap='viridis', s=1000, alpha=0.5, edgecolors=edge_colors)

# 색상 막대 표시
plt.colorbar()


# x축과 y축의 범위 설정
plt.xlim(0, 10)  # x축의 범위를 0부터 60까지로 설정
plt.ylim(0, 15)  # y축의 범위를 0부터 10까지로 설정


# 그래프 표시
plt.show()




