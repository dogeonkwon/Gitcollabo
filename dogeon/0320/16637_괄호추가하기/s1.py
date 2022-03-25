# 16637_괄호추가하기 풀이
# 2022-03-12

from collections import deque


def bracket(stack, q):
    global number, operation, result

    if not q:
        k = 0
        while k < len(stack):
            j = stack[k]
            if j in operation:
                if j == '+':
                    result.append(result.pop() + stack[k+1])
                    k += 2
                    # return
                elif j == '-':
                    result.append(result.pop() - stack[k+1])
                    k += 2
                    # return
                elif j == '*':
                    result.append(result.pop() * stack[k+1])
                    k += 2
                    # return
            else:
                result.append(j)
                k += 1
                # return
    else:
        n = q.popleft()
        if n in operation:
            for i in range(2):
                if i == 0 and n == '+':
                    stack1 = stack + [int(stack.pop()) + int(q.popleft())]
                    stack1.append(q.popleft())
                    q1 = q
                    bracket(stack1, q1)
                elif i == 0 and n == '-':
                    stack2 = stack + [int(stack.pop()) - int(q.popleft())]
                    stack2.append(q.popleft())
                    q2 = q
                    bracket(stack2, q2)
                elif i == 0 and n == '*':
                    stack3 = stack + [int(stack.pop()) * int(q.popleft())]
                    stack3.append(q.popleft())
                    q3 = q
                    bracket(stack3, q3)
                else:
                    stack4 = stack + [n]
                    q4 = q
                    bracket(stack4, q4)
        else:
            stack5 = stack + [int(n)]
            q5 = q
            bracket(stack5, q5)


N = int(input())
lst = deque(list(map(str, input())))
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operation = ['+', '-', '*']
visited = [False for _ in range(N+1)]
stack = list()
q = deque(lst)
result = list()

bracket(stack, q)
print(result)
# print(q)
# print(lst)
# print(int(lst[0]) in number)