print("별 트리를 만들어보자")
h = int(input("트리의 높이 입력: "))
for i in range(1,h-2):
       
        print(" "*((h//2)-i+1),end='')
        print('*'*(2*i-1))
        print(" "*((h//2)-i+1),end='')
        print()