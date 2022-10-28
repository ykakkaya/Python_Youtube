# bu bölümde karşılaşılabilecek string metedlarını inceleyeceğiz.
sentence=" bu programda python programlamaya ait temel kavramları öğreniyoruz."

#upper metodu tüm karakterleri büyük yapar.
sentence_upper=sentence.upper()
print(sentence_upper)
#lower tüm karakterleri küçük yapar.
sentence_lower=sentence.lower()
print(sentence_lower)
#title metodu her kelimenin baş harfini büyük yapar.
sentence_title=sentence.title()
print(sentence_title)
#capitilize metodu verilen string ifadenin sadece ilk harfini büyük yazar
name="yakup"
name_capitilize=name.capitalize()
print(name_capitilize)
#strip metodu string ifadenin en başında ve sonunda  boşluk varsa siler.Veri düzenlerken çok işe yarar.
sentence_strip=sentence.strip()
print(sentence_strip)
#split metodu da verilen değere göre string ifadeyi parçalar.
sentence_liste=sentence.split()
print(sentence_liste)
sentence_list2=sentence.split("a")
print(sentence_list2)
#replace ilk aldığı parametre yerine ikinci aldığı parametreyi yazar
sentence_replace=sentence.replace("bu","PYTHON")
print(sentence_replace)
#find metodu aradığımız bir kelimenin ilk harfinin index ini döner
sentence_find=sentence.find("ait")
print(sentence_find)
#count verilen ifadeden kaç tane olduğunu döner.
sentence_count=sentence.count("a")
print(sentence_count)