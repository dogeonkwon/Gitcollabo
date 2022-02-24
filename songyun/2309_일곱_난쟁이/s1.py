import sys
sys.stdin = open('input.txt')

height = []
for _ in range(9):
    height += (map(int, input().split()))

# 부분집합 구하기
# 9명이기 때문에 1을 9번 옮겨가며 검사해야 한다.
for i in range(1 << 9):

    # 부분집합의 경우를 담을 리스트
    part = list()

    # 여기서 부분집합의 개수가 1개인거 부터 9개 까지
    for j in range(9):
        if i & (1 << j):
            part.append(height[j])
            print(part)
        sum_1 = 0

    # 모든 부분집합들의 합
    for p in part:
        sum_1 += p

    # 만약 부분 집합의 합이 100이고, 부분의집합의 길이가 7이면 ans
    if sum_1 == 100 and len(part) == 7:
        ans = part

# 오름차순으로 정렬한다.
for i in range(7):
    for j in range(7):
        if ans[i] < ans[j]:
            ans[i], ans[j] = ans[j], ans[i]

# 하나하나 출력한다.
for i in ans:
    print("{}".format(i))

