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
'''
# UYGULAMA :
a = input("Adınızı Soyadınızı Giriniz : ")
b = int(input("Doğum Yılını Giriniz : "))
c = int(input("Emeklilik Yaşını Giriniz : "))

def _age(b) :        # verilen yıla göre yası hesap eden _age fonksiyon
    yas = 2022 - b
    print( a + "yasınız" + yas + "dır.")
    return yas
    
def _emekliligekaçyılkaldı(b,a) :
    yas = _age(b)     # _age fonks ile yası hesaplıyoruz.
    süre = c - yas    # emeklilik yaşından yaşı cıkarıp kalan sure hesaplanır.
   
    if süre <= 0 :     # süre bittiyse:
        print( "{a} emekliliği hak etmiştir.")
    else :
        print( "{a} emekliliğe {süre} yıl kalmıştır.")
