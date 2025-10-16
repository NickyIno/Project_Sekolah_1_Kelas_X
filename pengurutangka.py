
def urut_kecil_besar(list_angka):
    for x in range(len(list_angka)):
        for k in range(x+1,len(list_angka), 1):
            if list_angka[x] > list_angka[k]:
                kiana = list_angka[k]
                list_angka[k] = list_angka[x]
                list_angka[x] = kiana
    return list_angka

def urut_besar_kecil(list_angka):
    for x in range(len(list_angka)):
        for k in range(x+1,len(list_angka), 1):
            if list_angka[x] < list_angka[k]:
                kiana = list_angka[k]
                list_angka[k] = list_angka[x]
                list_angka[x] = kiana
    return list_angka

def pengurutan (list, tipe):
    if tipe == "asc":
        urut_kecil_besar(list)
        return (urut_kecil_besar(list))
    elif tipe == "desc":
        urut_besar_kecil(list)
        return (urut_besar_kecil(list))
print(pengurutan([12,3,1,7,2], "asc"))
print(pengurutan([12,3,1,7,2], "desc"))

