import sys
sys.stdin = open('1501_input.txt')
# input = sys.stdin.readline
def perm(k, w):
    if k == len(word):
        words.append(m[0] + w + m[-1])
        return
    else:
        for i in range(len(word)):
            if not used[i]:
                used[i] = 1
                perm(k+1, w + word[i])
                used[i] = 0

N = int(input())
arr = []
for i in range(N):
    words = []
    m = input()
    word = m[1: -1]
    used = [0] * len(word)
    perm(0, '')
    words = set(words)
    arr.append(words)
print(arr)
M = int(input())
for i in range(M):
    cnt = 0
    sentence = input()
    for j in range(N):
        if sentence in arr[j]:
            cnt += 1
    print(cnt)

