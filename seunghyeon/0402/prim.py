from asyncio.windows_events import INFINITE

def MST_PRIM(G, s):                     # G: 그래프, s: 시작점
    key = [INFINITE]] * N               # 가중치를 무한대로 초기화
    pi = [None] * N                     # 트리에서 연결될 부모 정점 초기화
    visited = [False] * N               # 방문 여부 초기화
    key[s] = 0                          # 시작 정점의 가중치를 0으로 설정

    for _ in range(N):          # 정점의 개수만큼 반복
        min_idx = -1
        min = INFINITE

        # 방문 안한 정점 중 최소 가중치 정점 찾기
        for i in range(N):
            if not visited[i] and key[i] < min:
                min = key[i]
                min_idx = i
        
        visited[min_idx] = True   # 최소 가중치 정점 방문처리
        
        # 선택 정점의 인접한 정점 탐색
        # 선택 정점의 인접한 정점 중 key값보다 더 작은 가중치로 트리에 연결될 수 있는 경우,
        # 정점 v의 key를 더 작은 가중치로 업데이트
        for v, val in G[min_idx]:
            if not visited[v] and key[i] > val:
                key[v] = val          # 가중치 갱신
                pi[v] = min_idx       # 트리에서 연결될 부모정점