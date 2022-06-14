# 5.Pythonda Koşul İfadeleri (IF and Else Clauses)

'''
Kod Bloğu -----> Koşul ------> True ise A yada False ise B Else ise C

if (kosul):
    True ise ......

'''

from imp import PY_CODERESOURCE


username = input("Lütfen kullanıcı adı giriniz :").lower().strip()
password = input("Lütfen parola giriniz : ")

u_name = "ondersevik"
p_word = "Onder1997."

''' 1 nci Yol :

isloggedin = (username == u_name) and (password == p_word)
# değişken = (True == True (T)) ve (True == True (T)) ...... T and T olursa True olur o zaman:
if isloggedin :  # yani yukarıdaki isloggedin koşulu True edildiyse alttakini bas diyor.
    print(" Hoşgeldiniz")
else :
    print("Bilgileriniz yanlıştır.")

''' # 2 inci Yol : Bunu tercih edebiliriz.
if (username == u_name) :
    if (password == p_word) :
        print(" Hoşgeldiniz")
    else :
        print("Parolanız yanlıştır.")
else :
    print("Kullanıcı adınız yanlıştır.")
