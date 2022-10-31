#list (sekumpulan data) menggunakan for range
#contoh
angka = int (input ("masukkan angka: "))
data = [i for i in range (1,angka+1)]
print(data)


#menampilkan bilangan genap
angka = int (input ("masukkan angka: "))
data = [ i for i in range (1,angka) if i %2 == 0]
print (data)

#menampilkan bilangan ganjil
angka = int (input ("masukkan angka: "))
data = [ i for i in range (1,angka) if i %2 != 0]
print (data)
