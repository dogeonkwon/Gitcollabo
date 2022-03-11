# deque(데크)

double-ended queue

: 앞과 뒤에서 즉, 양방향에서 데이터를 처리할 수 있는 queue형 자료구조를 의미한다. 



from collections import deque

해서 deque 불러오기

dq = deque()

```python
from collection import deque
dq = deque('love')
dq
# deque(['l','o','v','e'])
```

문자열을 이용해 deque를 만들면 각 문자가 요소로 된 리스트 형태의 deque가 만들어진다



- `deque.append(item)`: item을 데크의 오른쪽 끝에 삽입한다.
- `deque.appendleft(item)`: item을 데크의 왼쪽 끝에 삽입한다.

```python
dq.appendleft('l')
dq
# deque(['l','l','o','v','e'])
dq.pop()
# 'e'
dq
# deque(['l','l','o','v'])
```



- `deque.pop()`: 데크의 **오른쪽 끝 엘리먼트**를 가져오는 동시에 데크에서 삭제한다.
- `deque.popleft()`: 데크의 **왼쪽 끝 엘리먼트**를 가져오는 동시에 데크에서 삭제한다.
- `deque.extend(array)`: 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- `deque.extendleft(array)`: 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.

```python
dq
# deque(['l','o','v','e'])
dq.extend('you')
dq
# deque(['l','o','v','e','y','o','u'])

dq.extendleft('l')
dq
# deque(['l',l','o','v','e','y','o','u'])
```



- `deque.remove(item)`: item을 데크에서 찾아 삭제한다.
- `deque.rotate(num)`: 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

```python
dq
# deque(['l','o','v','e'])
dq[2]='n'
dq
# deque(['l','o','n','e'])
```



```python
dq = deque('love')
dq.insert(0,'k')
dq
# deque(['k','l','o','v','e'])
dq.insert(100, 'k')
dq
# deque(['k','l','o','v','e','k'])
dq.remove('k')
dq
# deque(['l','o','v','e,'k']) # 같은 항목이 있을 떄, 가장 왼쪽에 있는거 삭제
```

```python
dq
# deque(['l','o','v','e'])
dq.reverse()
dq
# deque(['e','v','o','l'])
```



queue와 stack 합치기가 queue