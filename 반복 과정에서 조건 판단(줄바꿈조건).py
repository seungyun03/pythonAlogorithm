#최적화버전
print('*를 출력합니다')
n = int(input("몇 개를 출력할까요?"))
w = int(input("몇 개마다 줄바꿈 할까요?"))
for i in range(n//w): #6/4는 실수값만,6//4는 몫만
    print('*'*w)#굳이 기본버전의  for문 사이if문을 넣을 필요없음(복잡도만 증가함)
rest = n % w
print("*"*rest)

#기본버전12
""""
print('*를 출력합니다')
n = int(input("몇 개를 출력할까요?"))
w = int(input("몇 개마다 줄바꿈 할까요?"))
for i in range(n):
    print('*', end='')
    if i % w == w - 1   :
        print() #줄바꿈
if n % w:
    print()
"""