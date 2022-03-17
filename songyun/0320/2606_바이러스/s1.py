import sys
sys.stdin = open('input.txt')

def DFS(graph, s, visited):

    # 시작점은 True
    visited[s] = True

    # 현재 컴퓨터와 연결된 컴퓨터를 i 에 넣는다.
    for i in graph[s]:
        # 처음 방문하는 컴퓨터라면
        if not visited[i]:
            # 방문했다고 표시하고
            visited[i] = True
            # 다시 탐색한다.
            DFS(graph, i, visited)

    return visited

# 컴퓨터의 갯수
N = int(input())

# 간선의 갯수
M = int(input())

# 연결 상태를 담을 리스트
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = list(map(int, input().split()))

    graph[a].append(b)
    graph[b].append(a)

    # graph : [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

    visited = [False] * (N+1)

    a = DFS(graph, 1, visited)

    # visited에 True가 몇 갠지 계산하면 감염된 컴퓨터가 몇 갠지 알 수 있다.
    # 1번 컴퓨터는 계산하지 하므로 -1 을 해준다.
    cnt = -1
    for i in range(N+1):
        if visited[i] == True:
            cnt += 1

print(cnt)