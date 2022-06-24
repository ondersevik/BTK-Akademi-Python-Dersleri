# 6. FOR ve WHILE DÖNGÜLERİ :
'''
# LİSTELERDE DÖNGÜLER :
sayılar = [1,2,3,4,5]
print (sayılar[:-1])

for num in sayılar :   # num değişken (istediğin ifade kullanabilirsin) + in (true/false) + sayılarda işlem gören liste ve : ile döngü başlıyor.
    print(num)         # sayılar listesindeki her 0-1-2 ... index teki elemenı al s değişkenine at ve döngüde ekrana yazdır.

# STRING İFADELERDE DÖNGÜLER :

string = "ondersevik"
print (string)

for str in string :   
    print(str)         


# TUPLE LİSTELERDE DÖNGÜLER :
tuple = ([1,2,3],"ondersevik",4,5,6,"bn")
print(type(tuple))

for tup in tuple :   
    print(tup)


# DICT DÖNGÜLER :
dict = { "a" : 1, "b" :2, "c" :3, "d" :4}  # key & value verileri ..
print(type(dict))

for key,value in dict.items() :   # dict farklı olutyor. .items() eklenecek dict ve hangi eleman yada elemanar lazımsa onlar çagrılır
    print(key,value)



# UYGULAMA :

sayılar = [1,3,5,7,9,12,21,21]

# hangileri 3 ün katıdır.
for i in sayılar :
    if (i % 3 == 0) :  # mod 3 kullanıyoruz .. True false
        print(f' {i} 3 ün {i/3} katıdır.')
    else :
        print (f' {i} 3 ün katı değildir.')

# sayıların karesi kaçtır.
for i in sayılar :
    print(f' {i} sayısı karesi = {i**2}')

# elemanların toplamı kaçtır.

e = 0
for i in sayılar :
    e += i                # e = e + i

    print(f' listedeki elemanların toplamı : {e} dir. ')  # Bi alttaki ile aradaki farka DİKKAT !!!!1
print(f' listedeki toplam elemanların toplamı : {e} dir. ') # DÖNGÜ SONRASI TEK 

print(sayılar.count(21))

sehirler = [" kocaeli", "istanbul", "ankara", "izmir", "rize"] # max 5 karakterli eleman olanlar hangisidir.
for i in sehirler :
    if (len (i) <= 5) : # eğer string length 5 ve 5 den fazlaysa
        print(f'{i} şehri uzunluğu 5 ve 5 den azdır.')
    else : 
        print (f'{i} şehir length uzunluğu 5 den fazladır.')


# UYGULAMALAR (DICTIONARY)
urunler = [
    {"adı" : " onder ", "fiyat" : "3000"},
    {"adı" : " ali ", "fiyat" : "5000"},
    {"adı" : " veli ", "fiyat" : "4500"},
    {"adı" : " hasan ", "fiyat" : "2000"},
]
print(len(urunler))
print(urunler[1])


toplam = 0
for key in urunler :                   # (key1 : value1)
    value_fiyat = int(key["fiyat"])    # keyi fiyat olanların int cevrilmiş value alındı..
    toplam += value_fiyat 
    if (int(key["fiyat"])) <= 3000 :
        print (key["adı"],"kişisi",key["fiyat"], "ile aldığı urun 3000 tl den düşük ve eşit ürünler listesinde olup ucuzdur.")
    else :
        print (key["adı"], "urunu pahalıdır.")
print ("urunlerin toplam fiyatı = ", toplam )



# While Döngüsü :

x = 90

while ( x< 100): # True koşul döndüğü sürece döngü var..Döngü başladı.
   
    if ( x % 2 ==0): # İçine if döngüsü yaptık:
        print(" çift sayılar :", x)
    else :
        print(" tek sayılar :", x)
   
    x += 1        # Döngü devam ediyor.
    print (x)    # İç döngü bitti.Devam while ile yeniden iç döngü başladı.
print(" Bitti")  # Dış döngü bitt. GİRİNTİLER ÖNEMLİ BURADA..



# While Uygulamalar :

sayilar = [1,3,5,7,9,12,19,21]  # liste adında türkçe karakter kullanma 👧 sayılar yazdım 1 saat ugrastım..

# liste elemanlarını yazdır.
i = 0
while i < (len(sayilar)) :
    
    print(sayilar[i])
    i += 1

print( "Bitti")

# Başlangıç ve Bitiş değerlerini aldığın listenin değerleini yazdır.

a = int(input("İlk değer giriniz:")) # Başlangıç sayısı aldık.
b = int(input("Son değer giriniz:")) # Bitiş sayısı alduk.

i = a                               # değişkene başlangıç sayısını atadık .
while ( i < b ):                    # koşul[T/F] : i değişkenin b den küçük olması = True.
    i += 1
    if ( i % 2 == 0) :               # alt koşul mod 2 olmasında iç IF döngüsü olusturdu.
        print(i, " sayısı çift sayıdır.")
    else :
        print(i, "sayısı tek sayıdır.")

# 1-100 arasını azalan şekilde yazdır.

i = 100                               # değişkene başlangıç sayısını atadık .
while ( i > 0 ):                    # koşul[T/F] : i değişkenin b den küçük olması = True.
    i -= 1
    print(i)
print("Bitti")
    


# Aldığımız değerleri liste içinde saklayalım.

from http.client import CONTINUE


liste = []                          # Boş liste oluşturduk.

i = 0                               # değişkene liste başlangıç indexini atadık .
while ( i < 5 ):                    # koşul[T/F] : i değişkenin 5 input girmesi = True.
    sayi = int(input("sayı giriniz :"))
    liste.append(sayi)              # sayi girişi listeye atandı.
    liste.sort()                    # sayılar sıralandı.
    liste.reverse()                 # sayılar ters çevrildi.

    # BREAK / CONTINUE KULLANIMI :
    if ( i == 3) :
        print(f' {i} nci döngüde break yaptık ve müteakip döngü durdu.')
        break      # break döngüyü durdurur. While döngüsünden çıkarız. Yani if = False olur.
       # continue  # continue o anda true iptal eder ve döngüde başa döner ve hep döngü olur. Bu yuzden i += 1 gecemeyiz
       # n yapacağız .. i += 1 satırını if satırı üstüne alacağız.
    i += 1
    print(liste)
print("Bitti")

    

# FOR VE RANGE DÖNGÜLERİ KARŞILAŞTIRMA :

liste = [1,2,3,4,5,6]

for i in liste :
    print (i)  # 1 2 3 4 5 6 

# peki elimizde liste olmaz ise nasıl yapacağız ?

for a in range(6): # 6 stop element i değişkenidir ve range hem for hemde while döngüde kullanılabilir.
    print (a)  # 0,1,2,3,4,5 verir.. dikkat 0 dan başlıyor ve stop değişken yok.

for b in range(2,50,4) : # başlangıç[dahil] + bitiş[hariç] ve step elemanları
    print (b)

print(list(range(2,50,2))) # yukarıdaki çıktıyı list objesi olarakta alabilirim. yada
print(tuple(range(2,50,2))) # tuple objesi

# enumerate : (eğer indexide almak istersek)

x = 'ondersevik'       # x stringine odersevik atandı

for index,i in enumerate(x):  # x stringi enumerate ile index nu ve string elemanlarına ayrıldı.
    print(index,i)           # stringin index nu ve elemanı yazıldı 

# zip : [ 2 listeyi dict gibi birleştrmek istersek]

list1 = [1,2,3,4,5]
list2 = ["a","b","c"]
print(list(zip(list1,list2)))  # [(1, 'a'), (2, 'b'), (3, 'c')]

for item in zip(list1,list2) :
    print(item)                 # (1, 'a')
                                # (2, 'b')
                                # (3, 'c')


for a , b in zip(list1,list2) :
    print(a)                 # sadece indexleri döker.

'''

# LIST COMPREHENSIONS AYNI SONUÇ VEREN UYGULAMALAR :

x =[]

# direkt listeye alınmış range :
print(list(range(2,20,2))) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

# döngü ile alınan değişkenlerin listeye append edilmesi :
for a in range(2,20,2) :   # [2, 4, 6, 8, 10, 12, 14, 16, 18]
    x.append(a) 
print(x)