for i in range(2, 100):
    j = 2
    count = 0
    while j < i:
        if i % j == 0:
            count = 1
        j += 1

    if count == 0:
        print(i, "é um número primo")
    count = 0
