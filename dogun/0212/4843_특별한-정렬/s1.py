import sys
sys.stdin = open('sample_input.txt', 'r')


# 길이를 구하기 위한 함수정의
def length(mylst):

    z = 0
    for _ in mylst:
        z += 1
    return z


# 테스트케이스의 수를 받는다.
T = int(input())

for tc in range(1, T+1):


    N = int(input())
    numbers = list(map(int, input().split()))

    # numbers를 선택정렬로 오름차순으로 만들어준다.
    for i in range(N-1):
        for j in range(i, N):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    # N보다 1작은 값까지 검사해야 하기 때문에 m = N - 1을 만들어 준다.
    # 조건에 맞는 리스트를 만들어주기 위한 빈 리스트를 만들어 준다.
    # 10개만 뽑아야 하기 때문에 일단 N-10의 값을 R에 넣어준다.
    m = N-1
    lst = []
    R = N-10

    # N이 하나씩 줄어들어 R이 된다면 탈출하는 while문을 만들었다.
    while N != R:
        N -= 1
        lst.append(numbers[m])

        # N을 나눴을 때 홀수라면 N만큼을 빼고
        if N % 2:
            m -= N

        # N을 나눴을 때 짝수라면 N만큼을 더해서
        else:
            m += N

        # 최종적으로 맨 뒤값, 맨 앞값, 두 번째 뒤에 값, 두 번째 앞값 .... 형식으로 10개가 맞춰진다.

    # 그 리스트의 순서대로 출력을 해준다.
    print('#{} '.format(tc), end='')
    for v in range(length(lst)):
        if v == length(lst)-1:
            print(lst[v])
        else:
            print(lst[v], end=' ')