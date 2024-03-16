#contoh disini jika kita print tanpa input kita tidak bisa mengetikkan apapun disamping str
#maka kita coba dengan contoh :

#note hilangkan tanda # untuk mengaktifkan 

#print(input('halo siapa nama kamu'))
#kita juga bisa memakai input dengan variabel contoh :
 
#input_nama = input('Hallo nama kamu siapa?')
#print(input_nama)

#rumus matematika sebuah python
#+ = +
#- = -
#* = di kali
#/ = di bagi

#a = 10
#b = 20
#d = 9
#e = 2
#c = a + b#jadi kita bukan ketik 10 + 20 karena sudah kita tampung di variabel 
#maka langsung saja tampung ke c = a + b lalu print(c) hasilnya akan muncul  berikut contoh nya :
#print(c)
#c1 = b - a
#c2 = a * b
#c3 = b / a #tipe data float atau tipe data berubah sesuai hasil
#c4 = d / e

#print(c1)
#print(c2)
#print(c3)
#print(c4)

#jadi kita bisa coba gabungkan dengan input contoh :

#f = input('masukan nomer pertama') #output str
#j = input('masukan nomer kedua') #output str
#c = f + j

#print(c) #kenapa ini jadi umpama 80 90 jadinya 80 90 karena
#input menghasilkan str output str

#jika kita masukan int maka akan muncul hasilnya contoh
#c = int(f) + int(j) # ---> interger contoh 10 + 10 = 20
#print('hasilnya adalah ' + str(c)) #jika str tambah int maka error
#kita perlu tambahkan str(c))
#jika di pembagian / itu adalah hasil default jika kita tambahkan // maka akan di bulatkan

x = input('nomer ke satu ? ')
z = input('nomer ke dua ?')
r = int(x) / int(z) #ubah perkalian atau pembagian dll di sini

print('hasil pembagian : ' + str(r)) #untuk bagian print tetap gunakan +