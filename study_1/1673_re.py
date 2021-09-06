# 치킨 쿠폰 n장 가지고 있고 한 마리를 주문할 때마다 도장을 하나씩, k개 모으면 치킨
# 치킨 최대 몇마리?
while True:
    try:
        n, k = map(int, input().split())
        chicken = n
        while n // k:
            chicken += n//k
            n = n // k + n % k
        print(chicken)
    except:
        break



