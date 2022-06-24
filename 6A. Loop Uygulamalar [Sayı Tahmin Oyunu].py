# RASTGELE SAYI TAHMİN ETME OYUNU :
 
import random  # random modulu import ettik


# list = [1,2,3,4,5]
# print(random.random()) # 0 ile 1.0 float döner
# print(random.uniform(1,100)) # 1.0 ile 100.0 arasında float döner
# print(random.randint(1,100)) # 0 ile 1.0 integer döner
# print(random.shuffle(list)) # liste içinde değerleri karıştırır


y = random.randint(1,100) # 0 ile 1.0 integer döner. Y DEĞERİ WHİLE DIŞINDA OLDUĞU İÇİN HER DEFASINDA DEĞİŞMEZ.

h = 5 # hak sayısı 5 dir.
while h > 0 :    # h>0 koşulu olduğu sürece True döner ve döngü çalışır.
    h -= 1       # her defasında hakkımız 1 azalacak ..
    x = int(input(" Bir sayı tahmin ediniz:"))   # Tahmin edilecek sayı istenecek While döngüde her defasında alınacak
   

# TAHMİN DOĞRUYSA :

    if x == y :                                  # eğer true olursa döngü çalışır.
        print(" Tebrikler rastgele sayıyı -- {y}-- bildiniz")
        break                                    # while döngüden çıkmak için lazım yoksa while döner durur.

# TAHMİN AZ İSE:

    elif x < y :                                  # eğer true olursa döngü çalışır.
        print(" Rastgele sayıyıyı bilemediniz. Yukarı tahmin edin. ")
       
# TAHMİN FAZLA İSE :
    else :                                       
        print(" Rastgele sayıyıyı bilemediniz. Aşağı tahmin edin. ")
       
    if h == 0 :
        print (f" Hakkınız bitmiştir. Tutulan sayı ={y} dir. ")

