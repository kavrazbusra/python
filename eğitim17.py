"""
iki tane liste oluştur ve ziple. Bu zipi aç.
For içinde ıf else kullanarak break ve continues ile ilgili kod yaz.
"""


list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
togetherlist = zip(list1, list2)

print(list(togetherlist))

numbers = range(0, 100)
for num in numbers :
    if num == 50:
        break

    elif (num%2==1):
        print(num)
    else:
        continue

