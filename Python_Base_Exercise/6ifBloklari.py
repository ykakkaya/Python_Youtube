#if(şart):
#   doğru ise yapılacaklar
#elif (yeni şart):
#    yapılacaklar
#else:
#    yapılacaklar

#girilen iki sayıdan büyük olan

# number1=int(input("birinci sayıyı giriniz: "))
# number2=int(input("ikinci sayıyı giriniz: "))

# if(number1>number2):
#     print(f"{number1} sayısı {number2} sayısından büyüktür.")
# else:
#     print(f"{number2} sayısı {number1} sayısından büyüktür.")


#girilen bir sayının tekmi çift mi olduğunu yazdır

# sayi=int(input("bir sayı giriniz: "))

# if(sayi%2==0):
#     print(f"{sayi} çifttir.")
# else:
#     print(f"{sayi} tektir.")



#kullanıcıdan 1 vize(%40) 1 final notu(%60) alınsın. ortalama 50 üstü ise geçer yoksa kalsın

vize=int(input("vize notunu giriniz. "))
final=int(input("final notunu giriniz. "))

ort=(vize*0.40)+(final*0.60)

if(ort>50):
    print(f"dersi geçtiniz ortalamanız:  {ort}")
else:
    print(f"dersten kaldınız ortalamanız:  {ort}")





