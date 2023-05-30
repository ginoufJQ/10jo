import matplotlib.pyplot as plt

# 그림 창 생성
plt.figure()
ax = plt.gca()
# x 축의 범위를 0에서 까지로 지정 #행, 열 값을 받아와서 설정 
plt.xlim(-1, 5)
# y 축의 범위를 0에서 까지로 지정
plt.ylim(-1, 5)

# 좌표와 대응하는 요소
x_coords = [1, 2, 3, 4]
y_coords = [1, 2, 3, 4]
labels = ['A', 'B', 'C', 'D']

# 주석을 저장할 변수
annotations = []

# hovering annotation 추가 함수
def add_hovering_annotation(event):
    if event.inaxes == ax:
        # 모든 주석을 숨김
        for annotation in annotations:
            annotation.set_visible(False)

        for x, y, label in zip(x_coords, y_coords, labels):
            if x-0.3 <= event.xdata <= x+0.3 and y-0.3 <= event.ydata <= y+0.3:
                annotation = ax.annotate(f"{label}", xy=(x, y), xytext=(x+0.5, y+0.5),
                                         arrowprops=dict(facecolor='black', arrowstyle='->'))
                annotation.set_visible(True)  # 해당 주석을 표시
                annotations.append(annotation)
        plt.draw()

# 이벤트 처리 함수 연결
plt.connect('motion_notify_event', add_hovering_annotation)  # 커서 가져다 대면 hovering annotation 표시

# 그림 창 표시
plt.show()





