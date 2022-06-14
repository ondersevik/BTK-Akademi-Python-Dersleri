# PYTHON OPERATÖTLERİ 🚴🏿‍♂️

'''
1. ATAMA OPERATÖRLERİ :
 + , - , * , / ,  // kalansız bölüm , % mod , += , /= vb , **n üssü , [index işlemleri]
'''
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

'''
2. KARŞILAŞTIRMA OPERATÖRLERİ :
  == eşitmi, != eşit değilmi, <= küçük eşit mi , < küçük mü .. True [1]/False[0] karşılaştırma, 
'''
a = int(input(" birinci sayı giriniz : "))
b = int(input(" ikinci sayı giriniz : "))
print (f" a sayısı {a} b den {b} büyüktür : ", a > b) 
a1 = (a % 2 == 0)   # tekmi çift mi?
a2 = (a >= 0)  # pozitif negatif ?
print (f" a sayısı tektir : {a1 == 0} ")
print (f" a sayısı pozitiftir : {a2 == 1} ")

c = int(input(" 1 nci vize sınav notu giriniz : "))
d = int(input(" 2 nci vize sınav notu giriniz : "))
e = int(input(" final sınav notu giriniz : "))
Not = 0.30 * ( c + d ) + 0.40 * e 
if Not >= 50 : " Sınavı geçmiştir." 
print (f'Sınavlardan aldığı ortalama not : {int(Not)} . Sınıfı geçmiştir : {Not>=50}')


'''
3. MANTIKSAL OPERATÖRLER
and , or ,not operatörleri

# AND : True and True = True (1) diğerleri False (0)
# OR  : True or True/False = True ; False or False = False (0)  
# NOT : result = not( 5<0) ; normalde False döner ama NOT true(1) yapar.
'''

# SORU : X  5 ve 15 arasında, çift ve pozitif bir sayımı ?
x = int(input(" x sayısını giriniz:"))
result = ((x<15) and (x>5)) and ( x %2 == 0) or not( x>=0) 
print (result)

a = int(input("Bir sayı giriniz :   "))
print(a)
result = ((a < 100) and (a > 0)) and (a % 2 == 0) # a 0 ile 100 arasında cift sayı mı ?
print(f' Sayı 0 ile 100 arasında ve çift sayımı :   {result}')

email = "onder@gmail.com"
password = "Onder1997."
posta = input("Email adresini giriniz:   ").lower().strip() # harfler büyük olsa bile kabul eder. boşluklıda siler kabul eder.
_password = input("Password giriniz :   ")
print(f'email adresiniz : {email == posta} // passwordunuz : {password == _password}') # Email ve Password kontrolu?

a1 = int(input("Bir sayı giriniz :   ")) # üç sayı kontrlou
a2 = int(input("İkinci sayı giriniz :   "))
a3 = int(input("Üçüncü sayı giriniz :   "))
resulta1 = (a1 > a2) and (a1 > a3)
print(f' a1, {a1} en buyuk sayıdır : {resulta1}')
resulta2 = (a2 > a1) and (a2 > a3)
print(f' a2, {a2} en buyuk sayıdır : {resulta2}')
resulta3 = (a3 > a1) and (a3 > a2)
print(f' a3, {a3} en buyuk sayıdır : {resulta3}')


vize1 = int(input("vize_1 notu giriniz :   "))
vize2 = int(input("vize_2 notu giriniz :   "))
final = int(input("final notu giriniz :   "))
resultnot = (((vize1+vize2)/2) * 0.60) + (final * 0.40)
print (f'Sınıfı geçtiniz : { final >= 70 or (resultnot >= 50 and final >=50)}')

adı = input("adı ve soyadını giriniz:   ").upper()
kilo = float(input("kilo bilgisini giriniz :   "))
boy = float(input("boy bilgisini giriniz :   "))
index = float(kilo / ( boy ** 2))
print (f'{adı} ağırlığı: {kilo} ve boyu : {boy} dur. BKIndex sonucu {index} dır. Zayıf : {(index <= 18.4)} // Normal :{(index >= 18.5) and (index <= 24.9)} // Şişman :{(index >= 25.0) and (index <= 40.0)}')

'''
4. IS VE IN KARŞILAŞTIRMA OPERATORLERİ :
'''
x = ( 1,2,"b")
print (1 in x)  # içindeyse True değilse False retyrn eder.
print ( 1 not in x)
print ("hj" in x)

# END OF LESSON ----OZETLER --

'''
1. ATAMA OPERATÖRLERİ :
+ , - , * , / ,  // kalansız bölüm , % mod alma , += , /= vb , **n üssü , [index işlemleri]

2. KARŞILAŞTIRMA OPERATÖRLERİ :
== eşitmi, != eşit değilmi, <= küçük eşit mi , < küçük mü .. True [1]/False[0] karşılaştırma, 

3. MANTIKSAL OPERATÖRLER
and , or ,not operatörleri

# AND : True and True = True (1) diğerleri False (0)
# OR  : True or True/False = True ; False or False = False (0)  
# NOT : result = not( 5<0) ; normalde False döner ama NOT true(1) yapar.

4. IS aynı mı ? VE IN içinde mi ? KARŞILAŞTIRMA OPERATORLERİ :
'''