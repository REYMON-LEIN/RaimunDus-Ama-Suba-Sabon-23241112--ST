# latihan mambuat percabangan
print("silakan masukan operasi yang diinginkan:")
print("1 -operasi penjumlahan")
print("2 -opersi pengurangan")
pilihan = int(input("Masukan pilihan anda: "))

if pilihan == 1: 
    print("\n ini operasi penjumlahan")
    bilangan1 = int(input("masukan bilangan pertama: "))
    bilangan2 = int(input("masukan bilangan kedua: "))
    hasil = bilangan1 + bilangan2
    print("hasil adalah: ",hasil) 
elif pilihan == 2:
    print("\n ini operasi pengurangan")
    bilangan2 = int(input("Masukan bilangan pertama: "))
    bilangan1 = int(input("Masukan bilangan kedua"))
    hasil = bilangan1 - bilangan2
    print("Hasil adalah: ", hasil)
else:
    print("pilihan angka 1 atau 2")
