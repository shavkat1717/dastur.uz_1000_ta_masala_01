a=float(input(" Burchakning radian qiymatini kiriting R = "))
pi=3.14159
if a>=0 and a<=2*pi:
    A=(a*180)/pi
    print("Ushbu R =",a," radian => A =",A," gradusga teng.")
else:
    print("Diqqatli bo'ling! Berilgan burchak [0;6.28318] oraliqda bo'lishi kerak")