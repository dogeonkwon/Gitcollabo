# 1717_집합의-표현 풀이
# 2022-05-07
import sys
sys.setrecursionlimit(10**6)    # 파이썬의 기본 재귀 깊이 제한은 1000으로 굉장히 적다. 따라서 sys.setrecursionlimit() 함수를 통해서 재귀 깊이를 크게 잡는다.

def find(k):        # 부모 노드를 찾아주는 함수
    if arr[k] == k:         # 자기 자신이 부모노드이면 그대로 반환
        return k
    arr[k] = find(arr[k])   # 아니라면 재귀를 통해 부모노드를 찾는다.
    return arr[k]


def union(x, y):    # x가 속한 집합과 y가 속한 집합을 합치는 함수
    x = find(x)     # x의 부모노드를 x에 넣고
    y = find(y)     # y의 부모노드를 y에 대임

    if x == y:      # 같으면 같은 집합에 있다는 의미이므로 변화가 없고
        return
    else:           # 다르면 arr[y]의 부모노드를 x로 바꿔준다.(합치기)
        arr[y] = x


n, m = map(int, sys.stdin.readline().split())   # 대량의 데이터를 반복적으로 입력받아야 할 때, input()대신 sys.stdin.readline()을 이용하면 성능(속도)이 향상
arr = [s for s in range(n+1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())    # sys.stdin.readline()대신 input()을 사용하여 시간초과가 발생
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')