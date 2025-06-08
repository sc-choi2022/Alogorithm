import sys

# 준현과 성민의 현금 M
M = int(sys.stdin.readline())
# 주가를 저장하는 배열 stocks
stocks = list(map(int, sys.stdin.readline().split()))
# 주가의 등락을 저장하는 배열 UD
UD = [0] * 14

# 준현과 성민 각각의 현금과 주식수 M1, S1, M2, S2
M1, S1, M2, S2 = M, 0, M, 0

for i in range(1, 14):
    if stocks[i-1] < stocks[i]:
        if UD[i-1] > 0:
            UD[i] = UD[i-1] + 1
        else:
            UD[i] = 1
    elif stocks[i-1] > stocks[i]:
        if UD[i-1] < 0:
            UD[i] = UD[i-1] - 1
        else:
            UD[i] = -1
    else:
        UD[i] = 0

for j in range(14):
    if M1//stocks[j]:
        S1 += M1//stocks[j]
        M1 = M1%stocks[j]
    if UD[j] == 3:
        M2 += S2*stocks[j]
        S2 = 0
    elif UD[j] <= -3:
        S2 += M2//stocks[j]
        M2 -= M2//stocks[j]*stocks[j]

# 준현의 자산 T1, 성민의 자산 T2
T1, T2 = M1+S1*stocks[13], M2+S2*stocks[13]

# 준현의 자산이 더 큰 경우
if T1 > T2:
    print('BNP')
# 성민의 자산이 더 큰 경우
elif T1 < T2:
    print('TIMING')
# 둘의 자산이 같은 경우
else:
    print('SAMESAME')