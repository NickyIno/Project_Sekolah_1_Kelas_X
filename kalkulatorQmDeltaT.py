def perubahan_energi_panas(m, c, delta_t):
    q = m * c * delta_t
    return q

def massa_jenis(q, c, delta_t):
    m = q / (c * delta_t)
    return m

def kalor_jenis_zat(q, m, delta_t):
    c = q / (m * delta_t)
    return c

def perubahan_suhu(q, m, c):
    delta_t = q / (m * c)
    return delta_t

print("=== Kalkulator Fisika: Kalor dan Perubahan Suhu ===")

lanjut = "y"
while lanjut.lower() == "y":
    print("Silakan pilih perhitungan:")
    print("1. Hitung Perubahan Energi (Q)")
    print("2. Hitung Massa (m)")
    print("3. Hitung Kalor Jenis Zat (c)")
    print("4. Hitung Perubahan Suhu (Delta T)")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    if pilihan == "1":
        m = float(input("Masukkan massa (m): "))
        c = float(input("Masukkan kalor jenis zat (c): "))
        delta_t = float(input("Masukkan perubahan suhu (Delta T): "))
        hasil = perubahan_energi_panas(m, c, delta_t)
        print("Hasil perubahan energi (Q):", hasil)
    elif pilihan == "2":
        q = float(input("Masukkan perubahan energi (Q): "))
        c = float(input("Masukkan kalor jenis zat (c): "))
        delta_t = float(input("Masukkan perubahan suhu (Delta T): "))
        hasil = massa_jenis(q, c, delta_t)
        print("Hasil massa (m):", hasil)
    elif pilihan == "3":
        q = float(input("Masukkan perubahan energi (Q): "))
        m = float(input("Masukkan massa (m): "))
        delta_t = float(input("Masukkan perubahan suhu (Delta T): "))
        hasil = kalor_jenis_zat(q, m, delta_t)
        print("Hasil kalor jenis zat (c):", hasil)
    elif pilihan == "4":
        q = float(input("Masukkan perubahan energi (Q): "))
        m = float(input("Masukkan massa (m): "))
        c = float(input("Masukkan kalor jenis zat (c): "))
        hasil = perubahan_suhu(q, m, c)
        print("Hasil perubahan suhu (Delta T):", hasil)
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
        continue

    lanjut = input("Ingin menghitung lagi? (y/n): ")

print("Terima kasih sudah menggunakan kalkulator fisika!")
