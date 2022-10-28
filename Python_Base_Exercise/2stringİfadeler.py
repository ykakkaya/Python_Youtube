#string ifadelerin birleştirilmesi

name="yakup"
surname="akkaya"
ad_soyad=name+" "+surname
print(ad_soyad)
sentence="bu programda python programlamaya ait temel kavramları öğreniyoruz."
#bazı python fonksiyonlarının kullanımı.
#cümlemizin tamamı:
print(sentence)
#cümlemizin uzunluğu:
print(len(sentence))
#cümlenin ilk karakteri:
print(sentence[0])
#cümlenin 5. karakteri:
print(sentence[4])
#cümlenin son karakteri:
print(sentence[-1])
#cümlenin 4. karakteri ile 14. karakteri arası:
print(sentence[3:13])
#baştan 10. karaktere kadar:
print(sentence[0:10])
print(sentence[:10])
#3. karakterden 38. karaktere kadar 1 er atlayarak
print(sentence[3:38:2])
#stringleri parametreleri girerek birleştirme .format ile
print("{0} ismli kişinin soyadı {1} dır".format(name,surname))
#f string formatlama yöntemi
print(f"{name} isimli kişinin soyadı {surname} dir.")
