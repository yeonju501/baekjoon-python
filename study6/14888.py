# 수의 개수 2개 둘째줄에는 A 덧뺄곱나의 개수
# 연산자만 골라주면 된다?
import sys
sys.stdin = open('14888_input.txt')
def perm(n, k):
    global m, M
    if n == k:
        val = arr[0]
        for i in range(1, l):
            if c[i-1] == 0:
                val += arr[i]
            elif c[i-1] == 1:
                val -= arr[i]
            elif c[i-1] == 2:
                val *= arr[i]
            elif c[i-1] == 3:
                if val < 0:
                    val *= -1
                    val //= arr[i]
                    val *= -1
                else:
                    val //= arr[i]
        if val > M:
            M = val
        if val < m:
            m = val
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                c[k] = op[i]
                perm(n, k+1)
                used[i] = 0

l = int(input())
N = l-1
arr = list(map(int, input().split()))
nums_op = list(map(int, input().split()))
op = []
for i in range(4):
    for j in range(nums_op[i]):
        op.append(i)
c = [0] * N
used = [0] * N
M = -987654321242
m = 9876543219
perm(N, 0)
print(M)
print(m)

"""
남의 코드
M = -1000000000
m = 1000000000
def f(nums, idx, result, plus, minus, multi, divide):
    if (plus == minus == multi == divide == 0):
        global M
        global m
        if (result > M):
            M = result
        if (result < m):
            m = result
    else:
        nextNum = nums[idx]
        if (plus != 0):
            f(nums, idx+1, result+nextNum, plus-1, minus, multi, divide)
        if (minus != 0):
            f(nums, idx+1, result-nextNum, plus, minus-1, multi, divide)
        if (multi != 0):
            f(nums, idx+1, result*nextNum, plus, minus, multi-1, divide)
        if (divide != 0):
            if (result < 0):
                f(nums, idx+1, -((-result)//nextNum), plus, minus, multi, divide-1)
            else:
                f(nums, idx+1, result//nextNum, plus, minus, multi, divide-1)

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

f(nums, 1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(M)
print(m)
"""