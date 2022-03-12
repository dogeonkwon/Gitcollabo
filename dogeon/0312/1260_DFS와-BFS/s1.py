# 1260_DFS와-BFS 풀이
# 2022-03-12

from collections import deque   # deque를 사용하기 위한 라이브러리를 가져온다.


def dfs(lst, start, visited):   # dfs 구현 함수
    global D_result

    visited[start] = True       # 지나간 자리(출발)를 True로 바꿔준다.
    D_result += [start]         # 그리고 dfs 결과변수에 추가해준다.
    for k in lst[start]:        # 출발할 값으로부터 어디로 갈 수 있는지 확인한다.
        if not visited[k]:      # 그 곳이 False라면 다시 그 곳을 출발점으로 잡는 dfs함수를 실행
            dfs(lst, k, visited)


def bfs(lst, start, visited):   # bfs 구현 함수
    global B_result

    queue = deque([start])      # queue를 데크로 설정해준다.
    visited[start] = True       # 그리고 그 자리를 True로 변경
    while queue:
        v = queue.popleft()     # queue의 제일 왼쪽값을 pop시킨 후 v에 넣어준다.
        B_result += [v]         # bfs 결과변수에 추가.
        for k in lst[v]:            # v를 출발값으로 가지는 목적지들을 전부 탐색
            if not visited[k]:      # 그 곳이 False라면
                queue.append(k)     # queue에 k값을 넣어준다.(바로 다음 탐색을 하지 않는 이유는 너비 우선 탐색이기 때문)
                visited[k] = True   # 또한 그 자리를 True로 변경


N, M, V = list(map(int, input().split()))
lst = [[] for _ in range(N+1)]          # 각 노드에 맞게 연결된 노드들을 나타내기 위함
D_visited = [False for _ in range(N+1)]            # 방문하였다는 것을 나타내기 위함(인덱스 0을 포함해야 하기 때문에 노드의 개수 + 1을 해준다.)
D_result = list()                       # 결과 값을 저장할 변수
B_visited = [False for _ in range(N+1)]
B_result = list()

for _ in range(M):                      # 노드 출발 인덱스와 연결된 노드들의 값을 빈 인덱스에 넣어준다.(+작은 수부터 탐색하기 위하여 미리 정렬을 해준다.)
    i, j = map(int, input().split())
    lst[i].append(j)
    lst[j].append(i)
    lst[i].sort()
    lst[j].sort()

dfs(lst, V, D_visited)
print(*D_result)

bfs(lst, V, B_visited)
print(*B_result)
