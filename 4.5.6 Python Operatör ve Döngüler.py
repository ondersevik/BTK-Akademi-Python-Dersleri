# Operatör ve Döngüler

# ATAMA OPERATÖRLERİ : + , - , * , / ,  // kalansız bölüm , % mod , += , /= vb , **n üssü , [index işlemleri]
#-------------------------------------------------------------------------------------------------------------
x = 5
y = x 
z = 78

print(x+y+z)

x += 5 # x = x + 5
y -= 1
z *= 2

print (x,y,z)

a = 3 * x // 2 # 3*15 tam böl 2 = 22.5 = 22
b = 3 * x % 2 # 3*15 mod 2 = 23 - 22 = 1
print (a,b)

değer = ( 1,2,3,4) # değişkenler değer tuplese atandı
a,b,c,d = değer    # değer tuplei a,b,c,d değişkenlerine atandı a= 1 :b =2 .....
e,*z = değer       # burada e= 1 atandı * ile kalanlar liste olarak z atandı 

print(type(değer)) # <class 'tuple'>
print (a+b+c) # 6
print (e,z)   # 1 [2, 3, 4]

# UYGULAMALAR 
x , y, z = 2,5,10
numbers = 1,5,7,10,6

print ((numbers[2] + numbers[0]) - ( x+y+z)) # numbers dan 2 ve 0 ncı indexleri aldık topmadan cıkardık -9
print (y // x)       # // KALANSIZ BÖLME : 5/ 2 kalansız = 2
print (( x+y+z) % 3) # % MOD : mod 3 17 = 2
print ( y ** x )     # 5 ussü 2 = 25

x,*y,z = numbers
print (z**3)         # 6 ussu 3 = 216
print (x,y,z)
print (y[0]+y[1]+y[2])  

# KARŞILAŞTIRMA OPERATÖRLERİ :  == eşitmi, != eşit değilmi, <= küçük eşit mi , < küçük mü .. True [1]/False[0] karşılaştırma, 
#---------------------------------------------------------------------------------------------------

a = int(input(" Bir sayı giriniz : "))
b = int(input(" ikinci sayı giriniz : "))
print (" a sayısı {a} b den {b} büyüktür : ", a > b) 
a1 = (a % 2)   # tekmi çift mi?
a2 = (a >= 0)  # pozitif negatif ?
print (f" a sayısı çifttir : {a1 == 0} ")
print (f" a sayısı pozitiftir : {a2 == 1} ")

c = int(input(" 1 nci vize sınav notu giriniz : "))
d = int(input(" 2 nci vize sınav notu giriniz : "))
e = int(input(" final sınav notu giriniz : "))
Not = 0.30 * ( c + d ) + 0.40 * e 
if Not >= 50 : " Sınavı geçmiştir." 
print (f'Sınavlardan aldığı ortalama not : {int(Not)} . Sınıfı geçmiştir : {Not>=50}')

