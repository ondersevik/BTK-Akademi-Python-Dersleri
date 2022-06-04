# 3.Python Objeleri ve Veri Tipleri

from regex import B, R
from sqlalchemy import DATE


musteri_Adi = "Onder"
musteri_Soyadi = "Sevik"
musteri_AdiSoyadi = musteri_Adi +" "+ musteri_Soyadi
musteri_Cinsiyet = True # Erkek
musteri_TCkimliknu = "12908728726" # bu tip veriler sstring olarak kaydedilir.
musteri_Dogumyılı = 1975
musteri_Yas = 2020 - musteri_Dogumyılı
print(musteri_Yas)

adam11 = 150
adam22 =223
adam33 = 567
v = (adam11+adam22+adam33)
print (v)
print ("onder borc", {v})


# STRING INDEXLEME (0,1,2------ yada ---4-3-2-1) yada[0:4] 0 ve 3 ncü index dahil
onder = "Onder Sevik"
print(onder[0])
print(len(onder))
print(onder[-1])
print(onder[2:6])
print(onder[4:])
a = 5
b = 18


# F STRING İLE SÜSLÜ PARANTEZ İÇİNDE {} DEĞİŞKEN ATAMASI :
c = "onder"
d = "sevik"
r = a/b
print( " My name is {} {} and a/b esittir {r:10.2}.".format(c,d,r=r))
print(f" My name is {c} {d} and a/b esittir {r:10.2}.") # f string ifadesi ile daha kolay değişken ataması:

# ORNEK
website = "http://ww.sadikturan.com"
course = "Phyton Kursu : jdjjffjjjlşnnnvfkkjhdjjdh"
print ("karakterSayısı =",len(course))
print(website[0:4]) # string slicing -http-
print(website[-4:0])
print(course[0:14])
print(course[15:-1])
print(course[-1:15])
print(course[len(course)-10:-1])
print(course[-len(course):-1])
print(course[::-1]) # başlangıç index ve bitiş index : ile tam yapılmış diğer -1 step indexi ile ters yazdırılmış

# ORNEK F STRING KULLANIMI
name = "Onder"
surname = "Sevik"
age = 46
job = "retired"
print(f"My name is {name} {surname}, my age is {age} and my job is {job}")

# STRING METODLARI
hello = "hello world"
result = hello.capitalize() # sadece ilk harf buyuk
result1=hello.count("e") # ilk e harf index
result2=hello.upper() # harfler buyuk
result3=hello.title() # kelime ilk harfler buyuk
print (result3)

result9 = hello.find("helloe") # 0 var ve -1 yok döker
print(result9)
isfound = hello.startswith("h") # True false döker
print(isfound)
result10= hello.strip("h") # h harfini strip etti
print(result10)
result11 = hello.split() # kelimeleri split etti
print(result11)
result12 = hello.replace("world","turkey")
print(result12)

# Ornek Uygulama -- STRING METODLARI :

result = " hello world "
result12 = "www.sadikturan.com"
result_strip = result.strip()
print(result)
print(result_strip)
result_split = result12.split(".")
print(result_split)
buyuk = result12.upper()
print(buyuk)
karakter = result.count("l")
print(karakter)
result_baslangıc= result.startswith(" hello") # başlangıç bu mu?
print(result_baslangıc)
result_find = result.find("worl") # index numarası döndürür
print (result_find)

# LİSTELER UYGULAMALAR
liste = ["BMW","Mercedes","Opel","Mazda"]
print (liste)
print (len(liste))
print (liste[0],liste[-1]) # ilk ve son elemanlar
liste[3] = "Toyota" # 4 ncü eleman Toyota yapıldı
print(liste)
print(liste[2])
liste[-1] = "Renault"
liste[-2] = "Totoya"
print(liste)

listedevarmı = "reno" in liste # -- in -- listede var mı?
print(listedevarmı) # True[var]/False [yok]veriyor 

print(liste [0:2]) # 0 dahil 2 hariç elemanları alır.
liste [-2:] = ["Onder","Atakan"] # -2 ve sonrasındaki elemanları listedeki bu elemanlar ile değiştirdik.
print(liste)
del liste[-1]
print(liste)



