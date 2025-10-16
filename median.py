def urut_kecil_besar(list_angka):
    for x in range(len(list_angka)):
        for k in range(x+1,len(list_angka), 1):
            if list_angka[x] > list_angka[k]:
                wadah = list_angka[k]
                list_angka[k] = list_angka[x]
                list_angka[x] = wadah
    return list_angka

angka = [12,5,4,3,10,2]
print(angka)

def median(angka):
    angka_urut = urut_kecil_besar(angka)
    n = len(angka_urut)
    angka_tengah = n // 2
    
    if n % 2 == 0:
        return (angka[angka_tengah - 1] + angka[angka_tengah]) / 2
    else: 
        return angka[angka_tengah]
print(median(angka))
