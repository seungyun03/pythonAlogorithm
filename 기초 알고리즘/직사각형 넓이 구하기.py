import math
area = int(input("넓이를 입력하세요:" ))
for i in range(1,int(math.sqrt(area)+1)):#필요시 그냥 area+1 해도됨
    if area % i !=0:
        continue
    print(f"{area} = {i} x {area/i}")

