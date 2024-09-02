sayilar = [1,3,5,7,9,12,19,21]

"""
sayilar listesindeki hangi sayılar 3'ün katıdır?
"""

for sayi in sayilar:
    if (sayi%3==0):
        print(sayi)

"""
sayilar listesinde sayıların toplamı kaçtır?
"""

toplam = 0
for sayi in sayilar:
    toplam += sayi
print('toplam: ' ,toplam)

"""
sayilar listesindeki tek sayıların karesini alınız
"""

for sayi in sayilar:
    if (sayi & 2 == 1):
        print(sayi ** 2)

sehirler = ['kocaeli' , 'istanbul' , 'ankara' , 'izmir' , 'rize']

"""
Şehirlerden hangileri en fazla 5 karaktere sahiptir ?
"""

for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)

