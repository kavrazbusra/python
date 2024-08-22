thislist = ["mercedes", "porsche", "lamborghini"]
print(thislist[1:3])
print(thislist[-2:-1])
thislist.insert(1,"wv")
thislist.append("volvo")
print(thislist)
mylist = ["banana", "strawberry", "cherry", "apple"]
mylist.extend((thislist))
print(mylist)

"""
önce thislist adında değişken adı verdim. 
2.sırada 1 indexten 3 indexe kadar çağırdım.
3.sırada ise -2 indeximden -1 indexime kadar çağırdım.
4.sırada 1 index yerine insert methodunu kullanarak wv stringi ekledim.
5.sırada append methodunu kullanarak volvo stringini listemin sonuna ekledim.
6.sırada tüm listemi çağırdım.
7.sırada farklı bir liste oluşturdum.
8.sırada oluşturuduğum listeme extend methodunu kullanarak iki listeyi birleştirdim.
9.sırada ise birleştirmiş olduğum iki listeyi çağırdım.
"""