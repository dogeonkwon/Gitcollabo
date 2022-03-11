# 1260_DFS와-BFS 풀이
# 2022-03-10
from collections import deque


def dfs(start_node, visited):
    global result_d
    global graph

    visited[start_node] = True     # 방문한 노드는 True 로 !
    result_d.append(start_node)    # 방문한 노드 차례대로 result_d에 추가

    for i in graph[start_node]:    # start_node에서 갈 수 있는 곳 탐색
        if not visited[i]:         # 만일 방문을 하지 않았다면
            dfs(i, visited)        # 깊이들어가 !


def bfs(start_node, visited):
    global result_b
    global graph
    queue = deque([start_node])  # 시작 노드를 큐에다가 먼저 삽입(삽입할 때 리스트[]로 감싸주기)
    visited[start_node] = True   # 시작 노드를 방문 처리

    while queue:
        start_node = queue.popleft()  # queue에서 노드를 pop
        result_b.append(start_node)   # 방문한 노드 result_b에 추가

        for i in graph[start_node]:   # start_node에서 갈 수 있는 곳 탐색
            if not visited[i]:        # 인접노드에 방문한 적 없을 때
                visited[i] = True     # 방문 표시
                queue.append(i)       # 큐에 방문기록 추가


N, M, V = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수, V: 탐색시작할 정점 노드
graph = [[] for _ in range(N+1)]

# 연결된 간선 받아오기
for m in range(M):
    i, n = map(int, input().split())
    graph[i].append(n)  # i는 n으로 갈 수 있음
    graph[n].append(i)  # n은 i로 갈 수 있음
    graph[i].sort()     # 정점 번호가 작은 것을 먼저 방문 >> 정렬
    graph[n].sort()
    visited_dfs = [0] * (N + 1)
    visited_bfs = [0] * (N + 1)

result_d = list()
dfs(V, visited_dfs)
print(*result_d)

result_b = list()
bfs(V, visited_bfs)
print(*result_b)