# 2304_창고_다각형 풀이
# 2022-02-26


N = int(input())            # 막대 기둥의 개수
w = list()                  # 가로 번호
h = list()                  # 높이

for _ in range(N):
    sub = list(map(int, input().split()))
    w += [sub[0]]
    h += [sub[1]]

for i in range(N-1):                    # 높이와 가로 번호를 따로 모은 후 가로번호에 따라 오름차순 정렬해준다.
    for j in range(i, N):
        if w[i] > w[j]:
            w[i], w[j] = w[j], w[i]
            h[i], h[j] = h[j], h[i]

result = 0              # 결과값
v = h[0]                # 정방향에서 비교할 높이
k = w[0]                # 정방향에서 비교할 가로 번호
reverse_v = h[-1]       # 역방향에서 비교할 높이
reverse_k = w[-1]       # 역방향에서 비교할 가로 번호

if N <= 1:          # 기둥이 하나라면 그냥 높이만 더 해줌
    result += v

else:
    for n in range(1, N):               # 그 이상이라면 반복문을 통해 더 높은 값을 만나면 전의 (현재 가로번호-전의 가로번호(k)) x 전의 높이(v)를 해준다.
        if h[n] >= v:
            result += v * (w[n]-k)
            v = h[n]
            k = w[n]
        if n == N - 1:          # 만약 끝까지 갔다면 돌았던 것 중 가장 큰 기둥을 더해준다.
            result += v
            break

    for m in range(N-1, -1, -1):            # 정방향을 확인하였으면 역방향으로 돌아서 정방향과 같은 방식으로 더해준다.
        if h[m] >= reverse_v:
            result += reverse_v * (reverse_k-w[m])
            reverse_v = h[m]
            reverse_k = w[m]
        if w[m] == k:               # 하지만 제일 높은 기둥은 이미 추가하였으므로 따로 추가하지 않는다.
            break

print(result)