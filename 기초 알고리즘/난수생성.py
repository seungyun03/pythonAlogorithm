import random
n = int(input("몇 개의 난수를 생성할까요?"))
ban = 13
for i in range(n):
    num = random.randint(1,18)
    print(f"num = {num}")
    if num == ban:
        break
    