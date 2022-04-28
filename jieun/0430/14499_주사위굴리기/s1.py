import sys
sys.stdin = open('input_text.txt','r')

# 전개도 따라서 만들어주기
def rolling_dice(direction):
    if direction == 1:
        dice[3], dice[0], dice[2],dice[4],dice[1],dice[5] = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
        return
    elif direction == 2:
        dice[1], dice[4], dice[2],dice[0],dice[3],dice[5] = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
        return
    elif direction == 3:
        dice[5], dice[1], dice[0],dice[3],dice[2],dice[4] = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
        return
    elif direction == 4:
        dice[2], dice[1], dice[4],dice[3],dice[5],dice[0] = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
        return

# 배열 안에 있는지 체크
def inarr_check(x, y, direction):
    dxdy = [[0,0], [0,1],[0,-1],[-1,0],[1,0]]
    nx, ny = x+ dxdy[direction][0], y+ dxdy[direction][1]
    if 0<= nx< N and 0<= ny < M:
        return True
    else:
        return False

N, M, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 주사위 전개도를 담을 리스트
dice = [0]* 6
i = 0
while i < k:
    dir = command[i]
    # 배열안에 있다면
    if inarr_check(x, y, dir) == True:
        dxdy = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]
        x += dxdy[dir][0]
        y += dxdy[dir][1]
        # 방향대로 주사위 굴리기
        rolling_dice(dir)
        # 칸이 0으로 되어있다면 주사위의 밑면에 담긴 숫자를 지도 칸에 넣기
        if arr[x][y] == 0:
            arr[x][y] = dice[4]
        # 칸이 0으로 되어있지 않다면 지도 칸을 주사위 밑면에 넣고 지도 칸 0으로 만들기
        elif arr[x][y] >0 :
            dice[4] = arr[x][y]
            arr[x][y] =0
        # 천장을 바라보는 칸의 숫자 출력
        print(dice[0])

    i+=1
