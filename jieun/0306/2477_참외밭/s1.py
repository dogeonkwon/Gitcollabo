import sys
sys.stdin = open('input.txt','r')

# 1m2 당 참외 갯수 가져오기
K = int(input())
# 6각형이니까 6번만 가져오면 됨
T = 6
len_list= []
for t in range(T):
    # 방향과 길이 받아오기
    direction, length = list(map(int, input().split()))
    len_list.append(length)

# 큰 상자와 작은 상자 구하기(이때 small이 무조건 min은 아님)
big = 0
small = 0
# 6번 진행할건데
for i in range(6):
    # 각 변과 인접한 변의 곱을 구해서 면적 구하기
    area = len_list[i] * len_list[(i+1) % 6]
    # 가장 큰 면적과 그 변의 위치 구하기
    if big < area:
        big = area
        idx = i
# 작은 상자 구하기 항상 3, 4칸 떨어져있음
small = len_list[(idx +3) % 6] * len_list[(idx +4) %6]
# 답구하기
ans = K * (big - small)
print(ans)
