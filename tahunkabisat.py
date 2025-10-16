def isTahunKabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        kabisat = "Tahun Kabisat"
        return kabisat
    else:
        kabisat = "Bukan Tahun Kabisat"
        return kabisat
print(isTahunKabisat(2025))
print(isTahunKabisat(2000))

    