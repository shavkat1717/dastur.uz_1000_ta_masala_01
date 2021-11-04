x=float(input("qayiq tezligini kiriting: Vq = "))
y=float(input("oqim tezligini kiriting: Vo = "))
a=float(input("qayiqning oqim bo'yicha yurgan vaqtini kiriting: t1 = "))
b=float(input("qayiqning oqimga qarshi yurgan vaqtini kiriting: t2 = "))
if x>y:
    S=(x+y)*a+(x-y)*b
    print("Qayiq jami: S=", S, " yo'l yurgan.")
else:
    print("Diqqatli bo'ling! Qayiq tezligi oqim tezligidan katta bo'lishi kerak...")