a, b, k = list(map(int, input().split()))

ans = set([])
for i in range(a, min(a+k, b+1)):
    ans.add(i)
for i in range(max(a, b-k+1), b+1):
    ans.add(i)
for a in sorted(list(ans)):
    print(a)
