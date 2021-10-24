import sys
sys.stdin = open('9047_input.txt')

T = int(input())
for tc in range(T):
    i = 0
    num = int(input())
    while num != 6174:
        n = list(str(num))
        num = int(''.join(sorted(n, reverse=True))) - int(''.join(sorted(n)))
        if num < 1000:
            sn = str(num)
            for _ in range(4 - len(sn)):
                sn += '0'
            n = int(sn)
        i += 1
    print(i)

