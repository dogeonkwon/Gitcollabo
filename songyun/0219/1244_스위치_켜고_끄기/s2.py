import sys
sys.stdin = open('input.txt')

swi_num = int(input()) # 스위치 갯수
switch = list(map(int, input().split())) # 스위치 상태

N = int(input()) # 학생 수

for _ in range(N):

    # std = [성별, 카드 숫자]
    std = list(map(int,input().split()))

    gen = std[0]
    card = std[1]
    card_idx = card - 1
    # 남학생 이라면
    if gen == 1:

        i = 0
        # card-1은 list의 인덱스와 맞추기 위해, card*i는 배수 설정
        while (card-1+card*i) < swi_num:
            # 해당 인덱스의 스위치가 1이면 0으로 바꾸고,
            if switch[card-1+card*i] == 1:
                switch[card - 1 + card * i] = 0
            # 0이면 1로 바꾼다.
            else:
                switch[card - 1 + card * i] = 1

            i += 1

    # 여학생 이라면
    if gen == 2:


        j = 1

        # 우선 카드 숫자에 대응하는 번호의 스위치 상태를 바꾼다.
        if switch[card_idx] == 1:
            switch[card_idx] = 0
        else:
            switch[card_idx] = 1

        # 스위치의 index가 벗어나지 않고, 양쪽 스위치 상태가 같다면
        while card_idx-j >= 0 and card_idx + j <= swi_num - 1 and (switch[card_idx-j] == switch[card_idx + j]):

            # 왼쪽 스위치 상태 바꿈
            if switch[card_idx - j] == 1:
                switch[card_idx - j] = 0
                switch[card_idx + j] = 0

            else:
                switch[card_idx + j] = 1
                switch[card_idx - j] = 1
            # 오른쪽 스위치 상태 바꿈

            # 한칸 옮겨서 양쪽 스위치의 상태를 비교한다.
            j += 1

k = 0
while k < swi_num:
    # 19, 39 번째 인덱스면 뒤에 공백 없이 출력한다.
    if k % 20 == 19:
        print(switch[k])
        k += 1
    # 19, 39 번째 인덱스가 아니라면 공백을 주면서 일렬로 출력하고
    else:
        print(switch[k], end=' ')
        k += 1