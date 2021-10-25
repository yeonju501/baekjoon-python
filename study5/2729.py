import sys
sys.stdin = open('2729_input.txt')

for tc in range(1, int(input())+1):
    a, b = input().split()
    a = int(a, 2)
    b = int(b, 2)
    ans = str(bin(a+b))

    print(ans[2:])
