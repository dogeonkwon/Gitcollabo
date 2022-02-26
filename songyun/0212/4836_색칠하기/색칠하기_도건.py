import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

# !!!문제를 제대로 안 읽고 풀어서 4시간 동안 헤맸다. 다음에는 문제부터 꼼꼼히 보자!!!

# (x, y), (n, m)이 주어졌을 때 x좌표끼리의 차이와 y좌표끼리의 만큼의 범위에 color(정해진 숫자)를 더 할 수 있는 함수를 만들어준다.
def overlapping_colors(N, arr):

    # 받은 값들을 5군데로 나눠서 담는다.
    min_x_location = N[0]
    min_y_location = N[1]
    max_x_location = N[2]
    max_y_location = N[3]
    color = N[4]

    # y(열)의 탐색이 끝나면 다음 x(행)로 넘어가기 때문에 정해진 범위에 있는 모든 값들을 color만큼 변화시킬 수 있다.
    for i in range(min_x_location, max_x_location+1):
        for j in range(min_y_location, max_y_location+1):
            arr[i][j] += color

    # 그리고 변한 값들을 담고 있는 arr리스트를 return 해준다.
    return arr


for tc in range(1, T+1):

    M = int(input())

    # 몇 개의 영역이 보라색으로 바꼈는지 체크하기 위함
    cnt = 0

    # 10 x 10의 2차원 리스트를 만들어 준다.
    base = result = [[0 for _ in range(10)] for _ in range(10)]

    # M(칠할 영역의 개수)만큼 반복한다.
    for k in range(M):

        N = list(map(int, input().split()))

        # result에 전에 만들었던 함수를 활용하한 결과를 넣어준다.
        result += overlapping_colors(N, base)

    # 모든 영역을 검사하며 보라색(3)이 되었다면 cnt를 1씩 늘려준다.
    # 여기서 1(빨강) + 2(파랑) = 3(보라색)이라 생각하지 못하고 빨강과 빨강이 겹치는 부분도 카운트하는 코드를 짜다가 시간을 많이 날렸다.
    # 다음부터는 문제에서 요구하는 것이 무엇인지 제대로 보자.
    for a in range(10):
        for b in range(10):
            if result[a][b] == 3:
                cnt += 1


    print('#{} {}'.format(tc, cnt))