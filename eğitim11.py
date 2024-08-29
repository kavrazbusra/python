"""
girilen bir sayının 0 ile 100 arasında olup olmadığını bulunuz

"""
number = float(input("bir sayı giriniz"))

if number<100 and number>0:
    print("girdiğiniz sayı 0 ile 100 arasındadır")

else:
    print("girdiğiniz sayı 0 ile 100 arasında değil")

"""
pozitif ve cift olduğunun kontrolü
"""
sayi = float(input("bir sayı giriniz"))

if sayi>0 and sayi%2==0:
    print("girdiğiniz sayı pozitif ve çifttir")

elif sayi>0 and sayi%2==1:
    print("girdiğiniz sayı pozitif ve tektir")

else:
    print("girdiğiniz sayı pozitif ve çift değildir")

"""
girilen üç sayıyı büyüklük olarak kaeşılaştırınız

"""

sayi1 = float(input("bir sayı giriniz"))
sayi2 = float(input("ikinci sayıyı giriniz"))
sayi3 = float(input("üçüncü sayıyı giriniz"))

if sayi1==sayi2 or sayi1==sayi3:
    print("sayi1, sayi2 ve sayi3'ten büyüktür")
    print("verdiğiniz sayılarda eşitlik vardır")


elif sayi2>sayi1 and sayi2>sayi3:
    print("sayi2, sayi1 ve sayi3'ten büyüktür")
elif sayi3>sayi1 and sayi3>sayi2:
    print("sayi3, sayi1 ve sayi2'den büyüktür")

else :
    print("sayi1, sayi2 ve sayi3'ten büyüktür")


"""
bir vize bir final olsun.Final notu 35 olma zorunluluğu, eğer 70 üzerinden alırsa da geçti yazacak. 
"""

"""
kullanıcıdan bir vize bir final notu al
ortalamasını bul
and or kullanarak şart bloklarıyla geçti kaldı yazdır

"""

vize = int(input("bir vize notu giriniz"))
final = int(input("bir final notu giriniz"))

if final>=35:
    if vize*0.4+final*0.6>=35:
        print("Geçti")
    elif final>=70:
        print("Geçti")
    else:
        print("Kaldı")
else:
    print("Kaldır")





if (final>=35 and (vize*0.4+final*0.6)>35) or final>=70:
    print("Geçti")
else:print("Kaldı") 


















