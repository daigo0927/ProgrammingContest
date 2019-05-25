h, w = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k]+c[k][j])

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == -1:
            continue
        else:
            ans += c[a[i][j]][1]
print(ans)
