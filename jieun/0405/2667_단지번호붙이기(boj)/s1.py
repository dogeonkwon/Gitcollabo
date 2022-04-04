# BOJ 2667 단지번호 붙이기 풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt','r')

# 디큐안하고 싶은데 참을 수 업써,,
from collections import deque

# 아파트 넘버링하는 함수 만들기
def numbering(i, j, idx):
    queue = deque()
    queue.append([i,j])
    visited[i][j] =1
    while queue:
        start = queue.popleft()
        start_i = start[0]
        start_j = start[1]
        # 4방향 탐색
        for di, dj in [[-1,0],[1, 0],[0, 1], [0, -1]]:
            ni = start_i + di
            nj = start_j + dj
            # 인덱스 배열 안에 있어야하고 아직 방문안하고 배열의 값이 0이 아닌 곳
            if 0<= ni< N and 0<= nj < N and visited[ni][nj] ==0 and apartment[ni][nj] != 0:
                queue.append([ni,nj])
                visited[ni][nj] =1
                apt_list[idx] += 1


N= int(input())
apartment = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 단지번호: 단지번호 같은 아파트 개수 를 만들 수 있는 딕셔너리 만들기
apt_list = {}
idx = 1

for i in range(N):
    for j in range(N):
        if apartment[i][j] != 0 and visited[i][j] == 0:
            # 단지에 맞는 아파트 개수 세기
            apt_list[idx] =1
            numbering(i, j, idx)
            #
            idx+=1

# 그러면
# {1: 7, 2: 8, 3: 9} 딕셔너리가 생성

# 오름차순으로 정리해주고 각 단지 아파트 개수 출력
apt_list = sorted(apt_list.values())
print(len(apt_list))
for k in apt_list:
    print(k)