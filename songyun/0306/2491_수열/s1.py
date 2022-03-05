N = int(input())
num = list(map(int, input().split()))

# 연속으로 커지거나 작아지는 구간을 찾아야 한다.
cnt = 1
max_1 = 1

# 작아지는 수열
for i in range(1, N):

    # 만약 현재 숫자가 바로 전 숫자보다 작거나 같다면 카운트 +1
    if num[i-1] >= num[i]:
        cnt += 1
    # 커진다면 카운트를 1로 초기화
    else:
        cnt = 1
    # 카운트를 max로 갱신
    if max_1 < cnt:
        max_1 = cnt

# 커지는 수열
cnt = 1
for i in range(1, N):
    # 만약 이전 숫자보다 현재 숫자가 더 커진다면
    if num[i-1] <= num[i]:
        cnt += 1
    # 작아진다면 1로 초기화
    else:
        cnt = 1
    # cnt가 max값을 넘는다면 갱신
    if max_1 < cnt:
        max_1 = cnt

print(max_1)
