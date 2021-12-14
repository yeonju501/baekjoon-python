import sys
from copy import deepcopy
sys.stdin = open('16677_input.txt')

m = input()
N = int(input())
w = [input().split() for _ in range(N)]
words = deepcopy(w)
for i in range(N):
    cnt = 0
    for j in range(len(m)): # 한 단어씩 검사하는 중
        if m[j] in words[i][0]:
            for l in range(len(words[i][0])):
                if m[j] != words[i][0][l]:
                    cnt += 1
                else:
                    words[i][0] = words[i][0][l+1:] # 같으면 자르기
                    break
        else:
            words[i].append(-1)
            break
    else:
        cnt += len(words[i][0])
        if cnt > 0:
            words[i].append(int(words[i][1])/cnt)

ans = words.index(max(words, key=lambda x:x[2]))
if words[ans][2] == -1:
    print('No Jam')
else:
    print(w[ans][0])

