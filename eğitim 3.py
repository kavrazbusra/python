mda = 'askim'
for x in mda:
    print(x)

if 6<=3:
    print("altı üçten küçük ya da eşittir")

elif 6>=3:
    print("altı üçe büyük ya da eşit")

else:
    print("bilmiyorum")

"""
for için değişken adı tanımladım. Sonra değişken yazdım, mda için x'i çağırdım. Her bir harf için döngü tamamlanmış oldu.
if için şart koydum. Şart bloğunu kontrol edip doğru olup olmadığına baktı. Yazılan değer yanlış olduğu için kodda tanımlanmadı.
elif için şart konuldu. Kontrol edildi ve doğru olduğu anlaşıldı. Kodu çalıştırdığımızda da bu değer çıktı.
else için else kısmına gelene kadar yukarda yazılan değerler kontrol edildi. Doğru yazılan alındı. Eğer her iki üst değer de yanlış olsaydı else için yazdığım kod bloğu tanımlanacaktı ve çalışacaktı.
"""

b="hello world"
print (b.upper())

a="HELLO WORLD"
print (a.lower())

a="hello world seni seviyorum"
list1=a.split(" ")
for x in list1:
    print(x)