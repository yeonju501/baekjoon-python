import sys
sys.stdin = open('2941_input.txt')

arr = list(input())
i = cnt = 0
al = ['c', 'd', 'l', 'n', 's', 'z']
while i < len(arr):
    cnt += 1
    if arr[i] not in al:
        pass
    elif arr[i] == 'c':
        if i+1 < len(arr) and (arr[i+1] == '=' or arr[i+1] == '-'):
            i += 1
    elif arr[i] == 'd':
        if i + 1 < len(arr) and arr[i + 1] == '-':
            i += 1
        elif i+2 < len(arr) and arr[i+1] == 'z' and arr[i+2] == '=':
            i += 2
    elif arr[i] == 'n' or arr[i] == 'l':
        if i+1 < len(arr) and arr[i+1] == 'j':
            i += 1
    elif arr[i] == 's' or arr[i] == 'z':
        if i+1 < len(arr) and arr[i+1] == '=':
            i += 1
    i += 1
print(cnt)