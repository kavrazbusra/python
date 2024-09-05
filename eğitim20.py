"""
Bir tane veri listem olacak ve sayılardan oluşacak. Bu içindeki verilerin aritmetik ortalamasını bul.
Sonra her veriyi aritmetik ortalamadan çıkart. Bu farkları, farklı bir listeye aktaracaksın.
Bulunan farkların her birinin karesini alıp toplayacaksın. Kaç veri varsa bunun bir eksiğini biraz önce bulduğum toplama böleceksin.
Sonra da bunun karekökünü alacaksın.

"""

import math
mylist = [1,3,5,7,9]

aritmetikOrtalama = sum(mylist) / len(mylist)

farklar = [ x - aritmetikOrtalama for x in mylist]

farklarinKaresi = [fark ** 2 for fark in farklar]

toplam = sum(farklarinKaresi)

ourlist = len(mylist) - 1

varyans = toplam / ourlist

standartSapma = math.sqrt(varyans)

print(f"mylist'deki verilerin standart sapması : {standartSapma}")





