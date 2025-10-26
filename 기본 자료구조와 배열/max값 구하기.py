from typing import Any,Sequence

def max(a : Sequence) ->Any:

    maxi = 0
    for i in range(len(a)):
        if a[i]>maxi:
            maxi = a[i]
    return maxi
leng = int(input("배열의 크기를 입력하세요: "))
a = [0]*leng
for i in range(leng):
    a[i] =int(input(f"a[{i}]: "  ))
print(f"최대값: {max(a)}")
#변수병 정할 때 메서드 이름(len())