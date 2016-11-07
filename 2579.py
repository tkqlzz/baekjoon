score = [0]
add = [0]
n = int(input())
for _ in range(n):
    add.append(int(input()))
for i in range(1, n + 1):
    if i == 1:
        score.append(score[0] + add[1])
    elif i == 2:
        score.append(score[1] + add[2])
    else:
        score.append(max(add[i] + score[i - 2], add[i] + add[i - 1] + score[i - 3]))
print(score[n])