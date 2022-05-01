import numpy as np
n, m = map(int, input().split())

np.l = []
for i in range(n):
    np.l.append(input().split())
for i in range(n):
    for j in range(m):
        if np.l[i][j].isdigit() and 0 <= int(np.l[i][j]) <= 100: #文字列が数値であり、0以上100以下であるか
            np.l[i][j] = int(np.l[i][j])
        else:
            np.l[i][j] = '-' #欠損値であれば'-'と置換する
            
for i in range(m):
    s = 0
    cnt = 0

    for j in range(n):
        if np.l[j][i] != '-':
            cnt += 1
            np.l[j][i] = int(np.l[j][i])
            s += np.l[j][i]

    if cnt > 0:
        print(s//cnt)
    else:
        print(0) #データが0個の場合は0を出力
    
    
