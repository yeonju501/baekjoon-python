#행열을 제대로.. 이름 똑바로 짓기
words = input().strip().split()
word1 = words[0]
word2 = words[1]
j_idxs = []
i_idxs = []
for i in range(len(word1)):
    if word1[i] in word2:
        col = i
        row = word2.index(word1[i])
        break
for j in range(len(word2)):
    if j == row:
        print(word1)
    else:
        print('.'*col + words[1][j] + '.'*(len(word1)-col-1))

