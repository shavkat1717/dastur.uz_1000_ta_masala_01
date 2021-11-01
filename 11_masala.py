a=int(input("Birinchi  sonni kiriting a = "))
b=int(input("Ikkinchi  sonni kiriting b = "))
if a!=0 and b!=0:
    print("Ikkala sonning yig'indisi =", a+b,"ga teng;")
    print("Ikkala sonning ko'paytmasi =", a*b,"ga teng;")
    if a>=0:
        print("Birinchi sonning moduli =", a,"ga teng;")
    else:
        print("Birinchi sonning moduli =", -1*a,"ga teng;")
    if b>=0:
        print("Ikkinchi sonning moduli =", b,"ga teng.")
    else:
        print("Ikkinchi sonning moduli =", -1*b,"ga teng;")
else: print("Diqqatli bo'ling! Kiritilayotgan sonlar 0 (nol) ga teng bo'lmasligi kerak")