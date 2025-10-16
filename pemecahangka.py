def pemecah_angka(n):
    if n % 2 == 0:
        i = n // 2
        j = i
    elif n % 2 == 1:
        i = n // 2
        j = i + 1
    return [i,j]

print((pemecah_angka(11)))
