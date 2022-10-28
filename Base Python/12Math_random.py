import math
import random


list=["python","ile","veri","bilimi","desleri",3,2,1]

# choice  listeden rastgele 1 eleman seçer

print(random.choice(list))

# sample verilen listeden rastgele belirtilen kadar eleman seçer

print(random.sample(list,3))

#randint belirtilen aralıkta int tipinde rastgele sayı üretir

print(random.randint(1,10))

#uniform belirtilen aralıkta float tipinde sayı üretir

print(random.uniform(1,5))

#ceil verilen değeri yukarı yuvarlar

print(math.ceil(6.76))

print(math.ceil(17.1))

#floor verilen değeri aşagıya yuvarlar

print(math.floor(6.76))

print(math.floor(17.1))

#sqrt verilen değerin karekökünü alır

print(math.sqrt(36))

print(math.sqrt(45))

#factorial verilen değerin faktoriyelini alır

print(math.factorial(5))

print(math.factorial(10))