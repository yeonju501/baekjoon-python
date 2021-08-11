# 3 3 곱한다 두번째 첫째 자리 곱한 것 / 둘째 자리 곱한것 / 셋째자리 곱한것 출력
# 0을 넣는다 마지막에 0 rstrip
# 숫자들끼리 더해서 최종 출력

num1 = int(input())
num2 = int(input())
print(num1 * (num2%10))
print((num1 * (num2%100//10) * 10)//10)
print((num1 * (num2//100) * 100)//100)
print(num1 * (num2%10) + (num1 * (num2%100//10) * 10) + (num1 * (num2//100) * 100))