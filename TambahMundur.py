def tambahMundur(x,y):                                      # Membuat fungsi 'tambahMundur' dengan parameter
    x2 = str(x)                                             # Melakukan konversi tipe data
    y2 = str(y)                                             # Melakukan konversi tipe data

    x1 = int(x2[::-1])                                      # Melakukan konversi tipe data
    y1 = int(y2[::-1])                                      # Melakukan konversi tipe data

    j = x1 + y1                                             # Melakukan penjumlahan
    j1 = str(j)                                             # Melakukan konversi tipe data
    jres = int(j1[::-1])                                    # Melakukan konversi tipe data

    if 0 < jres < 359999:                                   # Pernyataan kondisional
        print ('Hasil Tambah Mundurnya : ', jres)       
    else:
        print('Invalid Input, Nilai > 359999')

x = int(input('Masukkan Angka 1 : '))                       # Input data oleh user
y = int(input('Masukkan Angka 2 : '))                       # Input data oleh user

tambahMundur(x,y)                                           # Memanggil fungsi dengan argumen