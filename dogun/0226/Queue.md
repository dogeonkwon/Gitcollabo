# Queue



## 선형 Queue

- <strong>(중요)<span style = color:red> FIFO 구조</span></strong>

![image-20220225155403520](Queue.assets/image-20220225155403520.png)



![image-20220225155438892](Queue.assets/image-20220225155438892.png)



![image-20220225155729719](Queue.assets/image-20220225155729719.png)



![image-20220225155818938](Queue.assets/image-20220225155818938.png)



- 연결 큐는 교재에서 다루지 않음

![image-20220225155900713](Queue.assets/image-20220225155900713.png)



![image-20220225160115372](Queue.assets/image-20220225160115372.png)



```python
# 가장 앞에 있는 원소를 검색하여 반환하는 함수(검색)
def Qpeek():
    if front == rear:
        print('Queue_Empty')
    else:
        return Q[front+1]


# 비었는지 확인하는 함수(공백상태)
def isEmpty():
    return front == rear


# 가득인지 확인하는 함수(포화상태)
def Full():
    return rear == len(Q) - 1


# 삽입
def enQueue(item):
    global rear

    if rear == len(Q)-1:
        return 'Queue_Full'
    else:
        rear += 1
        Q[rear] = item


# 삭제
def deQueue():
    global front
    global rear

    if front == rear:
        return 'Queue_Empty'
    else:
        front += 1
        return Q[front]
```



---



## 원형 Queue

![image-20220225160644623](Queue.assets/image-20220225160644623.png)

![image-20220225160655374](Queue.assets/image-20220225160655374.png)



![image-20220225160747089](Queue.assets/image-20220225160747089.png)



![image-20220225160819822](Queue.assets/image-20220225160819822.png)



- 원형 Queue의 `front`는 항상 `-1` /  `rear`는 항상 `len(queue) - 1`
  - 따라서 따로 관리할 필요가 없음 

![image-20220225161734708](Queue.assets/image-20220225161734708.png)



```python
# 비었는지 확인하는 함수(공백상태)
def isEmpty():
    return front == rear

# 가득인지 확인하는 함수(포화상태)
def isFull():
    return (rear+1) % len(cQ) == front

# 삽입
def enQueue(item):
    global rear
    if (rear+1) % len(cQ) == front:
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item

# 삭제
def deQueue():
    global front
    if front == rear:
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]


cQ_size = 3
cQ = [0]*cQ_size

front = rear = 0

enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())
```



---



## 우선순위 Queue

![image-20220225162851835](Queue.assets/image-20220225162851835.png)



![image-20220225165159854](Queue.assets/image-20220225165159854.png)



![image-20220225165256412](Queue.assets/image-20220225165256412.png)



---



## Queue의 활용 - 버퍼

![image-20220225165318144](Queue.assets/image-20220225165318144.png)



![image-20220225165356840](Queue.assets/image-20220225165356840.png)



---



## BFS(너비 우선 탐색)

![image-20220225165502633](Queue.assets/image-20220225165502633.png)



![image-20220225165551927](Queue.assets/image-20220225165551927.png)



![image-20220225165636101](Queue.assets/image-20220225165636101.png)



![image-20220225165652587](Queue.assets/image-20220225165652587.png)



![image-20220225165710492](Queue.assets/image-20220225165710492.png)



![image-20220225165805098](Queue.assets/image-20220225165805098.png)



![image-20220225165814870](Queue.assets/image-20220225165814870.png)



![image-20220225165845135](Queue.assets/image-20220225165845135.png)



```python
def BFS(G, v, n):   # 그래프 G, 탐색 시작점 v, 정점의 개수 n
    visited = [0]*(n+1)     
    queue = list()              # 큐 생성
    queue.append(v)         # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:
        t = queue.pop(0)    # 큐의 첫 번째 원소 반환
        visit(t)            # visit(탐색시작점) 이라는 함수를 미리 만들어 놓기
        for i in G[t]:      # t와 연결된 모든 정점에 대해
            if not visited[i]:      # 방문되지 않은 곳이라면
                queue.append(i)     # 큐에 넣기
                visited[i] = visited[t] + 1      # n으로 부터 1만큼
```

