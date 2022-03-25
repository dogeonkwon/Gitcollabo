# 배열 2

- ##### 배열 : 2차원 배열

- ##### 부분집합 생성

- ##### 바이너리 서치 (Binary Search)

- ##### 설렉션 알고리즘 (Selection Algorithm)

- ##### 선택 정렬 (Selection Sort)



## 2차원 배열의 선언

- 1차원 List를 묶어놓은 List
- 2차원 이사의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함



##### 2행 4열 2차원 List

 ex ) arr = [ [0,1,2,3], [4,5,6,7] ]

![image-20220207205418467](List2.assets\image-20220207205418467.png)



##### [참고]

```python
# 	3		입력값
#	1 2 3
#   4 5 6
#   7 8 9

N = int(input)
arr = [list(map(int,input().split())) for _ in range(N)]


# => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```



```python
#	3		입력값
#	123
#	456
#	789

N = int(input)
arr = [list(map(int,input())) for _ in range(N)]


# => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```



---



- ### 2차원 List 입력 받기

  ![image-20220207210101410](List2.assets\image-20220207210101410.png)

  - 첫째 줄에 n행 m열
  - 둘째 줄부터 n*m의 행열 데이터가 주어질 경우 입력을 받는 방법

```python
# 예시 1)

n, m = map(int, input().split())

mylist=[0 for _ in range(n)]
#mylist = [0]*n

for i in range(n):
    mylist[i] = list(map(int, input().split()))


# 시퀀스 자료형의 (곱셈)연산자로 반복을 이용하는 방법도 가능함
```



```python
# 예시 2)

n, m = map(int, input().split())
mylist=[]
for i in range(n):
    mylist.append(list(map(int, input().split())))

```



```python
# 예시 3)

n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]
```



---



- ### 2차원 List에서 원하는 데이터의 위치 찾기

  ![image-20220207211029783](List2.assets\image-20220207211029783.png)

  - 주어진 데이터에서 1 이 입력된 [행, 열]의 위치 찾기

```python
# 예시 1)

n, m = map(int, input().split())

newlist = []
mylist = [0 for _ in range(n)]
for i in range(n):
    mylist[i] = list(map(int,input().split()))
    for j in range(m):
        if mylist[i][j] == 1:
            newlist.append([i, j])
```



```python
# 예시 2)

n, m = map(int, input().split())
mylist = [list(map(int,input().split())) for _ in range(n)]

newlist = [[i, j] for i in range(n) for j in range(m) if mylist[i][j] == 1]
```



---



- ### List 순회

- n X m List의 n * m개의 모든 원소를 빠짐없이 조사하는 방법

- 행 우선 순회, 열 우선 순회, 지그재그 순회로 나뉜다.



> ### 행 우선 순회

List의 행을 우선으로 List의 원소를 조사하는 방법

![image-20220207211820674](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220207211820674.png)

```python
# 예시)

arr = [[0, 1, 2, 3],
	  [4, 5, 6, 7],
      [8, 9, 10, 11]]

# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] #필요한 수행
```





> ### 열 우선 순회

List의 열부터 먼저 조사하는 방법

![image-20220207212103005](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220207212103005.png)

```python
# 예시)

for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j] # 필요한 연산 수행
```



> ### 지그재그 순회

List의 행을 좌우로 조사하는 방법

![image-20220207212242459](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220207212242459.png)

![image-20220210231951234](C:\Users\kjmk1\AppData\Roaming\Typora\typora-user-images\image-20220210231951234.png)

* 이 때 열을 참조하는 인덱스의 값을 주의깊게 살펴봐야 함

```python
# 예시)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j + (len(arr[0]) - 1 -2 * j) * (i % 2)] # 필요한 연산 수행
```



---



- ### 델타를 이용한 2차 List 탐색

1.  2차 List의 한 좌표에서 <span style = "color: red">**네 방향의 인접 List 요소를 탐색**</span>할 때 사용하는 방법
2. 델타 값은 한 좌표에서 네 방향의 좌표와 x, y의  <span style = "color: red">**차이를 저장한 List로 구현**</span>
3. 델타 값을 이용하여  <span style = "color: red">**특정 원소의 상하좌우에 위치**</span>한 원소에 접근할 수 있음

 

> ### 전치 행렬

- 행과 열의 값이 반대인 행렬을 의미



