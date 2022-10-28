import numpy as np

# 1- (1,15,3,17,6) değerlerine sahip numpy dizisi oluşturunuz.

result=np.array([1,15,3,17,6])


# 2- (20-25) arasındaki sayılarla numpy dizisi oluşturunuz.

result=np.arange(20,25)

# 3- (30-72) arasında 4'er 4'er artarak numpy dizisi oluşturunuz.


result=np.arange(30,72,4)

# 4- 5 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

result=np.zeros(5)


# 5- 7 elemanlı birlerden oluşan bir dizi oluşturunuz.

result=np.ones(7)

# 6- (0-100) arasında eşit aralıklı 4 sayı üretin.

result=np.linspace(0,100,4)

# 7- (10-30) arasında rastgele 3 tane tamsayı üretin.

result=np.random.randint(10,30,3)

# 8- [0 ile 1] arasında 5 adet sayı üretin.

result=np.random.rand(5)

#9- [-1 ile 1] arasında 5 adet sayı üretin.

result=np.random.randn(5)

# 10- (3x5) boyutlarında (-20 ve 50) arasında rastgele bir matris oluşturunuz.

matris=np.random.randint(-20,50,15).reshape(3,5)
print(matris)

# 11- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?

print(f"satır toplam: {matris.sum(axis=1)}")
print(f"sütun toplam: {matris.sum(axis=0)}")

# 12- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?

print(matris.max())
print(matris.min())
print(matris.mean())

# 13- Üretilen matrisin en büyük değerinin indeksi kaçtır ?


print(matris.argmax())

# 14- Üretilen matrisin ilk satırını seçiniz.

print(matris[0])

# 15- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?

print(matris[1][2])
# 16- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.

print(matris[:,0])
# 17- Üretilen matrisin her bir elemanının karesini alınız.
print(matris**2)

# 18- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? 
print(matris)
filter=(matris%2==0)&(matris>0)
print(matris[filter])