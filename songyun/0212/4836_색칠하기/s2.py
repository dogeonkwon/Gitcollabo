# 4836_색칠하기
# 22-02-15
import sys
sys.stdin = open('sample_input.txt', 'r')

# Test Case
T = int(input())

for t in range(1,T+1):
    boxes = int(input())
    red_box = list() # 빨간색으로 칠할 좌표를 넣을 리스트 생성
    blue_box = list() # 파란박스 리스트

    for i in range(boxes):
        x1, y1, x2, y2, color = map(int, input().split())
        
        # 만약 색이 빨간색이라면
        if color == 1: 
            # 아래 반복문을 통해 빨간색이 칠해질 좌표를 red_box에 추가 
            # 만약 (2,2) (4,4) 가 좌표라면 3X3 크기의 박스 이므로
            for j in range(x2-x1+1): # 3번 (4-2+1)
                for k in range(y2-y1+1): # 3번 (4-2+1)
                    red_box.append((x1+j)*10+(y1+k)) # red_box=[22,23,24,32,33,34,42,43,44]가 추가됨
        
        # (3,3) (6,6)의 파란색박스라면
        else:
            for j in range(x2-x1+1):
                for k in range(y2-y1+1):
                    blue_box.append((x1+j)*10+(y1+k)) # blue_box=[33,34,35,36,43,44,45,46,53,54,55,56,63,64,65,66]

    cnt = 0
    # red_box와 blue_box를 비교하여 중복되는 숫자의 갯수를 카운트
    for num in red_box:
        # 만약 red_box의 숫자가 blue_box에도 있다면
        if num in blue_box:
            # 1 카운트 
            cnt += 1
    print('#{} {}'.format(t, cnt))