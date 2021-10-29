import sys
sys.stdin = open('2231_input.txt')

N = int(input())
arr = list(range(1, N+1))
for num in arr:
    s = str(num)
    hap = 0
    for i in range(len(s)):
        hap += int(s[i])
    if num + hap == N:
        print(num)
        break
else:
    print(0)