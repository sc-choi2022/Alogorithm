import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 암호코드 비율 a:b:c:d의 bcd의 정보를 key로 대응하는 숫자를 value으로 갖는 딕셔너리 info
info = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}
# 16진수를 2진수로 바꾸기 위해 16진수 값을 key로 대응하는 이진수를 value로 갖는 딕셔너리 hex_bi
hex_bi = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
              '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}


for case in range(1, T + 1):
    # 세로의 크기 N, 가로의 크기 M
    N, M = map(int, input().split())
    # 암호코드 정보를 담을 리스트 text
    text = [input().strip() for _ in range(N)]

    # 정답 ans와 암호를 가지고 있는지를 확인하는 리스트 have를 초기화
    ans = 0
    have = []
    # text의 행을 기준으로 확인
    for i in range(N):
        tmp = text[i]
        # 행이 0으로만 이루어져 있다면 continue
        if tmp == '0'*M:
            continue
        # 16진수를 2진수로 나오는 값을 저장할 변수 str
        str2 = ''
        for t in tmp:
            str2 += hex_bi[t]

        res = []
        c1, c2, c3 = 0, 0, 0
        for c in range(len(str2)-1, -1, -1):
            if c2 == 0 and c3 == 0 and str2[c] == '1':
                c1 += 1
            elif c1 != 0 and c3 == 0 and str2[c] == '0':
                c2 += 1
            elif c1 != 0 and c2 != 0 and str2[c] == '1':
                c3 += 1
            elif c3 != 0 and str2[c] == '0':
                lower = min(c1, c2, c3)
                res.append(str(c3//lower) + str(c2//lower) + str(c1//lower))
                c1, c2, c3 = 0, 0, 0

                # 암호를 구성하는 8개의 수가 res에 담겼다면
                if len(res) == 8:
                    # 이를 대응하는 암호코드로 변환
                    for r in range(len(res)):
                        res[r] = info[res[r]]
                    if res not in have: # res안의 값이 int가 아니면 not it have가 제대로 작동하지 않는다.

                        # 검증코드는 아래와 같은 방법으로 계산값을 right에 할당
                        right = (res[7] + res[5] + res[3] + res[1]) * 2 + sum(res)
                        # right가 정상암호코드의 결과를 갖는다면
                        if right % 10 == 0:
                            # ans에 sum(res)를 더한다.
                            ans += sum(res)
                        have.append(res)
                    res = []
    print(f'#{case} {ans}')