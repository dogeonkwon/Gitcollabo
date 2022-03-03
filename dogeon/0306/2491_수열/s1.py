# 2491_수열 풀이
# 2022-03-05


N = int(input())
arr = list(map(int, input().split()))
result = sub = cnt = cnt2 = 0

for i in range(N-1):            # 전의 값보다 작거나 크다면 1을 더하고 계속 지속된다면 또 1을 더한다.
    if arr[i] <= arr[i+1]:      # 그러다 커지거나 작아지는 흐름이 변경된다면 다시 0으로 초기화 시켜준다.
        cnt += 1
    else:
        cnt = 0
    if arr[i] >= arr[i+1]:
        cnt2 += 1
    else:
        cnt2 = 0
    if cnt < cnt2:              # 초기화가 되기 전에 매번 가장 큰 수를 따로 저장해준다.
        sub = cnt2
    else:
        sub = cnt
    if result < sub:
        result = sub

print(result+1)         # 자기 자신을 포함하여 카운트를 해야하기 때문에 마지막에 더하기 1을 해준다.