# 1219_길찾기 (BFS)
# 2022-03-23
import sys
sys.stdin = open('input.txt')

T = 10

def BFS(s, ch1, ch2):

    # 시작점을 queue 에 추가하고
    queue.append([s])
    # 방문 처리 한다.
    visited[s] = True
    # print(queue)
    while queue[0]:
        # print(queue)
        v = queue.pop()  # 현재 탐색 중인 노드
        temp = []   # v에 어떤 노드들이 연결 됐나~ 담을 리스트

        for i in v:
            # ch1에 v와 연결된 노드가 있고,
            if ch1[i]:
                # 그곳이 방문하지 않은 곳이라면
                if not visited[ch1[i]]:
                    # 그곳을 temp 에 담는다.
                    temp.append(ch1[i])
                    visited[ch1[i]] = True

            # ch2도 동일
            if ch2[i]:
                if not visited[ch2[i]]:
                    temp.append(ch2[i])
                    visited[ch2[i]] = True

        # temp 에는 v와 연결된 최대 두개의 노드가 리스트 형태로 들어가 있다.
        queue.append(temp)
        # print(queue)
        # 만약 도착점이 queue 에 담기면 1을 출력
        if end in queue[0]:
            return print("#{} {}".format(tc, 1))

    # queue 가 다 비어도 end를 찾지 못하면 0을 출력
    return print("#{} {}".format(tc, 0))


for tc in range(1, T+1):
    # N: tc 번호 M: 길의 갯수
    N, M = list(map(int, input().split()))
    arr = list(map(int,input().split()))

    # 각 노드에는 최대 2개의 갈림길이 존재한다.
    # 각 갈림길을 담을 두개의 리스트
    ch1 = [[] for _ in range(100)]
    ch2 = [[] for _ in range(100)]


    for i in range(0, 2*M, 2):

        # 만약 ch1[x]에 아무 값이 없다면
        if not ch1[arr[i]]:
            ch1[arr[i]] = arr[i+1]

        # ch1[x]에 값이 있다면 ch2에 넣는다.
        else:
            ch2[arr[i]] = arr[i+1]

    # 노드의 개수는 총 100개
    visited = [False] * 100
    # 도착점의 노드 번호
    end = 99
    # 노트 x와 연결된 노드를 담을 queue
    queue = []
    # 시작점과 ch1, ch2를 보낸다.
    BFS(0, ch1, ch2)