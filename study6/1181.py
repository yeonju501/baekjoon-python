# 1. 전부 받아서 배열에 넣는다
# 2. 글자순으로 정렬
# 3. 길이가 같으면 사전술

import sys
sys.stdin = open('1181_input.txt')

N = int(input())
words_arr = set(input() for _ in range(N))
words_arr = list(words_arr)
words_arr.sort()
words_arr.sort(key=lambda x:len(x))
for i in range(len(words_arr)):
    print(words_arr[i])