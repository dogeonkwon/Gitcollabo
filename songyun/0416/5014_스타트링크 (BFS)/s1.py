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

# 최대 층 수
result = F

while queue:
    # s : 현재 위치, cnt : 몇 번 만에 방문 했는지
    s, cnt = queue.popleft()

    # 목표지점에 도착 했을 때
    if s == G:
        result = cnt #
        break

    # 위층으로 움직였을 때 범위 안에 들어오고, 아직 방문하지 않은 곳일 때
    if s + U <= F and not visited[s+U]:
        # 그곳을 방문 처리하고
        visited[s+U] = 1
        # 다음 층과 cnt 에 +1을 한다.
        queue.append((s+U, cnt+1))

    if s - D >= 1 and not visited[s-D]:
        visited[s-D] = 1
        queue.append((s-D, cnt+1))
    print(queue, cnt)


# while 문이 다 도는 동안 result 의 가 F 그대로인 경우
if result == F:
    print('use the stairs')


else:
    print(result)
