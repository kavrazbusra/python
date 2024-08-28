"""
kullanıcıdan gelen sayının tek mi çift mi olduğunu bul.
"""

variables1 = int(input("bir sayı giriniz"))
if variables1%2==0:
    print("cevap çifttir")
else :
    print("cevap tektir")

"""
kullanıcıdan gelen sayı negatif mi pozitif mi bul.

"""

kodumundegiskeni = int(input("bir sayı giriniz"))
if kodumundegiskeni<0:
    print("cevap negatiftir")
else :
    print("cevap pozitiftir")


"""
gmail python@gmail.com olsun, parola ise 12345

"""

while True :
    salakkod = str(input("bir gmail hesabı giriniz"))
    malkod = str(input("bir şifre giriniz"))
    if salakkod==str("python@gmail.com") and str("12345")==malkod:
        print("hesaba giriş yaptınız")
        exit()
    else :
        print("hesaba giriş yapamadınız")
