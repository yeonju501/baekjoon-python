import sys
sys.stdin = open('1018_input.txt')

def check():
    global ans
    for x in range(N - 7):
        for y in range(M - 7):
            cnt = 0
            for i in range(8):
                for j in range(8):
                    if (x + i) % 2 == 0 and (y + j) % 2 == 0 and arr[x + i][y + j] == 'B':
                        cnt += 1
                    elif (x + i) % 2 == 0 and (y + j) % 2 == 1 and arr[x + i][y + j] == 'W':
                        cnt += 1
                    elif (x+i) % 2 == 1 and (y + j) % 2 == 0 and arr[x + i][y + j] == 'W':
                        cnt += 1
                    elif (x + i) % 2 == 1 and (y + j) % 2 == 1 and arr[x + i][y + j] == 'B':
                        cnt += 1
            else:
                if ans > cnt:
                    ans = cnt

def check2():
    global ans
    for x in range(N - 7):
        for y in range(M - 7):
            cnt = 0
            for i in range(8):
                for j in range(8):
                    if (x + i) % 2 == 0 and (y + j) % 2 == 0 and arr[x + i][y + j] == 'W':
                        cnt += 1
                    elif (x + i) % 2 == 0 and (y + j) % 2 == 1 and arr[x + i][y + j] == 'B':
                        cnt += 1
                    elif (x+i) % 2 == 1 and (y + j) % 2 == 0 and arr[x + i][y + j] == 'B':
                        cnt += 1
                    elif (x + i) % 2 == 1 and (y + j) % 2 == 1 and arr[x + i][y + j] == 'W':
                        cnt += 1
            else:
                if ans > cnt:
                    ans = cnt

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
ans = 987654321
check()
check2()
print(ans)
