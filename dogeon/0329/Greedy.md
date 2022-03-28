# 탐욕 알고리즘



## 탐욕 알고리즘 소개

- ##### 최적화 문제를 해결하는 알고리즘

![image-20220328110714683](Greedy.assets/image-20220328110714683.png)



- 탐욕 알고리즘이 항상 최적해를 찾을 수 있는지 검증해야 한다.

![image-20220328110836247](../../../My_TIL/self_study/06_Algorithm/greedy.assets/image-20220328110836247-16484659638561.png)





## 탐욕 알고리즘 동작 과정

![image-20220328111012132](../../../My_TIL/self_study/06_Algorithm/greedy.assets/image-20220328111012132-16484659672202.png)





## 탐욕 알고리즘 문제 예시



- ### 동전 거스름돈 문제

![image-20220328111136838](Greedy.assets/image-20220328111136838.png)



1. ##### 해 선택 단계

- 가장 좋은 해 선택
- 단위가 큰 동전으로만 거스름돈을 만들면 동전의 개수가 줄어드므로 <span style= "color:red">**현재 고를 수 있는 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가**</span>

2. ##### 실행 가능성 검사

- <span style= "color:red">**거스름돈**</span>이 손님에게 내드려야 할 <span style= "color:red">**액수를 초과하는지 확인**</span>
- 초과할 경우 마지막에 추가한 동전을 거스름돈에서 빼고, 1로 돌아가서 현재보다 한 단계 작은 단위의 동전 추가

3. ##### 해 검사

- <span style= "color:red">**거스름돈 문제의 해**</span> = 손님에게 내드려야 하는 거스름돈의 액수
- 거스름돈을 확인해서 애굿에 모자라면 다시 1로 돌아가서 거스름돈에 추가할 동전 선택



#### -풀이 예시-

- ##### Case 1

![image-20220328111834501](Greedy.assets/image-20220328111834501.png)

1. ##### 해 선택 단계

- 거스름돈 금액 0원에서 시작
- 해 선택 - 선택할 수 있는 가장 큰 금액의 동전 선택



![image-20220328111845631](Greedy.assets/image-20220328111845631.png)

2. ##### 실행 가능성 검사

- 거스름돈 금액이 800원을 초과하지 않음

- 만약 800원을 초과한다면 추가했던 동전을 빼고 그 다음 큰 동전을 넣어서 비교해 본다.



![image-20220328111910946](Greedy.assets/image-20220328111910946.png)

3. ##### 해 검사

- 아직 800원이 되지 않음
- 다시 1번 부터 시작



=> 해 = 선택한 동전들의 집합 : 500, 100, 100, 100





- ##### case 2(400원 동전 종류 추가)

![image-20220328111937674](Greedy.assets/image-20220328111937674.png)

- ##### 가장 큰 동전을 선택하는 탐욕 방법으로는 최적해를 구할 수 없다!

- 탐욕 알고리즘에서 최종적인 해답을 만들었어도 최적이라는 보장은 없음



![image-20220328111958239](Greedy.assets/image-20220328111958239.png)

- ##### 완전 검색 적용

- 800원에서부터 선택한 동전의 금액 차감

- 가능한 모든 경우를 따져 보기 위해 5가지 동전 모두를 선택하면서 거스름돈 금액을 차감

- 동전을 선택하는 과정에서 금액이 음수가 되면 중단하고 다른 선택을 계속 해 나간다.





![image-20220328112055366](Greedy.assets/image-20220328112055366.png)

- 금액이 0원이 되면 조건에 만족하는 동전들의 집합 중 하나를 찾게 된다.
- 원하는 집합을 찾게 되지만 동전의 개수가 많을 수록 시간복잡도가 증가하게 된다.



---



- ### 배낭 문제



![image-20220328152057820](Greedy.assets/image-20220328152057820.png)



![image-20220328152157951](Greedy.assets/image-20220328152157951.png)





- ### 0-1 Knapsack 문제의 경우

- ##### 완전 검색 적용

![image-20220328152242566](Greedy.assets/image-20220328152242566.png)



- ##### 탐욕 기법 적용(값이 비산 물건부터 채우기)

![image-20220328152412520](Greedy.assets/image-20220328152412520.png)



- ##### 탐욕 기법 적용(무게가 가벼운 물건부터 채우기) - 물건1의 가격이 15만원으로 변경

![image-20220328152505906](Greedy.assets/image-20220328152505906.png)



- ##### 탐욕 기법 적용(무게당 값이 높은 물건부터 채우기) - 물건 1, 2, 3의 무게와 값이 변경

![image-20220328152536693](Greedy.assets/image-20220328152536693.png)



#### => 탐욕적 방법으로는 배낭문제를 풀 수 없다. 따라서 완전탐색을 해야 한다.





- ### Fractional Knapsack 문제 의 경우

![image-20220328152749146](Greedy.assets/image-20220328152749146.png)

- 무게만큼 가치를 가지게 됨
- 무게 당 가치가 가장 큰 물건 1을 선택
- 물건 3을 선택
- 이 후에도 배낭에 공간이 남으므로 남은 물건 2를 절반 잘라서 담는다.



#### => 실제 가능한 해는 아니고 이상적으로 구할 수 있는 해

배낭문제의 상태공간 트리를 탐색할 때 분기한정을 위한 한정값을 계산하는데 사용된다.



---



- ###  활동 선택 문제

- ##### 대표적인 예시 문제 - 회의실 배정 문제

![image-20220328154008045](Greedy.assets/image-20220328154008045.png)

- 탐욕적 방법을 적용해 최적해를 구할 수 있다.

- 하나의 회의를 하나의 활동으로 본다.



- #### 탐욕 기법 적용

![image-20220328154133101](Greedy.assets/image-20220328154133101.png)

- a0과 a(n+1)를 추가해서 정렬한다.
- a0 : 종료시간이 0인 활동
- a(n+1) : 시작시간이 무한대인 활동



![image-20220328154223143](Greedy.assets/image-20220328154223143.png)

- ai의 종료시간으로 부터 am의 시작시간 사이에 포함되는 활동이 없기 때문에 Si,m은 공집합이 된다.
- 이 후, Sm,j 가 남는다.



![image-20220328154259899](Greedy.assets/image-20220328154259899.png)





![image-20220328154323070](Greedy.assets/image-20220328154323070.png)





![image-20220328154337212](Greedy.assets/image-20220328154337212.png)





![image-20220328154403145](Greedy.assets/image-20220328154403145.png)





![image-20220328154424574](Greedy.assets/image-20220328154424574.png)



- #### 탐욕 기법 검증

![image-20220328154515765](Greedy.assets/image-20220328154515765.png)





![image-20220328154603959](Greedy.assets/image-20220328154603959.png)





![image-20220328154655916](Greedy.assets/image-20220328154655916.png)

 



![image-20220328154725937](Greedy.assets/image-20220328154725937.png)





---



- ### Baby-Gin 문제



![image-20220328153521900](Greedy.assets/image-20220328153521900.png)





![image-20220328153619225](Greedy.assets/image-20220328153619225.png)

- 1~0까지 counts 리스트를 생성한 뒤 입력된 숫자의 개수를 삽입한다.
- 숫자가 3개 연속이면 run 성립. 이 후, counts에서 -1씩 해주기
- 한 인덱스에 3개 이상의 숫자가 있다면 triplet 성립. 이 후, counts에 -3 해주기

- run + triplet = 2 라면, Baby-Gin 성립!!



![image-20220328153633808](Greedy.assets/image-20220328153633808.png)

