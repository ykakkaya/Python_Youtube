#def funcName(args):


#gönderilen ifadenin karesini ekrana basalım.

# def kareAl(sayi):
#     print(sayi**2)

# kareAl(5)


#verilen bir sayının 5 fazlasını döndüren bir method yazalım

# def sayiEkle(sayi):
    
#     return sayi+5

# a=sayiEkle(10)
# print(a)


#verilen bir sayının 5 fazlasını yazdıran bir method yazalım
# def sayiEkle2(sayi):

#     print(sayi+5)

# sayiEkle2(10)

#Gönderilen bir kelimeyi belirtilen kez ekrana yazdıran fonksiyonu yazın. 

# def kelimeYaz(kelime,adet):
#     print(kelime*adet)

# kelimeYaz("yakup ",5)


numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  

#aldığı listedeki tek sayıları geri döndüren metodu yazalım

def tekSayiBul(liste):
    tek=[]
    for item in numbers:

        if(item%2==1):

            tek.append(item)
    return tek

a=tekSayiBul(numbers)
print(a)








