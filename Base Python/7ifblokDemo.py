#database de kullanıcı adı ve parola bilgimiz var.username ve parola bilgileri ile giriş kontrolü yapma

username="yakup"
password="12345"

user=input("kullanıcı adınızı giriniz: ")
passw=input("şifrenizi giriniz: ")

if(username==user) & (password==passw):
    print("giriş başarılı")
else:
    print("hatalı giriş denemesi")


#kullanıcıdan boy ve kilo değerlerini al.buna göre vücut kitle endeksi hesapla .kilo/boyun karesi(vki)
    #0-18,4 zayıf
    #18,5-24,9 normal
    #25-29,9 fazla kilolu
    #30-34,9 obez

boy=int(input("boyunuzu giriniz cm olarak: "))
kilo=int(input("kilo değerinizi giriniz: "))

vki=kilo/(boy**2)

if(vki>0)&(vki<=18.4):
    print(f"zayıf vki indeksi: {vki}")
elif(vki>18.4)&(vki<=24.9):
    print(f"normal vki indeksi: {vki}")
elif(vki>24.9)&(vki<=29.9):
    print(f"fazla kilolu vki indeksi: {vki}")
elif(vki>29.9)&(vki<=34.9):
    print(f"obez vki indeksi: {vki}")