import numpy as np

print('----------------------------------------------------')
print('Nama     :DWI PEBRIYANTO PRADANA                    ')
print('Program  :Transpose, Determinan, dan Inverse Matriks')
print('----------------------------------------------------')

A=int(input("Masukkan jumlah baris Matriks: "))
B=int(input("Masukkan jumlah kolom Matriks: "))
print('Masukan Nilai Matriks: ')
entries = list(map(int, input().split()))
matriks = np.array(entries).reshape(A, B)
print('Matriks: ')
print(matriks)

print('\nSilahkan pilih perhitungan matriks sesuai angka:\n 1.Transpose Matriks\n 2.Determinan Matriks\n 3.Inverse Matriks')
Pilihan = int(input('Masukan pilihan anda: '))
if Pilihan == 1:
    transpose = matriks.transpose()
    print('\nTranspose matriks: ')
    print(transpose)

elif Pilihan == 2:
    ordo1 = matriks.shape
    jumlah_baris = ordo1[0]
    jumlah_kolom = ordo1[1]
    if jumlah_baris == jumlah_kolom:
        determinan = np.linalg.det(matriks)
        print('\nDeterminan matriks:')
        print("{:.1f}".format(determinan))
    else:
        print('\nTidak memiliki determinan (matriks bukan persegi)')

elif Pilihan == 3:
    ordo1 = matriks.shape
    jumlah_baris = ordo1[0]
    jumlah_kolom = ordo1[1]
    if jumlah_baris == jumlah_kolom:
        determinan = np.linalg.det(matriks)
        print('\nDeterminan matriks:')
        print("{:.1f}".format(determinan))
        if determinan != 0:
            invers_matriks = np.linalg.inv(matriks)
            print('\nInvers matriks:')
            print(invers_matriks)
        else:
            print('\nTidak memiliki invers (matriks singular)')
    else:
        print('\nTidak memiliki determinan (matriks bukan persegi)')
else:
    print('Pilihan tidak tersedia')