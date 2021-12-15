import sys
sys.stdin = open('10844_input.txt')

N = int(input())
arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

for i in range(1, N):
    temp = []
    for j in range(len(arr[i-1])):
        num = int(arr[i-1][j])
        if num % 10 == 0:
            temp.append(num * 10 + num % 10 + 1)
        elif num % 10 == 9:
            temp.append(num * 10 + num % 10 - 1)
        else:
            temp.append(num * 10 + num % 10 - 1)
            temp.append(num * 10 + num % 10 + 1)
    arr.append(temp)
for i in range(N):
    print(len(arr[i]))

