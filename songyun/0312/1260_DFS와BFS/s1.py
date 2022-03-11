import sys
sys.stdin = open('input.txt')

# v는 현재 노드
def dfs(v):
    print(v, end=' ')

    # 방문하면 visit에 방문했다고 표시
    visit[v] = 1

    # 노드 갯수 만큼 반복해서 탐색한다.
    for i in range(1, N + 1):

        # 만약 i 노드에 방문하지 않았고, 현재 노드와 i노드가 연결 되어 있다면
        if visit[i] == 0 and set[v][i] == 1:

            # 해당 노드를 탐색한다.
            dfs(i)

def bfs(v):
    # queue 에 현재 노드를 담고
    queue = [v]
    # visit 에 해당 노드를 방문했다고 표시 (dfs 에서 사용한 visit 변수를 재활용 했으므로 1이 아닌 0이 방문 했다는 표시)
    visit[v] = 0

    # queue 가 빌 때까지 반복한다.
    while(queue):

        # queue 의 맨 앞 원소를 탐색 할 것이다.
        v = queue[0]
        print(v, end=' ')

        # bfs는 이미 탐색한 노드라면 더 이상 필요 없다.
        # queue[0]를 없앤다.
        del queue[0]

        # 노드의 갯수 만큼 반복해서 탐색한다.
        for i in range(1, N + 1):

            # 탐색할 노드가 방문한 적이 없고, 현재 노드와 연결 되어 있따면
            if visit[i] == 1 and set[v][i] == 1:
                queue.append(i)
                visit[i] = 0

# N = 노드 갯수, M = 간선 갯수, V = 시작점
N, M, V=list(map(int, input().split()))

set = [[0] * (N+1) for i in range(N+1)] # 노드간 연결 상태를 표시할 set
visit = [0 for i in range(N+1)]         # 방문 여부를 저장할 visit

for i in range(M):
    x, y = map(int, input().split()) # 연결 상태 받아오기
    set[x][y] = 1 # 1-2 , 1-3
    set[y][x] = 1 # 2-1 , 3-1

dfs(V)
print()
bfs(V)