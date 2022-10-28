# {key: value} şeklinde yazılır.

plakalar={34:"istanbul",35:"izmir",38:"kayseri",1:"adana"}
print(plakalar)
#dictionary içinde dictionary tanımlamak ( öğrenci numarası adı soyadı telefonun olduğu dict.)

ogrenciler={1:{"ad":"ahmet","soyad":"kara","tel":123456},
2:{"ad":"ayşe","soyad":"ışık","tel":246813579},
3:{"ad":"mehmet","soyad":"kaya","tel":147258}}

#bir elemanın bilgilerine ulaşmak
print(ogrenciler[2])

#alt elemanın bilgilerine ulaşmak
print(ogrenciler[3]["ad"])
#key bilgilerine ulaşmak

print(ogrenciler.keys())
#value bilgilerine ulaşmak

print(ogrenciler.values())
#eleman eklemek
plakalar.update({6:"ankara"})
print(plakalar)
#eleman silmek

print(plakalar)

plakalar.pop(38)
print(plakalar)