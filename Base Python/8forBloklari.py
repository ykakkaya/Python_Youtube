sayilar = [1,3,5,7,9,11,13,15,17,18,19]

# Sayilar listesindeki hangi sayılar 3'ün katıdır

# for item in sayilar:
#     if(item %3==0):
#         print(item)

#Sayilar listesinde sayıların toplamı
# toplam=0
# for item in sayilar:
#     toplam+=item
# print(toplam)


#Sayilar listesindeki tek sayıların karesini alınız

# for item in sayilar:
#     if(item %2==1):
#         print(item**2)


urunler = [
    {'name':'iphone11', 'price': 14000 },
    {'name':'iphone12', 'price': 15000 },
    {'name':'iphone13', 'price': 18000 },
    {'name':'iphone14', 'price': 23000 }
]

# 5- Ürünlerin fiyatları toplamı nedir ?
# toplam=0
# for item in urunler:
#     toplam+=item["price"]
# print(f"ürünlerimizin toplam fiyatı {toplam}")


# 6- Ürünlerden fiyatı en fazla 15000 olan ürünleri gösteriniz ?

for item in urunler:
    if(item["price"]<=15000):
        print(f"{item['name']} ürünümüzün fiyatı  {item['price']}")