import sys

# 종이의 줄의 개수 N
N = int(sys.stdin.readline())
# 숫자를 저장하는 배열 numbers
numbers = []

for _ in range(N):
    # 주어지는 글자 string
    string = sys.stdin.readline().rstrip()
    # 숫자문자를 저장하는 변수 word
    word = ''

    for letter in string:
        # 정수인 경우
        if letter.isdigit():
            word += letter
        else:
            # word에 숫자문자가 존재
            if word:
                numbers.append(int(word))
                # word 초기화
                word = ''
    if word:
        numbers.append(int(word))
# 비내림차순 정렬
numbers.sort()
# 비내림차순으로 출력
for number in numbers:
    print(number)