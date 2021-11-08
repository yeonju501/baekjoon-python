import sys
sys.stdin = open('2108_input.txt')

import collections
input = sys.stdin.readline
N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
arr.sort()
a = sum(arr) / N
print(f'{a:.0f}') # 산술 평군
print(arr[N//2]) # 중앙값
c = collections.Counter(arr)
sorted_c = c.most_common()
if len(sorted_c) > 1:
    if sorted_c[0][1] == sorted_c[1][1]:
        print(sorted_c[1][0])
    else:
        print(sorted_c[0][0])
else:
    print(sorted_c[0][0])
print(max(arr)-min(arr)) # 범위