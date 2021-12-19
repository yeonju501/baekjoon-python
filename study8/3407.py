import sys
sys.stdin = open('3407_input.txt')
# input = sys.stdin.readline


arr = ['H',	'He', 'Li', 'Be', 'B', 'c',	'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc',
       'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb',
       'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'Hf', 'Ta', 'W', 'Re', 'Os',
       'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg',
       'Cn', 'Fl', 'Lv', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Ac', 'Th',
       'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
N = int(input())
for i in range(len(arr)):
    arr[i] = arr[i].lower()
for _ in range(N):
    word = input()
    dp = [0] * len(word)
    for i in range(len(word)):
        if word[i] in arr:
            dp[i] = 1
        if len(word) - 1 > i and word[i] + word[i+1] in arr:
            dp[i] = 1
            dp[i+1] = 1

    if 0 in dp:
        print('NO')
    else:
        print('YES')

