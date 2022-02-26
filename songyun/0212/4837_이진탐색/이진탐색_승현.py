# 이진탐색
# 2022-02-12

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    # l: 시작페이지, r: 끝 페이지
    # A, B: A와 B가 찾을 페이지 번호
    # c: 중간값
    # cnt_A: A가 이중탐색을 실행한 횟수
    # cnt_B: B가 이중탐색을 실행한 횟수
    # page: 끝값을 저장
    r, A, B = map(int, input().split())
    l = 1
    c = 0
    cnt_A = 0
    cnt_B = 0
    page = int(r)

    # A의 이중탐색 실행횟수 계산
    while True:
        c = (r+l)//2

        # 이중탐색 종료
        if c == A:
            break

        # 중간값이 찾을 페이지보다 작으면, 왼쪽값 수정
        elif c < A:
            l = c

        # 중간값이 찾을 페이지보다 크면, 오른쪽값 수정
        elif c > A:
            r = c

        cnt_A += 1

    # B를 탐색하기 위해 시작페이지와 끝페이지 초기화
    r = page
    l = 1

    # B의 이중탐색 실행횟수 계산
    while 1:
        c = (r+l)//2

        # 이중탐색 종료
        if c == B:
            break

        # 중간값이 찾을 페이지보다 작으면, 왼쪽값 수정
        elif c < B:
            l = c

        # 중간값이 찾을 페이지보다 크면, 오른쪽값 수정
        elif c > B:
             r = c

        cnt_B += 1

    if cnt_A == cnt_B:
        print('#{} {}'.format(tc, 0))

    elif cnt_A < cnt_B:
        print('#{} {}'.format(tc, 'A'))

    else:
        print('#{} {}'.format(tc, 'B'))
