# 고대 그리스 수학자 에라토스테네스가 만든 소수 찾는 알고리즘
# 소수 : 1과 자기 자신만을 약수를 가지는 숫자
# 예 : 2, 3, 5, 7, 11 등
#
# 알고리즘 동작 과정
# 가정사항 : 2부터 15까지 숫자 중에 소수 찾기
# 1은 소수가 아니기 때문에 2부터 시작
#
# 모든 경우의 수를 나열
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

import math

su =[2,3,4,5,6,7,8,9,10,11,12,13,14,15]

max_su = max(su)
print("max_su", max_su)

for i in su:
    ##sqrt 제곱근
    if math.sqrt(i) < max_su:

        for j in su:

            if j > 1 and j%i == 0:
                print("i:",i,"/j:",j)

                su.remove(j)

print(su)