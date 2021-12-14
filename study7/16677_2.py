import sys
sys.stdin = open('16677_input.txt')
m = input()
N = int(input())
j = 0
dap = {}
flag = 0
for i in range(N) :
    w, g = input().split()
    for i in w :
        if i == m[j] and flag == 0 :
            j += 1
            if j == len(m)  :

                ans = int(g) // (len(w) - len(m))
                dap[w] = ans
                j = 0
                flag = 1
    j = 0
    flag = 0


if dap :
    sort_arr = (sorted(dap.items(), key = lambda item: item[1], reverse=True))
    print(sort_arr[0][0])
else :
    print('No Jam')