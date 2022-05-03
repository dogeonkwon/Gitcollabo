# import sys
# sys.stdin = open('input.txt','r')

# 슬라이딩 비교 

n, m = map(int, input().split())
w = input()
s = input()

wl = [0] * 52
sl = [0] * 52

# w의 각 알파벳마다 등장하는 부분 +1
for i in range(n):
    if 'a' <= w[i] <= 'z':
        wl[ord(w[i]) - ord('a')] += 1
    else:
        wl[ord(w[i]) - ord('A') + 26] += 1

print(wl)
start, length, count = 0, 0, 0

for i in range(m):
    if 'a' <= s[i] <= 'z':
        sl[ord(s[i]) - ord('a')] += 1
    else:
        sl[ord(s[i]) - ord('A') + 26] += 1
    length += 1

    if length == n:
        if wl == sl:
            count += 1
        if 'a' <= s[start] <= 'z':
            sl[ord(s[start]) - ord('a')] -= 1
        else:
            sl[ord(s[start]) - ord('A') + 26] -= 1
        start += 1
        length -= 1

print(sl)
print(count)



# 시간 초과
# def pick(n,picked, toPick):
#     if toPick == 0:
#         w_chars.append(picked[:])
    
#     for char in n:
#         if char not in picked:
#             pick(n, picked+[char], toPick -1)

# w, s = map(int, input().split())
# W = list(map(str, input()))
# S = list(map(str, input()))
# w_chars = []
# pick(W, [], w)
# cnt = 0
# for i in range(0, s-w):
#     for j in range(len(w_chars)):
#         for k in range(w):
#             if w_chars[j][k] not in S[i:i+4]:
#                 break
#         if w_chars[j] == S[i:i+4]:
#             cnt +=1

# print(cnt)