![image-20220207212929449](List2.assets\image-20220207212929449.png)



```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]	# 3 * 3 행렬

for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j],arr[j][i] = arr[j][i], arr[i][j]
```



---



- 파이썬에서 import하지 않고 사용할 수 있는 함수로 zip(iterable*)이 있다.

> ### zip

- 동일한 개수로 이루어진 자료형들을 묶어 주는 역할을 하는 함수

![image-20220207213329516](List2.assets\image-20220207213329516.png)

- 각 List를 슬라이스하여 순서대로 튜플객체로 묶어줌
- 묶은 결과는 List나 딕셔너리로 변경해서 사용가능

![image-20220207213443181](List2.assets\image-20220207213443181.png)



---



[연습 문제 1]

- 5 X 5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
- 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
- 예를 들어 아래 그림에서 7 값의 이웃한 값은 2, 6, 8, 12 이며 차의 절대값의 합은 12이다.

![image-20220210223615807](List2.assets\image-20220210223615807.png)

- 25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
- 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.
  - 예를 들어 [0] [0]은 이웃한 요소가 2개이다.



---

---



## 2. 부분 집합

- 부분 집합의 합 문제 : 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분 집합 중에서 <span style="color: red">그 집합의 원소를 모두 더한 값이 0이 되는 경우</span>가 있는지를 알아내는 문제



```python
# 예시)

{-7, -3, -2, 5, 8}이 있을 때

{-3, -2, 5}는 부분 집합이면서 

(-3) + (-2) + 5 = 0 이므로

=> 답은 참이다!!!
```



- 풀이 팁
  - 완전 검색기법으로 부분 집합 합 문제를 풀기 위해서는 우선 집합의 모든 부분 집합을 생성한 후 <span style="color: red">각 부분 집합의 합을 계산</span>함
  - 주어진 집합의 <span style="color: red">부분 집합을 생성하는 방법</span> 생각해 보기



---



>### Loop를 이용하여 확인하고, 부분 집합을 생성하는 방법

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i							# 0번째 원소
    for j in range(2):
        bit[1] = j						# 1번째 원소
        for k in range(2):
            bit[2] = k					# 2번째 원소
            for l in range(2):
                bit[3] = l				# 3번째 원소
                print(bit)				# 생성된 부분집합 출력
```



![image-20220207215213824](List2.assets\image-20220207215213824.png)



![image-20220207215239349](List2.assets\image-20220207215239349.png)



- #### bit 리스트는 0과 1로 이루어진 리스트이다.

![image-20220207215439821](List2.assets\image-20220207215439821.png)



- #### 비트연산자 : 0과 1로 이루어진 이진수에 대한 연산을 수행하는 연산자

![image-20220207215945193](List2.assets\image-20220207215945193.png)



- #### 위의 방법보다 간결하게 부분 집합을 생성하는 방법

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)		# n: 원소의 개수

for i in range(1 << n):		# 1 << n: 부분 집합의 개수 / 몇 사이클 출력할 것인지 정함
    for j in range(n):		# 원소의 수만큼 비트를 비교함  <- 원소의 포함 여부 판단이 가능함
        if i&(1<<j):		# i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=',')
    print()
```



---

---



## 3. 검색



- ### 검색의 종류 : 순차 검색 / 이진 검색 / 인덱싱 



> ### 순차검색

1. 일렬로 되어 있는 자료를 <span style="color: red">순서대로 검색</span>하는 방법
2. List나 연결 List 등 <span style="color: red">순차구조로 구현된 자료구조</span>에서 유용함
3. 구현이 쉽지만, <span style="color: red">검색 대상이 많은 경우</span> 수행시간의 증가로 비효율적임



- ### 정렬되지 않은 자료의 검색 과정

![image-20220207222739410](List2.assets\image-20220207222739410.png)



![image-20220207223429901](List2.assets\image-20220207223429901.png)



- 찾고자 하는 원소의 순서에 따른 비교횟수 결정 
  - 첫 번째 원소를 찾을 때에는 1번 비교, 두 번째 원소를 찾을 때에는 2번 비교
  - 정렬되지 않은 자료에서의 순차 검색의 평균 비교 횟수 => 1 / n(1 + 2 + 3 + ... + n) = (n + 1) / 2
  - 시간 복잡도 : O(n)

```python
def sequentialSearch(a, n, key):
    i = 0
    while < n and a[i]!=key:
        i = i + 1

	if i<n: return i
    else: return -1
```



