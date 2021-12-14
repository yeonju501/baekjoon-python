import sys
sys.stdin = open('7490_input.txt')

def perm(k, ex):
    if k == (N*2-1):
        gap = [int(ex[0])]
        for i in range(1, N*2-1, 2):
            if ex[i] == '+':
                gap.append(int(ex[i+1]))
            elif ex[i] == '-':
                gap.append(int(ex[i+1]) * -1)
            elif ex[i] == ' ':
                if gap[-1] > 0:
                    gap[-1] = gap[-1] * 10 + int(ex[i+1])
                else:
                    gap[-1] = gap[-1] * 10 - int(ex[i+1])
        hap = 0
        for i in range(len(gap)):
            hap += gap[i]
        if hap == 0:
            ans.append(ex)
    else:
        if k % 2 == 0:
            perm(k+1, ex + str(nums[k//2]))
        elif k % 2:
            for j in range(3):
                perm(k+1, ex + op[j])


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(range(1, N+1))
    op = [' ', '+', '-']
    ans = []
    perm(1, str(nums[0]))
    print(*ans, sep='\n')
    print()