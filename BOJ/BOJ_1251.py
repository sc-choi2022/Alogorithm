import sys

# 처음 주어지는 단어 word
word = sys.stdin.readline().rstrip()
# word의 길이
L = len(word)
# 만들 수 있는 모든 단어의 종류를 담을 배열 answers
answer = 'z' * L

for i in range(L - 2):
    for j in range(i + 1, L - 1):
        for k in range(j + 1, L):
            tmp = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            # tmp가 answer보다 사전순서로 작다면 answer에 tmp값을 저장
            if tmp < answer:
                answer = tmp
# answer를 출력
print(answer)