import sys
sys.stdin = open('sample_input.txt', 'r')



T = int(input())

# 12개의 숫자를 가진 집합 A를 설정해준다.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# A의 길이구하기
length = 0
for _ in A:
    length += 1

# 모든 경우의 수를 받을 빈 리스트를 만들어준다.
lst = []

# 1 << length == 2^length 만큼 for문을 돌려준다.(비트연산자)
for i in range(1 << length):

    # 한 사이클의 경우의 수를 받을 빈 리스트를 만들어준다.
    sub_lst = []

    # length의 값만큼 for문을 돌려주는데 그 이유는 모든 갑들을 비교해야 하기 때문이다.
    # 이 부분이 조금 헷갈림
    for j in range(length):
        if i & (1 << j):
            sub_lst.append(A[j])
    lst.append(sub_lst)
# 큰 for문이 종료되면 lst에 모든 경우의 수를 담은 집합이 만들어짐


for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt = 0

# 모든 경우의 수를 담은 lst에서 하나씩 개별의 리스트를 뽑아낸다.
    for k in lst:

        # for문이 돌아갈 때마다 하나의 개별 리스트에 있는 숫자들의 합을 담기 위한 변수
        total = 0

        # k의 길이를 구하기 위함 그래야 조건에 맞을 경우 for문을 사용할 수 있음
        k_length = 0
        for _ in k:
            k_length += 1

        # k의 길이(k_length)가 N이라면
        # for문을 통해 각각 개별 인자를 total에 더해줄 수 있도록 한다.
        if k_length == N:
            for l in k:
                total += l

        # 그리고 만약 더해준 total값이 M과 같다면 카운트를 1씩 올려준다.
        if total == M:
            cnt += 1

    print('#{} {}'.format(tc, cnt))