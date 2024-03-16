# TABEL VARIABEL
nama = "rouf " #tipe string
usia = 16  #tipe integer
tinggi_badan = 172 #tipe float

# Catatan True and False
Punya_Ayam = True #True and False harus diawali dengan huruf besar diawalnya jika menggunakan seperti ini true false makan akan error
Punya_Ayam = False

#int('10') ---> 10
#str(5) ---> '5'
#float(5) ------> 5.0 float itu adalah bilangan desimal
#jika ingin ubah integer ke string pakailah str didalam kurungnya adalah nilai yang akan kita ubah

menyapa = 'hallo semua nama saya ' #output harus str karena sudah ada str
print(menyapa + nama) # string
print(usia) #integer
print(tinggi_badan) #float

#jadi kita tambahkan str untuk ubah integer ke string contoh :
print("usia saya " + str(usia)) #output harus str jadi tidak akan terjadi kesalahan

#sama juga untuk tinggi badan contoh : 
print('tinggi saya ' + str(tinggi_badan)) #jangan lupa tutup kurung output 2 kurung untuk str

#jadi jika kita gabungkan semuanya itu bisa dengan cara dibawah ini :

print('nama saya ' + nama + 'usia saya ' + str(usia))
print('tinggi badan saya ' + str(tinggi_badan))
#maka akan tercipta "nama saya rouf usia saya 16 tinggi badan saya 172"
#Jika ingin di tambahin cm kita ketik saja cm di samping kurung menggunakan string contoh :
print('tinggi badan saya ' + str(tinggi_badan) + 'cm')