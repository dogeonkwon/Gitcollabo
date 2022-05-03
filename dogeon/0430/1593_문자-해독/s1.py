# 1593_문자-해독 풀이
# 2022-04-30

n, m = map(int, input().split())
w = input()
s = input()

start, res, cnt = 0, 0, 0

# 모든 알파벳이 몇번 담겼는지 기록해줄 리스트
wl = [0] * 52
sl = [0] * 52

# w가 어떤 알파벳을 담고 있는지 체크
for i in range(n):
    if 'A' <= w[i] <= 'Z':
        wl[ord(w[i]) - ord('A')] += 1
    else:
        wl[ord(w[i]) - ord('a') + 26] += 1

# s가 어떤 알파벳을 담고 있는지 체크하면서 n만큼이 되었으면 w와 같은지 체크한 후 제일 처음 들어왔던 값을 하나 지우고 다시 탐색
for j in range(m):
    if 'A' <= s[j] <= 'Z':
        sl[ord(s[j]) - ord('A')] += 1
    else:
        sl[ord(s[j]) - ord('a') + 26] += 1
    cnt += 1

    if cnt == n:
        if wl == sl:
            res += 1
        if 'A' <= s[start] <= 'Z':
            sl[ord(s[start]) - ord('A')] -= 1
        else:
            sl[ord(s[start]) - ord('a') + 26] -= 1
        start += 1
        cnt -= 1
print(res)