- ### 정렬된 자료의 검색 과정

![image-20220207223238635](List2.assets\image-20220207223238635.png)



![image-20220207223342194](List2.assets\image-20220207223342194.png)



- 찾고자 하는 원소의 순서에 따른 비교횟수 결정 

  - 정렬되어 있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어듦

  - 시간 복잡도 : O(n)

```python
def sequentialSearch2(a, n, key):
    i = 0
    while < n and a[i] < key:
        i = i + 1

	if i<n and a[i] == key : return i
    else: return -1
```





> ### 이진 검색

- 앞의 순차 검색보다 효율적인 방법
- 자료의 가운데 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 <span style="color: red">검색 범위를 반으로 줄여가면서 빠르게 검색</span>을 수행함
- 이진 검색을 하기 위해서는 <span style="color: red">자료가 정렬된 상태</span>여야 함
- 정렬된 데이터 n개가 있는 경우의 시간복잡도 -> 순차 검색 시 O(N)의 시간이 걸리지만, 이진 검색 시 O(logN)의 시간이 걸림



![image-20220207224422788](List2.assets\image-20220207224422788.png)

 

![image-20220207224514303](List2.assets\image-20220207224514303.png)

 

![image-20220207224601853](List2.assets\image-20220207224601853.png)



- 검색 범위의 시작점과 종료점을 이용

  - 검색 범위의 <span style="color: red">시작점과 종료점을 이용하여 검색을 반복 수행</span>함

  - 이진 검색의 경우, 자료에 삽입이나 삭제가 발생하였을 때 <span style="color: red">List의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요함</span>

```python
def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if key == a[middle]:	# 검색 성공
            return True
        elif key < a[middle]:
            end = middle - 1
		else:
            start = middle + 1
 	return Flase	# 검색 실패 
```



```python
# 재귀 함수를 이용한 이진 검색 구현

def binarySearch2(a, low, high, key):
    if low > high:	# 검색 실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]: # 검색 성공
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle - 1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle + 1, high, key)
```





> ### 인덱스

- 데이터베이스에서 유래, 테이블에 대한 동작 속도를 높임
- 룩 업 테이블(Look up table) 등의 용어로 사용함
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블 저장에 필요한 디스크 공간보다 작음
  - 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목은 갖고 있지 않음
- List를 사용한 인덱스
  - 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없음. 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 List 인덱스를 사용할 수 있음



![image-20220207225510576](List2.assets\image-20220207225510576.png)



---

---



## 4. 정렬

- #### 셀렉션 알고리즘

  - 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
  - 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 함



![image-20220207230244368](List2.assets\image-20220207230244368.png)



- k가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로 함

```python
# 예) k번째로 작은 원소를 찾는 알고리즘 - 1번부터 k번째까지 작은 원소들을 찾아 List의 앞쪽으로 이동시키고, List의 k번째를 반환


def select(list, k):
    for i in range(0, k):
        minindex = i
        for j in range(i + 1, len(list)):
            if list[minindex] > list[j]:
                minindex = j
 		list[i], list[minindex] = list[minindex], list[i]
 	return list[k-1]
```





- #### 선택 정렬

  - 주어진 자료들 중 <span style="color: red">가장 작은 값의 원소부터 차례대로</span> 선택하여 위치를 교환하는 방식
  - 셀렉션 알고리즘을 전체 자료에 적용한 것
  - 정렬 과정
    - 주어진 List 중에서 <span style="color: red">최소값을 찾음</span>
    - 그 값을 List의 맨 앞에 위치한 값과 교환
    - 맨 처음 위치를 제외한 나머지 List를 대상으로 위의 과정을 반복
  - 시간 복잡도 : O(n^2)



![image-20220207231208545](List2.assets\image-20220207231208545.png)



![image-20220207232019957](List2.assets\image-20220207232019957.png)



![image-20220207231957279](List2.assets\image-20220207231957279.png)



```python
def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
      	a[i], a[min] = a[min], a[i]
```



- ##### 정렬 알고리즘의 특성 비교

![image-20220207232219137](List2.assets\image-20220207232219137.png)



![Screen-Shot-2019-02-07-at-2.31.54-PM-1](List2.assets\Screen-Shot-2019-02-07-at-2.31.54-PM-1.png)



https://blog.chulgil.me/algorithm/
