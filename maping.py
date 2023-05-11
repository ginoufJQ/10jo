

# # def in_func():
# #     junc_x = input("분기점의 x좌표를 입력하세요: ")
# #     junc_y = input("분기점의 y좌표를 입력하세요: ")
# #     for x in range(row*2 + 1):
# #         if x == junc_x:
    
# #             for y in range(col*2 + 1):
# #                 if y > junc_y:
# #                 #분기점 y에 대한 if문 + else깔즤
# #                 map_list[x][y][0] = x
# #                 map_list[x][y][1] = y
# #                 for j in range(4): #select문으로 바꾸기
# #                     for k in 
# #                     if 
# #                     map_list[x][y][] = #select문 써서 j값에 따라 ~~를 입력하세요 하고 input함수로 받기
# #                 else:

# #         else:
# #             map_list[x][y][3] = 0

#----------------------------------------------------------------------------------


# # mf = '\u2610'
# # fd = '\u2610'
# # hline_fd = '\u2500'
# # vline_fd = '\u2502'
# # hline_load = '\u2500'
# # vline_load = '\u2502'
# # sw = '\u25CB'

row = int(input("Max number of row line: "))    #행의 최대 전선 개수 입력 (간단계통도에서 6)
col = int(input("Max number of column line: ")) #열의 최대 전선 개수 입력 (간단계통도에서 4)


jh = []  #빈 리스트 생성 #피더고, 전선이고, 개폐기고 하나하나 개별로 생각
               #후에 함수에 조건 적용하기 위해서 분기점도 하나의 좌표로 설정 -> row*2 + 1

for i in range(col*2):         #2차원 리스트 생성 #열의 개별 모든 개수 더하면 col*2
    second_dim = []
    for j in range(row*2 + 1):     #행의 개별 모든 개수 더하면 row*2+1
        third_dim = []
        for k in range(5):         #(x좌표, y좌표, 종류, 값, )을 담고있는 리스트 생성 후 초기값 0대입
            third_dim.append(0)
        second_dim.append(third_dim)
    jh.append(second_dim)

print(jh)                    #내가 원하는 정보들을 입력하기 위한 3차원 배열 생성완료


