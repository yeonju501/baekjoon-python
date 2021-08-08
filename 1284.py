# 각 숫자 1 여백
# 1 은 2 0은 4 나머지는 3 앞뒤 1
import sys
while True:
    num = sys.stdin.readline().strip()
    cm = 1
    if num == '0':
        break
    else:
        for i in range(len(num)):
            if num[i] == '0':
                cm += 5
            elif num[i] == '1':
                cm += 3
            else:
                cm += 4
    print(cm)
