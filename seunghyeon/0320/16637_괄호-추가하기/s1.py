# 16637_괄호-추가하기 풀이
# 2022-03-07

N = int(input())
calc = list(map(str, input()))
queue = [0] * N
tail = -1
front = 0
result = 0

for c in range(0, N, 2):
    tail += 1
    queue[tail] = int(calc[c])

result = queue[front]
front = 1
i = 1

while i < N:
    if i+2 < N and calc[i] == '+' and calc[i+2] == '*' and result < 0:
        val = queue[front] * queue[front + 1]
        front += 2
        result += val
        i += 4
        continue
    elif calc[i] == '+':
        result += queue[front]
        front += 1
        i += 2
        continue
    elif i+2 < N and calc[i] == '-' and calc[i+2] == '*':
        result1 = (result-queue[front]) * queue[front+1]
        result2 = result - (queue[front] * queue[front+1])
        front += 2
        i += 4
        if result1 > result2:
            result = result1
        else:
            result = result2
        continue
    elif i+2 < N and calc[i] == '-' and calc[i+2] == '-':
        if queue[front] < queue[front+1]:
            val = queue[front] - queue[front+1]
            result -= val
            front += 2
            i += 4
            continue
        else:
            result -= queue[front]
            front += 1
            i += 2
            continue
    elif calc[i] == '-':
        result -= queue[front]
        front += 1
        i += 2
        continue
    elif i+2 < N and calc[i] == '*' and calc[i+2] == '+':
        val = queue[front] + queue[front+1]
        front += 2
        result *= val
        i += 4
        continue
    elif i+2 < N and calc[i] == '*' and calc[i+2] == '-' and result < 0 and queue[front] < queue[front+1]:
        val = queue[front] - queue[front+1]
        front += 2
        result *= val
        i += 4
        continue
    elif calc[i] == '*':
        result *= queue[front]
        front += 1
        i += 2
        continue

print(result)