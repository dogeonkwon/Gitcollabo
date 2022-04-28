# 10814_나이순-정렬 풀이
# 2022-04-30

N = int(input())
lst = [[] for _ in range(100001)]   # 들어올 수 있는 자리만큼 미리 만들어 준다.
stop = 0

for i in range(N):
    age, name = input().split() # 나이와 이름을 따로 받음
    lst[int(age)].append(name)  # 나이에 맞는 인덱스에 이름을 저장
for j in range(100001):     # 나이인덱스에 값이 있다면 순서대로 출력
    if lst[j]:
        for k in lst[j]:
            print(f'{j} {k}')
            stop += 1
    if stop == N:       # N만큼 구했다면 멈춤
        break