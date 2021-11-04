a=int(input(" Burchakning gradus qiymatini kiriting A = "))
pi=3.14159
if a>=0 and a<=360:
    R=(pi/180)*a
    print("Ushbu A =",a," gradus => R =",R," radianga teng.")
else:
    print("Diqqatli bo'ling! Berilgan burchak [0;360] oraliqda bo'lishi kerak")