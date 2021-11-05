A=int(input("Kvadrat tenglamaning birinchi koeffitsientini kiriting: A = "))
B=int(input("Kvadrat tenglamaning ikkinchi koeffitsientini kiriting: B = "))
C=int(input("Kvadrat tenglamaning uchinchi koeffitsientini kiriting: C = "))
print("Chiziqli tenglamamiz ", A, "x*x +", B,"x +",C," = 0 ko'rinishiga keldi.")
D=B**2-4*A*C
if A!=0 and D>0:
    x=(-B+(D**(1/2)))/2*A
    y=(-B-(D**(1/2)))/2*A
    print("Demak kvadrat tenglamaning yechimlari: x1 = ",x," x2 =", y," ga teng ekan.")
else:
    print("Xato: A = 0 yoki D < 0")