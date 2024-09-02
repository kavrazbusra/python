sayilar = [1,3,5,7,9,12,19,21]

"""
sayilar listesini while ile ekrana yazdırın
Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
1-100 arasındaki sayıları azalan şekilde yazdırın
Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız
**ürün sayısını kullanıcıya sorun
**dictionary listesi (name, price) şeklinde olsun
**ürün ekleme işlemi bittiğinde ürünler, ekranda while ile listeleyin
"""

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

baslangic = int(input('baslangic değerini giriniz'))
bitis = int(input('bitis değerini giriniz'))

i = baslangic
while i < bitis:
    i += 1
    if (i % 2 ==1):
        print(i)

i = 100
while i > 0:
    print(i)
    i -= 1


numbers = []
i = 0
while i<5:
    sayi = int(input('bir sayı giriniz'))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)


urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))
i = 0

while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price' : price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')