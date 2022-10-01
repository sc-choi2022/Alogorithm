N, L = map(int, input().split())
t = 0
x = -1
it = 0
for i in range(L, 101):
    t = (i*i-i)//2
    if (N - t)%i == 0 and (N-t)//i >= 0:
        x = (N - t)//i
        it = i
        break
if x == -1:
    print(-1)
else:
    for j in range(it):
        print(int(x+j), end=' ')