from decimal import*
from math import*
# 라이프니츠
#
# answer = Decimal(0)
# for x in range(1,20000000,2):
#     # print(x)
#     if (x-3)%4 == 0:
#         answer -= Decimal(4/x)
#     else:
#         answer += Decimal(4/x)
#
# print(answer)

# Chudnovsky 알고리즘
from math import factorial
from decimal import Decimal, getcontext

# from math import factorial
# from decimal import Decimal, getcontext
# # Chudnovsky algorithm for figuring out pi
# getcontext().prec=1000
#
# pi_input = input('How many digits of pi would you like?')
# n = int(pi_input)
#
# def cal(n):
#     t= Decimal(0)
#     pi = Decimal(0)
#     deno= Decimal(0)
#
#     for k in range(n):
#         t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
#         deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
#         pi += Decimal(t)/Decimal(deno)
#     pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
#     pi = 1/pi
#     return round(pi,n)
#
# print(cal(n))
#
#
# 톡방 방식
# #파이를 소숫점 아래 N자리까지 근사
# N = 100
# #편의를 의해 D로 사용
# D=Decimal
# #소숫점 아래 N 자리까지 계산
# getcontext().prec = N
# #오차
# error=10**(1-N)
# #Sin함수를 테일러 전개로 구현
# Sin=lambda x:sum([x*(-x*x)**n/factorial(2*n+1)for n in range(N)])
# #초기값. Sin값이 약 3.14라는 것은 자명하므로 3.14와 3.15를 초기값으로 사용
# P,Q=D('3.14'),D('3.15')
# while abs(Sin(p:=(P+Q)/2))>error:
#     if Sin(p)<0:Q=p
#     else:P=p
# print(p)

# 내가 짜보기

N = int(input())
getcontext().prec=1000
boonja = Decimal(0)
boonmo = Decimal(0)
boonsoo = Decimal(0)

for q in range(N):
    boonja = ((-1)**q) * (factorial(6*q)) * (((545140134)*q)+(13591409))
    boonmo = (factorial(3*q)) * ((factorial(q))**3) * (640320**((3*q)+(Decimal(1.5))))
    boonsoo += Decimal(boonja)/Decimal(boonmo)
print(round((12*boonsoo)**-1,N))
