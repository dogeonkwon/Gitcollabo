import sys
sys.stdin = open('input.txt')

from collections import deque
F, S, G, U, D = list(map(int, input().split()))

queue = deque()
queue.append((S, 0))

# 각 층의 방문 여부를 기록 할 리스트
visited = [0] * (F+1)

# 시작 층 방문
visited[S] = 1

# 결과값
result = 0
while queue:
    # current : 현재 위치, cnt : 몇 번 만에 방문 했는지
    current, cnt = queue.popleft()

    # 목표지점에 도착 했을 때
    if current == G:
        result = cnt
        break

    # 위층으로 움직였을 때, 범위 안에 들어오고, 아직 방문하지 않은 곳일 때
    if current + U <= F and not visited[current+U]:
        # 그곳을 방문 처리하고
        visited[current+U] = 1
        # 다음 층과 cnt 에 +1을 한다.
        queue.append((current+U, cnt+1))

    if current - D >= 1 and not visited[current-D]:
        visited[current-D] = 1
        queue.append((current-D, cnt+1))

    print(queue)

if result > 0:
    print(result)
else:
    print('use the stairs')

