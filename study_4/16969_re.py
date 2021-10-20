import sys
sys.stdin = open('16969_input.txt')

a = input()
if a[0] == 'c':
    ans = 26
if a[0] == 'd':
    ans = 10
for i in range(1, len(a)):
    if a[i] == 'c':
        if a[i-1] == a[i]:
            ans *= 25
            ans %= 1000000009
        else:
            ans *= 26
            ans %= 1000000009
    elif a[i] == 'd':
        if a[i-1] == a[i]:
            ans *= 9
            ans %= 1000000009
        else:
            ans *= 10
            ans %= 1000000009

print(ans)
