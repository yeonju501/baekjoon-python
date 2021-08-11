# 치킨 쿠폰 n장 k개 모으면 치킨
# 치킨 최대 몇마리?
import sys
sys.stdin = open('1673_input.txt')
for i in range(3):
    n, k = map(int, input().split())
    ck = 0
    coupon = 0
    while True:
        if n > 0:
            ck += 1
            coupon += 1
            n -= 1
        elif n == 0:
            if coupon >= k:
                ck += 1
                coupon -= k
                coupon += 1
                if k <= 0:
                    break
            else:
                break
    print(ck)

