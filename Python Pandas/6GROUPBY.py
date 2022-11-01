from statistics import mean
import pandas as pd
import numpy as np

df=pd.read_excel("personel.xlsx")
print(df)

#maaş toplamı
result=df["MAAS"].sum()

#yaş ortalaması
result=df["YAS"].mean()

#PAZARLAMA departmanında çalışanlar

result=df.groupby("DEPARTMAN").get_group("PAZARLAMA")
#AVCILARDA OTURAN PERSONELLER

result=df.groupby("ILCE").get_group("AVCILAR")

#SEMTE GÖRE MAAŞ ORTALAMALARI
result=df.groupby("DEPARTMAN")["MAAS"].mean()

#DEPARTMANLARDAKİ EN BÜYÜK YAŞ
result=df.groupby("DEPARTMAN")["MAAS"].max()

#MUHASEBE BÖLÜMÜNDE EN YÜKSEK MAAS ALAN KİŞİ
result=df.groupby("DEPARTMAN")["MAAS"].max().loc["MUHASEBE"]

#TÜM PERSONELİN DEPARTMANLARA GÖRE MAAŞ VE YAŞLARININ ORTALAMASI TOPLAMI MAX VE MİN DEĞERLERİ 

result=df.groupby("DEPARTMAN").agg(["mean","max","min"])

print(result)

