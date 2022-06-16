# 5.Pythonda Koşul İfadeleri (IF and Else İLE Elif Clauses)


# Kod Bloğu -----> Koşul ------> True ise A yada False ise B Else ise C

if (kosul):
    True ise ......
elif (kosul):
    True ise .......
else (kosul artık False olmuş):
    False ise .......



username = input("Lütfen kullanıcı adı giriniz :").lower().strip()
password = input("Lütfen parola giriniz : ")

u_name = "ondersevik"
p_word = "Onder1997."

1 nci Yol :

isloggedin = (username == u_name) and (password == p_word)
# değişken = (True == True (T)) ve (True == True (T)) ...... T and T olursa True olur o zaman:
if isloggedin :  # yani yukarıdaki isloggedin koşulu True edildiyse alttakini bas diyor.
    print(" Hoşgeldiniz")
else :
    print("Bilgileriniz yanlıştır.")

 # 2 inci Yol : Bunu tercih edebiliriz.
if (username == u_name) :
    if (password == p_word) :
        print(" Hoşgeldiniz")
    else :
        print("Parolanız yanlıştır.")
else :
    print("Kullanıcı adınız yanlıştır.")


# UYGULAMA 1 : 

adı = input(" Adını Giriniz: ").upper().strip()
yas = int(input(" Yaşını Giriniz: "))
egt = input(" Eğitim bilgisini Giriniz: ")

if (yas>=18) : # eger true olursa,
    # İÇ BLOK YAPIYORUZ
    if ((egt == "lise") or (egt == "üniversite")) : # iç blok yaptık ve eger buda true olursa,
        print(f'{adı} {yas} yasında ve {egt} mezunu olup ehliyet alabilir.')
    else : # eğitim tutmadı ve false oldu.
        print(f'{adı}, {yas} yasında olup eğitim derecesi tutmadığı için ehliyet alamaz.')
    # İÇ BLOK BİTİYOR VE DIŞ BLOK BAŞLIYOR.
else:
    print(f'{adı}, {yas} yasında olup 18 yasının altında olduğu için ehliyet alamaz.')

# UYGULAMA 2 :

adı = input("Adınız Giriniz : ").upper().strip()
yaz1 = int(input(" 1 nci Yazılı notunu giriniz: "))
yaz2 = int(input(" 2 nci Yazılı notunu giriniz: "))
söz = int(input(" Sözlü notunu giriniz: "))

# değişken notun hesaplanması :
x = (yaz1 + yaz2 + söz ) / 3

if (x > 24) : # eger true olursa,
    # İÇ BLOK YAPIYORUZ
    if (x > 44) : # iç blok yaptık ve eger buda true olursa,
        if (x > 54) : # iç blok yaptık ve eger buda true olursa,
            if (x > 69) : # iç blok yaptık ve eger buda true olursa,
                if (x > 84) : # iç blok yaptık ve eger buda true olursa,
                    print(f'{adı}, {x} not ortalaması ile 5 notu almıştır.')
                else :    
                    print(f'{adı}, {x} not ortalaması ile 4 notu almıştır.')
            else :
                print(f'{adı}, {x} not ortalaması ile 3 notu almıştır.')
        else :
            print(f'{adı}, {x} not ortalaması ile 2 notu almıştır.')
    else :
        print(f'{adı}, {x} not ortalaması ile 1 notu almıştır.')
else:
    print(f'{adı}, {x} not ortalaması ile 0 notu almıştır.')



# UYGULAMALAR 1 : Girilen sayı değerinin 0-100 arasında olup olmadığı ?

x = int(input(" Bir sayı giriniz : ")) 

if (x <= 100 and x> 0) :
    print(f'Girdiğiniz {x} sayısı 0 (hariç) ve 100 (dahil) arasındadır.')
else :
    print(f'Girdiğiniz {x} sayısı 0 (hariç) ve 100 (dahil) arasında değildir.')

# UYGULAMALAR 2 : Girilen sayı pozitif çift sayımıdır ?

x = int(input(" Bir sayı giriniz : ")) 

if (x % 2 == 0 and x>= 0) :
    print(f'Girdiğiniz {x} sayısı pozitif çift sayıdır.')
else :
    print(f'Girdiğiniz {x} sayısı pozitif çift sayı değildir.')
    

# UYGULAMALAR 3 : Eposte ve Parola bilgileri ile giriş kontrolu yapılması ?

e = "osevik75@gmail.com"
p = "Onder1997."

eposta = input(" E-posta adresini giriniz: ").lower().strip()
parola = input(" Parolayı giriniz: ").strip()

if ( eposta == e) : # Unutma burada True False için == olacak .. yanlış yazıp = yapıyorsun ?????
    if ( parola == p) :
        print(f' {eposta} e-posta adresiniz ve parola bilgileriniz doğrudur. Giriş başarılıdır.')
    else :
        print(f'parolanız yanlıştır.')
else :
    print (f'{e} e-posta adresiniz yanlıştır.')


# UYGULAMA 3 Hangi sayı buyuktur?

a = int(input(" A sayısını giriniz : ")) 
b = int(input(" B sayısını giriniz : ")) 
c = int(input(" C sayısını giriniz : ")) 

if (a > b and a > c) :
    print(f'Girdiğiniz {a} sayısı {b} ve {c} sayısından büyüktür.')
elif (b > c) :
    print(f'Girdiğiniz {b} sayısı {a} ve {c} sayısından büyüktür.')
else :
    print(f'Girdiğiniz {c} sayısı {a} ve {b} sayısından büyüktür.')
    

# UYGULAMA 3 Hangi sayı buyuktur?

a = int(input(" Vize 1 notunu giriniz : ")) 
b = int(input(" Vize 2 notunu giriniz : ")) 
c = int(input(" Final notunu giriniz : ")) 

x = ((a+b)/2)*0.60 + c*0.40

if (c>=70):
    print (f'Final sınav notunuz {c} yeterli olup sınıfı geçtiniz.')
elif (x >=50  and c>=50) :
    print(f'Not ortalamınız {x} [baraj notu :50] ve final sınav baraj notu {c} yeterli olup [ baraj notu : 50 ] sınıfı geçtiniz.')
else :
    print(f'Sınıfta kaldınız.')
    
