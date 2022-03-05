import sys
sys.stdin = open('input.txt')

N = int(input())  # 1제곱미터 당 참외 갯수

arr = [list(map(int, input().split())) for _ in range(6)]

# 가로,세로 가장 긴 길이를 곱해서 큰 사각형 넓이를 구하고
# 잘려 있는 부분의 가로 세로 길이를 찾아서 작은 사각형 넓이를 구한 후,
# 둘을 빼면 참외밭의 넓이를 구할 수 있다.

maxl = 0 # 제일 긴 가로 길이
maxh = 0 # 제일 긴 세로 길이

for i in range(6):
    for j in range(6):
        if arr[i][0] <= 2:       # 가로 길이 탐색
            if arr[i][1] > maxl: # 가장 긴 가로 길이 구하기
                maxl = arr[i][1]
                maxl_idx = i     # 가장 긴 가로길이의 인덱스

        elif arr[i][0] > 2:      # 세로 길이 탐색
            if arr[i][1] > maxh: # 가장 긴 세로 길이 구하기
                maxh = arr[i][1]
                maxh_idx = i     # 가장 긴 세로길이의 인덱스

# 가장 긴 가로, 세로 인덱스에 +3 을 하면 잘린 부분의 가로 세로 인덱스를 알 수 있다.

# 만약 +3을 했을 때 인덱스를 넘지 않는다면 +3을 해서 찾고
if maxl_idx + 3 < 6:
    minl = arr[maxl_idx + 3][1]
# 인덱스를 넘는다면 -3을 하면 찾을 수 있다.
else:
    minl = arr[maxl_idx - 3][1]

if maxh_idx + 3 < 6:
    minh = arr[maxh_idx + 3][1]
else:
    minh = arr[maxh_idx - 3][1]

# 큰 사각형과 작은 사각형
small_sq = minl * minh
big_sq = maxl * maxh

result = N * (big_sq - small_sq)
print(result)
