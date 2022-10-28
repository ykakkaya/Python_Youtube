from tracemalloc import start


sayilar = [1,3,5,7,9,11,13,15,18,17]

#sayilar listesini while ile ekrana yazdırın.
# i=0
# while(i<len(sayilar)):

#     print(sayilar[i])
#     i+=1


#Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
# start=int(input("Başlangıç değerini giriniz: "))
# finish=int(input("Bitiş değerini giriniz: "))

# while(start<=finish):

#     if(start%2==1):

#         print(start)
#     start+=1


#Kullanıcıdan alacağınız sonsuz sayıyı ekranda sıralı bir şekilde yazdırın.-1 e basınca çık

numbers=[]
i=0

while( i==0 ):
    sayi=int(input("bir sayı giriniz çıkmak için -1 e basınız :"))

    if(sayi==-1):
        i=-1
    else:    
        numbers.append(sayi)
numbers.sort()
print(numbers)
