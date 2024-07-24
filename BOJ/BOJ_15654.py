from itertools import permutations

# N개의 자연수 중에서 M개를 고른 수열의 N, M
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

# 순열을 이용하여 M개의 수열을 저장하는 배열 permu
permu = list(permutations(numbers, M))

# 수열을 증가하는 순서로 공백으로 구분하여 출력한다.
for p in permu:
    print(*p)