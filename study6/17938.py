import sys
sys.stdin = open('17938_input.txt')

N = int(input())
P, T = map(int, input().split())
j = 1
arm = flag = 0
for i in range(T):
    arm += j
    arm %= N*2
    if not flag:
        j += 1
    else:
        j -= 1
    if j == (N*2):
        flag = 1
    elif j == 1:
        flag = 0
print(arm)













