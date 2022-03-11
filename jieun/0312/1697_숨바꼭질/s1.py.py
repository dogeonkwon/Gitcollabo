from collections import deque
import sys
sys.stdin = open('input.txt','r')

def bfs(N,K):
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x== K:
            print(distance[x])
            return
        for i in (x-1, x+1, x*2):
            if 0<= i <= 10000 and distance[i] == 0:
                distance[i] = distance[x] + 1
                queue.append(i)

N, K = 5, 17
max = 10000
distance = [0] * (max+1)
bfs(N, K)