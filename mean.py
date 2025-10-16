list_angka = [2,3,4,5,10,12]
def mean(angka):
    hasil = 0
    for x in angka:
        hasil += x
    return hasil / len(angka)
print(mean(list_angka))
