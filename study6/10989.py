import sys
sys.stdin = open('10989_input.txt')
input = sys.stdin.readline
def counting_sort(A, B, k):
    C = [0] * k
    # 카운팅
    for i in range(len(A)):
        C[A[i]] += 1
    # 누적
    for i in range(1, len(C)):
        C[i] += C[i-1]
    # 결과 배열의 해당 위치에 넣기
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
s = max(arr)
a = [0] * N
counting_sort(arr, a, s+1)
for i in range(N):
    print(a[i])