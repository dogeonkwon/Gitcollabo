# 1593_문자-해독 풀이
# 2022-04-30

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
print(count)


'''
g, s = map(int, input().split())
W = input()
S = input()
cnt = 0

for i in range(g, s):
    word = 0
    for j in W:
        if j in S[i-g:i]:
            word += 1
        else:
            break
    if word == g:
        cnt += 1
print(cnt)
'''