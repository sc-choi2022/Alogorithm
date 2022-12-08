import sys

words = [list(sys.stdin.readline().strip()) for _ in range(5)]

# words의 word의 길이 중 최대값을 i로 지정
for i in range(max(len(word) for word in words)):
    for j in range(5):
        # i가 words[j]의 길이보다 작다면 print
        if i < len(words[j]):
            print(words[j][i], end='')