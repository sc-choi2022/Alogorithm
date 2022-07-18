# 문자열의 길이 L
L = int(input())
# 문자열 혹은 수열을 하나의 정수로 치환하기 위해 사용할 딕셔너리 alpha
alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
         'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
         'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
         'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
# mod M하여 출력할 정답 ans
ans = 0
# 주어지는 문자열 words
words = input()
# 주어진 서로소 r, M의 값을 각 31, 1234567891로 할당
r = 31
M = 1234567891
# 수식에 맞게 for문을 사용하여 계산
for i in range(len(words)):
    ans += alpha[words[i]] * r ** i
# ans mod M을 출력
print(ans%M)