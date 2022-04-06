# 2644_촌수계산 풀이
# 2022-03-29

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
start, last = map(int, input().split())
m = int(input())
family = [[] for _ in range(N+1)]           # 촌수를 노드라고 생각하고 풀기
visited = [False for _ in range(N+1)]       # 방문한 노드인지 체크

for _ in range(m):                      # 양방향 노드
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

q = [(start, 0)]        # 시작지점과 지나온 간선의 개수를 q에 넣어준다.
visited[start] = True
front = result = -1     # 초기 result값은 -1(촌수 계산이 안 될 경우 -1을 출력해야함)
rear = 0

while front != rear:            # bfs를 활용하여 풀이
    if result > -1:
        break
    front += 1
    v = q[front]
    for i in family[v[0]]:
        if not visited[i]:
            visited[i] = True
            q.append((i, v[1]+1))   # 다음 탐색을 할 수 있도록 i(다음 갈 수 있는 노드)와 v[1]+1(지나온 간선 수)를 삽입
            rear += 1
            if i == last:           # i가 도착지점과 같다면 result에 v[1]+1을 저장해주고 종료
                result = v[1]+1
                break
print(result)




