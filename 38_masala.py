A=int(input("Chiziqli tenglamaning birinchi koeffitsientini kiriting: A = "))
B=int(input("Chiziqli tenglamaning ikkinchi koeffitsientini kiriting: B = "))
print("Chiziqli tenglamamiz ", A, "x +", B," = 0 ko'rinishiga keldi.")
x=(-B)/A
if A!=0:
    print("Demak noma'lum sonimiz: x = ",x," ga teng ekan.")
else:
    print("Diqqatli bo'ling! A nolga teng bo'lmasin.")