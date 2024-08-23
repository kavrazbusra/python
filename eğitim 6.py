"""
while döngüsü oluştur 1'den 5'e kadar gidecek. 5 de dahil ve her döngü döndüğünde bir tane boş listeye her döndüğünde append etsin.
bir tane liste oluştur, oluşturduğun listede for döngüsüne sok ve şart bloğu kullanarak verdiğim listenin içinden a harfini bulup boş listeye atıp ekrana çıktısını ver.
("dogukan", "busra", "mehmet", "ozum", "aysegul", "basak", "melih", "nuh", "mircan")
yukardaki listenin sort'lu halini ekrana çıktı ver ve tersten sıralanmış halini ver.
bu listeyi üç farklı yolla kopyalama yap.
"""

mylist = []
i=1
while i<6:
    mylist.append(i)
    i=i+1
print(mylist)
ourlist = []
thislist = ["dogukan", "busra", "mehmet", "ozum", "aysegul", "basak", "melih", "nuh", "mircan"]
for x in thislist:
    if "a" in x:
        ourlist.append(x)
print(ourlist)
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
list1 = thislist.copy()
list2 = list(thislist)
list3 = thislist[:]
print(list1)
print(list2)
print(list3)


