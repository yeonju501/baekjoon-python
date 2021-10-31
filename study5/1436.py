import sys
sys.stdin = open('1436_input.txt')

def find():
    global ans
    cnt = 0
    for num in range(666, 10000001):
        s = str(num)
        for i in range(len(s)-1, 1, -1):
            if s[i] == '6' and s[i-1] == '6' and s[i-2] == '6':
                cnt += 1
                if cnt == N:
                    ans = num
                    return
                break

N = int(input())
ans = 0
find()
print(ans)


