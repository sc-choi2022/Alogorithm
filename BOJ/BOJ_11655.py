import sys

# 입력받은 문자열 S
S = sys.stdin.readline()
answer = ''
for letter in S:
    if letter.islower():
        tmp = ord(letter)+13
        answer += chr(tmp-26) if tmp > 122 else chr(tmp)
    elif letter.isupper():
        tmp = ord(letter)+13
        answer += chr(tmp-26) if tmp > 90 else chr(tmp)
    else:
        answer += letter
# S를 ROT13으로 암호화한 내용을 출력
print(answer)