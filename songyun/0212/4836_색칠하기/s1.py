import sys
sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    box_num = int(input())

    red_box = []
    blue_box = []

    for n in range(box_num):
        r1, c1, r2, c2, color = map(int, input().split())
        # 빨간색 박스라면
        if color == 1:
            for i in range(r2-r1+1):
                for j in range(c2-c1+1):
                    red_box.append([r1+i,c1+j])

        else:
            for i in range(r2-r1+1):
                for j in range(c2-c1+1):
                    blue_box.append([r1+i,c1+j])



    cnt=0
    for k in red_box:
        if k in blue_box:
            cnt+=1
    print("#{} {} " .format(tc,cnt))
