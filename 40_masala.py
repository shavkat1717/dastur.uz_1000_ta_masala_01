A1=int(input("chiziqli tenglamalar sistemasining birinchi koeffitsientini kiriting: A1 = "))
B1=int(input("chiziqli tenglamalar sistemasining birinchi koeffitsientini kiriting: B1 = "))
C1=int(input("chiziqli tenglamalar sistemasining birinchi koeffitsientini kiriting: C1 = "))
A2=int(input("chiziqli tenglamalar sistemasining ikkinchi koeffitsientini kiriting: A2 = "))
B2=int(input("chiziqli tenglamalar sistemasining ikkinchi koeffitsientini kiriting: B2 = "))
C2=int(input("chiziqli tenglamalar sistemasining ikkinchi koeffitsientini kiriting: C2 = "))


D=A1*B2-A2*B1
if D!=0:
    x=(C1*B2-C2*B1)/D
    y=(A1*C2-A2*C1)/D
    print("Chiziqli tenglamalar sistemasining yechimlari: x = ",x," y =", y," ga teng ekan.")
else:
    print("Xato: D = 0; Nolga bo'lish mumkin emas!")