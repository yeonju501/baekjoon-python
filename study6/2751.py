import sys
sys.stdin = open('2751_input.txt')
from collections import deque
input = sys.stdin.readline
# def merge(left, right):
#     result = []
#     left = deque(left)
#     right = deque(right)
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.popleft())
#         else:
#             result.append(right.popleft())
#
#     if left:
#         result.extend(left)
#     elif right:
#         result.extend(right)
#     return result
#
# def merge_sort(a):
#     if len(a) == 1:
#         return a
#     else:
#         mid = len(a) // 2
#         left = a[:mid]
#         right = a[mid:]
#
#         left = merge_sort(left)
#         right = merge_sort(right)
#
#         m = merge(left, right)
#         return m

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)

        left_idx = 0
        right_idx = 0
        i = 0

        while left_idx < len(left) and right_idx < len(right):
            # 두 부분집합의 요소가 모두 남아있을 때
            if left[left_idx] <= right[right_idx]:
                arr[i] = left[left_idx]
                left_idx += 1
            else:
                arr[i] = right[right_idx]
                right_idx += 1
            i += 1

        if left_idx < len(left):
            arr[i:] = left[left_idx:]
        elif right_idx < len(right):
            arr[i:] = right[right_idx:]

        return arr
N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())

arr = merge_sort(arr)
for i in range(N):
    print(arr[i])