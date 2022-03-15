# 2606_바이러스 풀이
# 2022-03-15


def dfs(v):                 # v: 출발점
    global visited
    visited[v] = True       # 출발점 방문 표시

    for n in graph[v]:      # v에서 갈 수 있는 경로 탐색
        if not visited[n]:  # 방문한 적이 없으면,
            dfs(n)          # 더 깊이 들어가 !


N = int(input())  # N: 노드의 개수
M = int(input())  # M: 간선의 개수
graph = [[] for _ in range(N+1)]  # graph[n] : n번 노드가 갈 수 있는 경로
visited = [False] * (N+1)   # 방문 기록

# 양방향 연결 정보 받아오기
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


dfs(1)
print(visited.count(1)-1)  # 1번 컴퓨터는 제외하므로, -1