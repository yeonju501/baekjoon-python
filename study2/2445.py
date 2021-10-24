T = int(input())
arr = [['*'] * (T*2) for _ in range(2*T-1)]
for i in range(len(arr)):
    for j in range(2*T):
        if i > (2*T-1)//2:
            if 2*T-i-1 <= j <= i:
                arr[i][j] = ' '
            else:
                continue
        else:
            if i < j < 2*T-i-1:
                arr[i][j] = ' '
            else:
                continue
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end='')
    print()