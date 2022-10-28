#python veri yapılarından listeleri inceleyelim.
#yeni bir liste oluşturmak
liste1=[1,2,3,4,5,6]
liste2=[10,9,8,7]
#verilen listeleri + ile birleştirebiliriz.
liste3=liste1+liste2
print(liste3)
#liste içinde liste saklamak
liste_inner=[liste1,liste2]
print(liste_inner)
#alt liste elemanına ulaşmak için
print(liste_inner[0])
print(liste_inner[0][3])
#listenin eleman sayısını bulmak
print(len(liste3))
#listenin ilk ve son elemanına ulaşmak
print(liste3[0])
print(liste3[-1])
#bir elemanın listede olup olmadığını aramak
print(5 in liste3)
print(18 in liste3)
#listenin belirli aralıktaki elemanlarına ulaşmak
print(liste3[1:5])
#listeye eleman eklemek
liste3.append(12)
print(liste3)
#listeden eleman silmek
liste3.remove(1)
print(liste3)
#listenin isteninlen index ine eleman eklemek
liste3.insert(3,45)
print(liste3)
#bir listeyi tersten yazdırma.
liste3.reverse()
print(liste3)
#bir listeyi sıralama
liste3.sort()
print(liste3)
#listenin tüm elemanlarını silme

liste3.clear()
print(liste3)