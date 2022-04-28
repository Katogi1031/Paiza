import numpy as np
n, h, w, p, q = map(int, input().split())
seat = np.zeros((h, w))

for i in range(n):
    x, y = map(int, input().split())
    seat[x][y] = 99

m = 99
for i in range(h):
    for j in range(w):
        if seat[i][j] != 99:
            seat[i][j] = abs(p-i) + abs(q-j)
        if m > seat[i][j]:
            m = seat[i][j]

for i in range(h):
    for j in range(w):
        if seat[i][j] == int(m):
            print(i, j)
