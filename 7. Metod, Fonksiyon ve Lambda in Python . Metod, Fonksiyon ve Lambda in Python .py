# Method : https://docs.python.org/3/tutorial/introduction.html# bu sayfadan list string ve numbers methodları hakkında bilgi var.

'''
# 1. Liste <class list> için methodlar :
liste = [1,2,3,4,5]
liste.append(6)     # class/sınıf = liste ve append is method of liste class 
print(type(liste),liste) # <class 'list'> [1, 2, 3, 4, 5, 6]
# liste.[append,extend,remove,remove,pop,sort,index,insert,clear,copy,count ] bunlar liste sınıflarının methodları..

# 2. String <class str> için methodlar :
string = "ondersevik"
print(string.startswith("b"))    # class/str = string ve capitalize is method of liste class .. False // True döker bu metod
print(type(string),string) # <class 'list'> [1, 2, 3, 4, 5, 6]
# liste.[append,extend,remove,remove,pop,sort,index,insert,clear,copy,count ] bunlar liste sınıflarının methodları..

# 3. Fonksiyonlar : methodlardan farkı class içinde değiller...

def sayHello(name) :     # sayHello fonksiyonu oluşturalım. parametre olarakta name atayalım. istersek burayı atlayabiliriz.
    print("Hello World " + name)

sayHello("Onder")        # Hello World Onder

# UYGULAMA : YAS HESAPLAMA ..

def _age(b) :        # verilen yıla göre yası hesap eden _age fonksiyon

a = input("Adınızı Soyadınızı Giriniz : ")
b = int(input("Doğum Yılını Giriniz : "))
c = int(input("Emeklilik Yaşını Giriniz : "))

    return 2022 - b

def _emekliligekaçyılkaldı(b) :
    yas = _age(b)     # _age fonks ile yası hesaplıyoruz.
    süre = c - yas    # emeklilik yaşından yaşı cıkarıp kalan sure hesaplanır.
   
    if süre <= 0 :     # süre bittiyse:
        print( f"{a} emekliliği hak etmiştir.")
    else :
        print( f"{a} emekliliğe {süre} yıl kalmıştır.")


# Fonksiyon Uygulaması örnek 1: 
def changeName(n):      # n parametresi/değiskeni  ile changeName foksiyonu oluşturduk ve parametreyi " ada " olarak değiştirdik
    
    n = "ada"           # değişken ve bu alanda bulunan değer

name = "onder"          # name değişkeni tanımladık ve onder ismini verdik
changeName(name)        # fonsiyona name bilgisini gönderdik ve sonuç :
print(name)             # onder olarak geldi...

name1 = "ata"          # name1 değişkeni tanımladık ve ata ismini verdik
changeName(name1)        # fonsiyona name1 bilgisini gönderdik ve sonuç :
print(name1)             # ata olarak geldi...

name2 = "nola"          # name2 değişkeni tanımladık ve onder ismini verdik
changeName(name2)        # fonsiyona name2 bilgisini gönderdik ve sonuç :
print(name2)             # nola olarak geldi...

print(name,name1,name2,[name,name1,name2])  # onder ata nola ['onder', 'ata', 'nola']

n = a = ["ata","key","atkey"] # liste olarak a listesi ve onuda n değişkenine referans verdim. 3 de aynı değer
changeName(a)           # fonksiyona soktuk 
print(a,n[0])                # ['ata', 'key', 'atkey'] ata
'''
# Fonksiyon Uygulaması Ornek 2 : toplam fonksiyonu oluşturalım..

from numpy import average

# toplam fonksiyonu yapalım:
def toplam(*params) :  # * ile parametre veridiğinde artık kaç tane parametre girersen gir farketmez.
    return sum(params)

# ortalama fonksiyonu yapalım:
def ortalama(*params) :  # değişik yazdık bu sefer. 1 nci değer a , son değer c ve * ile aradaki tümü b atandı
    return average(params)
    
print(toplam(1,3,2,5,67,8))
print(ortalama((1,3,4,5,67,8)))

