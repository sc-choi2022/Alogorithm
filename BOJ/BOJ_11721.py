# 주어지는 단어 word
word = input()
# 단어를 열 개씩 끊어서 한 줄에 하나씩 출력
for i in range(0, len(word), 10):
    print(word[i:i+10])