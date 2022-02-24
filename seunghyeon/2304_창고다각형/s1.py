# 2304_창고다각형 풀이
# 2022-02-26

N = int(input())     # N: 막대 기둥
left = [0] * N       # left: 왼쪽면의 위치 모으기
height = [0] * N     # height: 높이 모으기

# L, H: 위치와 높이를 받아 모두 모아준다.
for n in range(N):
    L, H = map(int, input().split())
    left[n] = L
    height[n] = H

# 높이와 위치를 묶어줌
area = list(map(list, zip(left, height)))

# 위치에 따라 정렬해줘 !
for n in range(N, -1, -1):
    for m in range(n - 1):
        if area[m][0] > area[m + 1][0]:
            area[m], area[m + 1] = area[m + 1], area[m]

# 제일 높은 건물 인덱스 찾기 !
maxI = 0
for n in range(N):
    if area[maxI][1] < area[n][1]:
        maxI = n

# 제일 높은 건물을 기준으로 왼쪽 오른쪽 나눈다 !
# 왼쪽일 때, 다음 건물의 높이가 현재 건물의 높이보다 작으면
# 현재 건물의 높이로 바꿔줌 >> 물이 고일수 없으니까 !
for n in range(maxI-1):
    if area[n][1] > area[n + 1][1]:
        area[n + 1][1] = int(area[n][1])

# 뒤에서부터 탐색
# 내 앞의 건물이 내 건물보다 낮으면, 내 건물 높이로 바꿔줌 !
for n in range(N - 1, maxI + 1, -1):
    if area[n][1] > area[n - 1][1]:
        area[n - 1][1] = int(area[n][1])


# 결과를 구한다 !
# 가장 높은 건물의 값을 결과의 초기값으로 정해줌
result = area[maxI][1]
i = 0
while i < maxI:
    result += (area[i + 1][0] - area[i][0]) * area[i][1]
    i += 1

i = N - 1
while i > maxI:
    result += (area[i][0] - area[i - 1][0]) * area[i][1]
    i -= 1

print(result)
