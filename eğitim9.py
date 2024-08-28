vize1 = int(input("vize notu gir:"))
vize2 = int(input("diğer bir vize notunu gir:"))
final = int(input("final notu gir:"))
result = (vize1*0.3)+(vize2*0.3)+(final*0.4)
if result>=50:
    print("gecti")
else :
    print("kaldı")