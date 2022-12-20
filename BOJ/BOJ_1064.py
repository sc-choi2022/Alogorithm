import sys
# 평행사변형의 후보인 세개의 점 xA yA xB yB xC yC
Xa, Ya, Xb, Yb, Xc, Yc = map(int, sys.stdin.readline().split())

if ((Xa - Xb)*(Ya - Yc) == (Ya - Yb)*(Xa - Xc)):
    print(-1.0)
else:
    # 세개의 점으로 만들수 있는 변의 길이 lenAB, lenBC, lenCA
    lenAB = ((Xb - Xa)**2 + (Yb - Ya)**2)**0.5
    lenBC = ((Xc - Xb)**2 + (Yc - Yb)**2)**0.5
    lenCA = ((Xa - Xc)**2 + (Ya - Yc)**2)**0.5

    # 사변형의 다른 두 변의 길이를 담는 리스트 length
    length = [lenAB + lenBC, lenBC + lenCA, lenCA + lenAB]
    # 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이 ans
    ans = 2 * (max(length) - min(length))
    # ans출력
    print(ans)