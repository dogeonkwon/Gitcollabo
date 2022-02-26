import sys
sys.stdin = open('input.txt')

swi_num = int(input()) # 스위치 갯수
switch = list(map(int, input().split())) # 스위치 상태

N = int(input()) # 학생 수

for _ in range(N):

    std = list(map(int,input().split())) # 성별과 받은 카드

    gen = std[0]
    card = std[1]

    if gen == 1: # 남학생 이라면
        i = 0
        while (card-1+card*i) < swi_num:
            if switch[card-1+card*i] == 1:
                switch[card - 1 + card * i] = 0
            else:
                switch[card - 1 + card * i] = 1

            i+=1

    if gen == 2: # 여학생 이라면

        # 양쪽 비교
        j =1
        card_idx = card - 1 # 2

        if switch[card_idx] == 1:
            switch[card_idx] = 0
        else:
            switch[card_idx] = 1


        # 양쪽 스위치 상태가 같다면
        if switch[card_idx-j] == switch[card_idx+j]:
            while card_idx-j >= 0 and card_idx+j < swi_num :

                if switch[card_idx-j] == 1:
                    switch[card_idx - j] = switch[card_idx+j] = 0
                else:
                    switch[card_idx - j] = switch[card_idx + j] = 1

                j+=1


k = 0
i = 1

while k < swi_num :
    print(switch[k], end=' ')

    k+=1

    if k > 20*i:
        print()
        i+=1




# arr =[]
# for z in range(100):
#     arr.append(z)
# print(arr)
# a = 1
# b = 2
#
# while a ==1 and b > 1:
#     a+=1
#
# if a > 0:
#     a+=1
# print(a)
