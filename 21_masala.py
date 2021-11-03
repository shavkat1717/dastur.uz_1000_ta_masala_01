x1=float(input("Uchburchakning birinchi X uchi koordinatalarini kiriting x1 = "))
y1=float(input("Uchburchakning birinchi Y uchi koordinatalarini kiriting y1 = "))
x2=float(input("Uchburchakning ikkinchi X uchi koordinatalarini kiriting x2 = "))
y2=float(input("Uchburchakning ikkinchi Y uchi koordinatalarini kiriting y2 = "))
x3=float(input("Uchburchakning ikkinchi X uchi koordinatalarini kiriting x3 = "))
y3=float(input("Uchburchakning ikkinchi Y uchi koordinatalarini kiriting y3 = "))
a=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
b=(((x3-x1)**2)+((y3-y1)**2))**(1/2)
c=(((x3-x2)**2)+((y3-y2)**2))**(1/2)
x=(a+b+c)/2
P=2*x
S=(x*(x-a)*(x-b)*(x-c))**(1/2)
print("Uchburchakning perimetri P =", P)
print("Uchburchakning yuzasi  S =", S)