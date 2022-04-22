#입력 받은 숫자가 소수인지 판별
import math



def numberCheck(num):

    if num == 0 or num == 1:
        return False
    else:
#sqrt 제곱근
        for i in range(2, int(math.sqrt(num)) + 1):
            print(i)
            if num % i == 0:
                return False
    return True


print(numberCheck(10))


print(numberCheck(1000000))