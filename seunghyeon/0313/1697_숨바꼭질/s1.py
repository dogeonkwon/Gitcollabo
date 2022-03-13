# BOJ_1697_숨바꼭질
# 2022-03-12

from collections import deque

N, M = map(int, input().split())    # N: start, M: end
cnt = 0                 # 횟수
find = 0                # 찾으면 멈춰줘 !
queue = deque([[N]])    # 시작
visit = [0] * 150000    # 방문확인

while queue and N != M:
    start = queue.popleft()   # 시작노드 빼오기
    cnt += 1                  # 횟수세기
    v = list()                # 시작노드에서 갈수있는 곳 담을 공간

    for s in start:           # start 노드가 여러개 !
        for n in [s+1, s-1, s*2]:   # s가 갈 수 있는 곳: s-1, s+1, s*2
            if n == M:              # 찾으면 멈춰줘 !
                find = 1
                break
            if 0 <= n < 150000 and visit[n] == 0:   # 방문안했으면 방문해줘 !
                v.append(n)
                visit[n] = 1
                continue

        if find == 1:
            break

    if find == 1:
        break

    queue.append(v)    # 다 방문했으면 멈춰줘 !

print(cnt)
