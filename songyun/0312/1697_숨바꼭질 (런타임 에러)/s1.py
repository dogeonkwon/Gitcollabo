from collections import deque

def bfs(s, level):

    # 시작점을 큐에 넣는다.
    queue = deque([s])

    # 빈 queue 가 될 때까지 반복
    while queue:

        # c = 현재 위치
        c = queue.popleft()

        # 만약 현재 위치가 동생의 위치랑 같다면
        if c == K:
            # 현재위치의 레벨을 print 후 반복문 종료
            print(level[c])
            break

        # 그렇지 않다면 c에서 갈 수 있는 다음 위치(자식 노드)를 고려해야 한다.
        elif c != K:
            # 걸어가거나 순간이동한 위치의 경우의 수
            for i in (c-1, c+1, 2*c):
                # 처음 방문한 곳 이라면
                if not level[i]:
                    # 이전 위치(부모노드)의 레벨에 +1을 한다.
                    level[i] = level[c] + 1
                    # queue 에 넣어 다음 탐색에 사용한다.
                    queue.append(i)


# N = 시작점, K = 동생의 위치
N, K = list(map(int, input().split()))

# 각 노드의 레벨을 알려줄 변수 (몇 초가 걸렸는지)
level = [0] * 100001
bfs(N, level)
