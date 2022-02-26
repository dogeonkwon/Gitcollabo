import sys
sys.stdin = open('input.txt','r')
#모든 테스트 케이스 수를 받아줘
T = int(input())
# 모든 테스트 케이스를 살펴볼거야
for t in range(1, T+1):
    #몇번 색칠할건지 받아줘
    n = int(input())
    #일단 빈 10X10 행렬을 만들어줘
    arr = [[0]* 10 for _ in range(10)]
    #n번만큼 계속 실행할건데 뭘 할거냐면
    for _ in range(n):
        #x1, y1, x2, y2 좌표와, 어떤 색깔을 칠한건지 받아줘
        x1, y1, x2, y2, color = map(int, input().split())
        #그리고 x1부터 x2까지 살펴볼거고
        for i in range(x1, x2+1):
            #y1부터 y2까지 살펴볼건데
            for j in range(y1, y2+1):
                #만약 색깔이 빨간색이라면 빈 행렬에 1을 더해주고
                if color == 1:
                    arr[i][j] +=1
                #만약 색깔이 파란색이라면 빈 행렬에 2를 더해줘
                elif color == 2:
                    arr[i][j] +=2
    cnt = 0
    #10x10를 살펴볼거라 10x10범주를 살펴볼건데
    for i in range(10):
        for j in range(10):
            #빨간색도 칠해주고 파란색도 칠했다면 보라색이 됐을 텐데 그러면 1+2 = 3이 되겠지?
            if arr[i][j] == 3:
                #3이된다면 1을 count해줘!
                cnt +=1
    print('{} {}'.format(t, cnt))