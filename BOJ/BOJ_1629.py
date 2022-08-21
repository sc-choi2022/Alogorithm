def func(A, B, C):
    if B == 1:
        return A%C
    else:
        k = func(A, B//2, C)
        if B%2==0:
            return k*k%C
        else:
            return k*k*A%C


# 자연수 A, B, C
A, B, C = map(int, input().split())
print(func(A,B,C))