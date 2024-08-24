"""
("uskudar", "kadıköy", "besiktas", "ortakoy", "bagcilar")
yukardaki verilen verileri 1-3, baştan sona, -3/-1, 2-son,
yukardaki veride ortaköy yerine çekmeköy olarak değiştir ve ataşehir de ekle ve kadıköyü sil.
yukarıdaki verimizi değişkene aktar. İki değişken bir liste olacak. Bir tanesi de değişken, bir tanesi liste, bir tane değişken.
yukarıdaki verimizi for döngüsüyle tek tek ekrana çıktı ver. While döngüsüyle de ekrana çıktı ver.
"""

mytuple = ("uskudar", "kadıköy", "besiktas", "ortakoy", "bagcilar")
print(mytuple[1:3])
print(mytuple[0:5])
print(mytuple[-3:-1])
print(mytuple[2:5])
y = list(mytuple)
y[3] = "cekmekoy"
mytuple = tuple (y)
print(mytuple)
y = list(mytuple)
y.append ("atasehir")
mytuple = tuple (y)
print(mytuple)
y = list(mytuple)
y.remove ("kadıköy")
mytuple = tuple (y)
print(mytuple)
(x,y,z,d,b) = mytuple
(x,y, *z)= mytuple
print(x)
print(y)
print(z)
(x, *y, z) = mytuple
print(x)
print(y)
print(z)
for x in range(len(mytuple)):
    print(mytuple[x])
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i+=1



