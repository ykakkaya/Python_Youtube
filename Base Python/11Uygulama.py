import random

number=random.randint(0,100)

start=True
sayac=1

while(start):
    
    tahmin=int(input("tahmininizi giriniz: "))

    if(tahmin==number):
        print(f" doğru tahmin ettiniz.sayımız: {number}. deneme sayınız: {sayac}")
        start=False
    
    elif(tahmin<number):

        print("daha büyük bir sayı deneyiniz")
        sayac+=1

    elif(tahmin>number):

        print("daha küçük bir sayı deneyiniz")
        sayac+=1