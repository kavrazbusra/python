"""
Gönderilen kelimeyi ekranda belirtilen kez ekranda gösteren fonksiyonu yazın.
Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu hazırlayınız.
Gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.
Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde oluşturunuz.

"""

def yazdir(kelime, adet):
    print(kelime * adet)
yazdir ('Merhaba/n', 10)



def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)

    return liste
result = listeyeCevir(10,20,30, 'Merhaba')
print(result)



def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1 :
            for i in range (2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
sayi1 = int(input('sayi1 : '))
sayi2 = int(input('sayi2 : '))
asalSayilariBul(sayi1, sayi2)




def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2, sayi):
        if (sayi % 1 == 0):
            tamBolenler.append(i)
    return tamBolenler
print(tamBolenleriBul(20))