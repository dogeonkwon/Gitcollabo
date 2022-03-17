# 2606_바이러스 풀이
# 2022-03-20

from collections import deque

N = int(input())
M = int(input())
network = [[] for _ in range(N+1)]          # 네트워크 연결이 어디로 되어 있는지 확인
visited = [False] * (N+1)                   # 방문했는지 확인
result = 0

for _ in range(M):                          # 출발지 인덱스에 도착지 값을 넣어주는 작업
    sub = list(map(int, input().split()))
    network[sub[0]].append(sub[1])
    network[sub[1]].append(sub[0])

q = deque([1])
visited[1] = True
while q:                                # q가 빌때까지 반복(더 이상 갈 곳이 없다는 의미)
    v = q.popleft()
    for i in network[v]:                # 출발지로 갈 수 있는 곳을 탐색했을 때 간 적이 없는 곳이라면 True로 바꿔주고 결과값 + 1 을 해준다. 그리고 다음 탐색을 하기 위해 q에 추가한다.
        if not visited[i]:
            visited[i] = True
            result += 1
            q.append(i)

print(result)