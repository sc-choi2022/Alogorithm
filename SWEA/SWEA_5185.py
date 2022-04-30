import sys
sys.stdin = open('sample_input.txt')

# 16진수의 4자리 2진수를 key와 value를 가진 dictionary
binary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
          '4':'0100', '5':'0101', '6':'0110', '7':'0111',
          '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
          'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

# 테스트케이스 수 T
T = int(input())
for case in range(1, T+1):
    # 자리 수 N, 16진수 number
    N, number = input().split()
    ans = ''
    # number의 각 자리수를 binary의 key로 사용하여 이진수를 받는다.
    for num in number:
        ans += binary[num]
    # 테스트 케이스 번호와 답을 출력
    print(f'#{case} {ans}')