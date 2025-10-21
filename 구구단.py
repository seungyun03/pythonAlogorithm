print('-'*27)

for i in range(1,10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j:3}", end=' ')#:3은 3칸 확보
    print()