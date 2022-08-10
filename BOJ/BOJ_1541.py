# -을 기준으로 구분하기 위에 split('-') 활용
equation = input().split('-')

for i in range(len(equation)):
    # equation[i] 값은 +을 포함하거나 미포함하는 string값
    # split('+')을 통해 구분하고 int로 변환하여 값을 담는다.
    tmp = map(int, equation[i].split('+'))
    equation[i] = sum(tmp)
# 출력하는 ans에 equation의 첫값을 할당
ans = equation.pop(0)
# 나머지 모든 값을 ans에서 빼준다.
while equation:
    ans -= equation.pop(0)
# ans 출력
print(ans)