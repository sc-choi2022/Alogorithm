def star(n):
    if n == 1:
        return ['*']
    n = n//3
    t_b = [i*3 for i in star(n)]
    mid = [i + ' '*n + i for i in star(n)]
    return t_b + mid +t_b

n = int(input())
mstar =star(n)
for m in mstar:
    print(m)