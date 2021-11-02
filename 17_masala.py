A=float(input("Sonlar o'qidagi birinchi nuqtani kiriting A = "))
B=float(input("Sonlar o'qidagi ikkinchi nuqtani kiriting B = "))
C=float(input("Sonlar o'qidagi uchinchi nuqtani kiriting C = "))
AC=C-A
BC=C-B
L=AC+BC
if AC>=0:
    print("AC kesmaning uzunligi AC = ", AC," ga teng.")
if AC<0:
    print("AC kesmaning uzunligi AC = ", -1*AC," ga teng.")
if BC>=0:
    print("BC kesmaning uzunligi BC = ", BC," ga teng.")
if BC<0:
    print("BC kesmaning uzunligi BC = ", -1*BC," ga teng.")
if L>=0:
    print("AC va BC kesmalar yig'indisi L= ", L, " ga teng.")
if L<0:
    print("AC va BC kesmalar yig'indisi L= ", -1*L, " ga teng.")