import sys
sys.stdin = open('2621_input.txt')

def check1():
    for i in range(5):
        if letters[-1] != letters[i]:
            return 0
    for i in range(4):
        if num[i] + 1 != num[i+1]:
            return 0
    return num[-1] + 900

def check2():
    if num[0] == num[3] or num[1] == num[4]:
        return num[3] + 800
    else:
        return 0

def check3():
    if num.count(num[0]) == 2 and num.count(num[2]) == 3:
        return num[2] * 10 + num[0] + 700
    elif num.count(num[0]) == 3 and num.count(num[3]) == 2:
        return num[0] * 10 + num[3] + 700
    else:
        return 0

def check4():
    for i in range(5):
        if letters[-1] != letters[i]:
            return 0
    return num[-1] + 600

def check5():
    for i in range(4):
        if num[i] + 1 != num[i+1]:
            return 0
    return num[-1] + 500

def check6():
    for i in range(5):
        if num.count(num[i]) == 3:
            return num[i] + 400
    return 0

def check7():
    if num.count(num[0]) == 2 and (num.count(num[2]) == 2 or num.count(num[3]) == 2):
        return num[3] * 10 + num[0] + 300
    elif num.count(num[1]) == 2 and num.count(num[3]) == 2:
        return num[3] * 10 + num[1] + 300
    else:
        return 0

def check8():
    for i in range(5):
        if num.count(num[i]) == 2:
            return num[i] + 200
    return 0


letters = []
nums = []
for _ in range(5):
    l, n = input().split()
    letters.append(l)
    nums.append(int(n))
num = sorted(nums)
if check1():
    print(check1())
elif check2():
    print(check2())
elif check3():
    print(check3())
elif check4():
    print(check4())
elif check5():
    print(check5())
elif check6():
    print(check6())
elif check7():
    print(check7())
elif check8():
    print(check8())
else:
    print(100 + num[-1])



