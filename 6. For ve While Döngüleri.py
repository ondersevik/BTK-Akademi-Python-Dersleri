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

'''
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
