import sys
# 단어의 개수 N
N = int(sys.stdin.readline())

# 단어를 담을 배열 words
words = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 단어의 각 알파벳의 위치와 개수의 정보를 담을 딕셔너리 alphabet
alphabet = {}

# words의 각 word에 대해
for word in words:
    for i in range(len(word)):
        # 알파벳이 딕셔너리 alphabet에 없는 경우
        if word[i] not in alphabet:
            # alphabet에 10 ** (len(word) -1 -i)을 value로 추가
            alphabet[word[i]] = 10 ** (len(word) -1 -i)
        # 존개하는 경우
        else:
            alphabet[word[i]] += 10 ** (len(word) -1 -i)

# 알파벳을 value를 기준으로 정렬
alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)
# 정렬한 value을 기준으로 정보를 담을 딕셔너리 alphabetNum
alphabetNum = {}

# 가장 큰 값이 나올 수 있도록 변수 num을 9로 초기화
num = 9
for alpha in alphabet:
    alphabetNum[alpha[0]] = num
    num -= 1

# 출력할 최대값 ans 0으로 초기화
ans = 0

# word의 각 알파벳을 alphabetNum의 값에 맞게 add에 저장 후 ans에 반영
for word in words:
    add = ''
    for w in word:
        add += str(alphabetNum[w])
    ans += int(add)

# ans 출력
print(ans)