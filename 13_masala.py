R1=float(input("Birinchi radiusni kiriting R1 = "))
R2=float(input("Ikkinchi  radiusni kiriting R2 = "))
pi=3.14159
S1=pi*R1**2
S2=pi*R2**2
S3=S1-S2
if R1>0 and R2>0 and R1>R2:
    print("Birinchi doiraning yuzasi S1 =", S1, "ga teng;")
    print("Ikkinchi doiraning yuzasi S2 =", S2,"ga teng;")
    print("Yuzalar ayirmasi S3 =", S3,"ga teng;")
else: 
    print("Birinchi doiraning yuzasi S1 =", S1, "ga teng;")
    print("Ikkinchi doiraning yuzasi S2 =", S2,"ga teng;")
    print("Yuzalar ayirmasi S3 =", -1*S3,"ga teng;")