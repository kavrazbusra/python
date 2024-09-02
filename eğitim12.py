"""
kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
ehliet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
"""

isim = input('bir isim giriniz')
yas = int(input('bir yaş giriniz'))
egitim = input('eğitim durumunu giriniz')

if (yas>=18):
    if (egitim=='lise' or egitim=='üniversite'):
        print('ehliyet alabilirsiniz.')
    else:
        print('ehliyet alamazsınız eğitim durumunuz yetersiz')
else:
    print('ehliyet alamazsınız yaşınız tutmuyor.')


"""
kullanıcıdan 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığını karşılık gelen not bilgisini yazdır.
0-24 ==> 0
25-44 ==> 1
45-54 ==> 2
55-69 ==> 3
70-84 ==> 4
85-100 ==> 5
"""

yazili1 = float(input('birinci yazılı notunu giriniz'))
yazili2 = float(input('ikinci yazılı notunu giriniz'))
sozlu = float(input('sözlü notu girini'))

ortalama = (yazili1 + yazili2 + sozlu)/3

if (ortalama>=0) and (ortalama<25):
    print(f'ortalamanız: {ortalama} notunuz: 0')
elif (ortalama >= 25 ) and (ortalama<45):
    print(f'ortalamanız: {ortalama} notunuz: 1')
elif (ortalama >= 45 ) and (ortalama<55):
    print(f'ortalamanız: {ortalama} notunuz: 2')
elif (ortalama >= 55 ) and (ortalama<70):
    print(f'ortalamanız: {ortalama} notunuz: 3')
elif (ortalama >= 70 ) and (ortalama<85):
    print(f'ortalamanız: {ortalama} notunuz: 4')
elif (ortalama >= 85 ) and (ortalama<=100):
    print(f'ortalamanız: {ortalama} notunuz: 5')
else:
    print('yanlış bilgi girdiniz.')