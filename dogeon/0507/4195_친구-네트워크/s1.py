# 4195_친구-네트워크 풀이
# 2022-05-07

import sys
sys.setrecursionlimit(10**6)


def find(x):            # 부모 노드 찾기
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])     # 재귀를 통해 부모 노드 찾기
    return parent[x]


def union(x, y):    # 두 친구가 속한 부모노드를 합치는 함수
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x   # 부모노드가 다르면 y의 부모 노드를 x의 부모 노드로 바꿔준다
        number[x] += number[y]   # x의 탐색횟수에 y의 탐색횟수 만큼을 더해준다


for _ in range(int(input())):
    parent = dict()             # 부모노드를 가리킬 딕셔너리
    number = dict()             # 헤더의 자식이 몇개인지 나타낼 딕셔너리
    f = int(sys.stdin.readline())   # 대량의 데이터를 반복적으로 입력받아야 할 때, input()대신 sys.stdin.readline()을 이용하면 성능(속도)이 향상

    for i in range(f):
        f1, f2 = sys.stdin.readline().split()   # 이번 문제에서는 input()을 사용하여도 시간초과 발생하지 않음

        if f1 not in parent:        # 친구목록에 없다면 추가
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1

        union(f1, f2)
        print(number[find(f1)])