# memasukan data 4 bilang
a = int(input("masukan bilangan pertama "))
b = int(input("masukan bilangan kedua "))
c = int(input("masukan bilangan ketiga "))
d = int(input("masukan bilangan keempat "))

#Proses pengecekan
if a >= b and a>=c and a>=d:
    terbesar = a
elif b>= a and b>=c and b>=d:
    terbesar = b
elif c>= a and c>=b and c>=d:
    terbesar = c
else:
    terbesar  = d

#Output hasil
print("Bilangan terbesar adalah:", terbesar)