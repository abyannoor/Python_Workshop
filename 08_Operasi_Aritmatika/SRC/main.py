# Operasi Aritmatika Standard


a = 10
b = 3

# Operasi Tambah +
hasil = a + b
print(a, '+' ,b, '=', hasil)


# Operasi Pengurangan -
hasil = a - b
print(a, '-' ,b, '=', hasil)


# Operasi Perkalian *
hasil = a * b
print(a, '*' ,b, '=', hasil)


# Operasi Pembagian /
hasil = a / b 
print(a, '/' ,b, '=', hasil) # otomatin menjadi float data


# Operasi Eksponen (pangkat) **
hasil = a ** b
print(a, '**' ,b, '=', hasil)




# Operasi modulus (sisa pembagian) %
hasil = a % b
print(a, '%' ,b, '=', hasil)


# Operasi floor division (pembagian yang dibulatkan ke bawah) //
hasil = a // b
print(a, '//' ,b, '=', hasil)



# Prioritas Operasi, operational precedence
'''
 1. ()
 2. eksponen **
 3. perkalian dan temannya
 4. pertambahan dan pengurangan
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z, '=', hasil)