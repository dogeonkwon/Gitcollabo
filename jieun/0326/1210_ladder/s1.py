import sys
sys.stdin = open('input.txt','r')

T = 10
for tc in range(1, T+1):
    t = int(input())
    #100x100행렬 옆에 0을 만날 수 있게 0으로 된 기둥을 양옆에 세워줄게
    arr = [[0] + list(map(int, input().split())) +[0] for _ in range(100)]
    
    #2가 있는 자리에서 거꾸로 올라갈거야 일단 그 위치가 어디있는지 알려줘
    for j in range(102):
        if arr[99][j] ==2:
            y = j
    x = 99
    
    # 위, 오른쪽, 왼쪽
    dx = [-1, 0, 0]
    dy = [0, 1, -1]
    
    #direction 0: 위/ 1: 오른쪽/ 2: 왼쪽
    direction = 0
    
    #무한 루프를 만들건데
    while True:
        #만약 x가 0행까지 올라왔다면 멈쳐줘
        if x == 0:
            break
        
        #왼쪽에 1이있다면 왼쪽으로 꺾기
        if arr[x][y-1] ==1:
            direction = 2
            # 왼쪽으로 쭉 가고 있다가 0을 마주치면 while문 깨고 나와서 위로 올라가는 코드 타
            while True:
                x+=dx[direction]
                y+=dy[direction]
                if arr[x][y-1] ==0:
                    break
        
        #오른쪽에 1이 있다면 오른쪽으로 꺾기
        elif arr[x][y+1] ==1:
            direction = 1
            # 오른쪽으로 쭉 가고 있다가 0을 마주치면 while문 깨고 나와서 위로 올라가는 코드 타
            while True:
                x+=dx[direction]
                y+=dy[direction]
                if arr[x][y+1] ==0:
                    break

        #이도 저도 아니라면 위쪽 방향으로 계속 올라가기
        direction = 0
        x+= dx[direction]
        y+= dy[direction]
    
    #테스트 케이스 번호와 2에 도착하게 되는 출발점의 x좌표를 구해라!
    print('#{} {}'.format(t, y-1))