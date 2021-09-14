import sys
sys.stdin = open('12981_input.txt')
arr = list(map(int, input().split()))
m = min(arr)
cnt = m
for i in range(3):
    arr[i] -= m
for i in range(len(arr)):
    if arr[i] >= 3:
        cnt += arr[i]//3
        arr[i] = arr[i]%3

while len(arr) != 0:
    while 0 in arr:
        arr.remove(0)
    if len(arr) == 2:
        m = min(arr)
        arr[0] -= m
        arr[1] -= m
        cnt += m
    elif len(arr) == 1:
        cnt += 1
        arr[0] = 0
print(cnt)




