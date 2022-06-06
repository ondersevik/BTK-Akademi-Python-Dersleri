# Operatör ve Döngüler

x , y , z = 5 ,10 ,15

x += 5
y = x 

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