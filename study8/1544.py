import sys
sys.stdin = open('1544_input.txt')

N = int(input())
arr = [input() for _ in range(N)]
j = cnt = 0
while arr:
    word = arr[0]
    cnt += 1
    for i in range(len(word)):
        while (word[i:] + word[len(word) * -1: (len(word) - i) * -1]) in arr:
            arr.remove(word[i:] + word[len(word) * -1: (len(word) - i) * -1])
            N -= 1
print(cnt)
