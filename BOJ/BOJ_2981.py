import sys,math

# 주어지는 숫자의 개수 N
N = int(sys.stdin.readline())
# N개의 숫자를 담을 리스트 numbers
numbers = [int(sys.stdin.readline()) for _ in range(N)]
# numbers를 정렬
numbers.sort()
# numbers의 값들을 나누어서 같은 나머지가 나오는 M을 찾아야한다.
# numbers의 값들을 정렬 후 빼준 값의 약수가 M이 되는 값을 찾으면 동일한 값들을 찾을 수 있다.
# 이를 위해 정렬된 숫자를 뺀 값을 넣어 줄 리스트 modify를 만든다.
modify = [0] * (N-1)
for i in range(N-1):
    modify[i] = numbers[i + 1] - numbers[i]
# modify의 값들에서 최대 공약수를 구하고 변수 key_num에 할당한다.
key_num = math.gcd(*modify)
# 최대 공약수의 약수를 1을 제외하고 출력한다.
for k in range(2, key_num + 1):
    if key_num % k == 0:
        print(k, end=' ')