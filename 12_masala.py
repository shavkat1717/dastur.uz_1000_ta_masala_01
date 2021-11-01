a=float(input("Birinchi katetni kiriting a = "))
b=float(input("Ikkinchi  katetni kiriting b = "))
c=(a**2+b**2)**(1/2)
if a>0 and b>0:
    print("Ushbu to'g'ri burchakli uchburchakning gipotenuzasi c =", c, "ga teng;")
    print("Ushbu to'g'ri burchakli uchburchakning perimetri esa P =", a+b+c,"ga teng;")
else: print("Diqqatli bo'ling! Uchburchakning tomoni nomusbat bo'lmaydi...")