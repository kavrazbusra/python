while True:
    a = int(input("lütfen bir sayı giriniz:"))
    b = int(input("ikinci sayıyı giriniz:"))
    if a>b:
        print("girilen en büyük değer", a)
    elif b>a:
        print("girilen en büyük değer", b)
    else :
        print("girilen iki değer eşittir")
        exit()