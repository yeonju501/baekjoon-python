import sys
sys.stdin = open('1501_input.txt')

def check(word):
    m = sorted(list(word[1:-1]))
    cnt = 0
    for i in range(len(dic)):
        if len(dic[i]) == len(word):
            if dic[i][0] == word[0] and dic[i][-1] == word[-1]:
                if m == sorted(list(dic[i][1:-1])):
                    cnt += 1
    return cnt

N = int(input())
dic = [input() for _ in range(N)]
M = int(input())

for i in range(M):
    sentence = list(input().split())
    ans = 1
    for word in sentence:
        ans *= check(word)
    print(ans)