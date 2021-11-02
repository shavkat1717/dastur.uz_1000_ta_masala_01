x1=float(input("Tekislikdagi nuqtaning birinchi X uchi koordinatalarini kiriting x1 = "))
y1=float(input("Tekislikdagi nuqtaning birinchi Y uchi koordinatalarini kiriting y1 = "))
x2=float(input("Tekislikdagi nuqtaning ikkinchi X uchi koordinatalarini kiriting x2 = "))
y2=float(input("Tekislikdagi nuqtaning ikkinchi Y uchi koordinatalarini kiriting y2= "))
l=(((x2-x1)**2)+((y2-y1)**2))**(1/2)

print(f" Koordinatalar ({x1};{y1}) va  ({x2};{y2}) ")
print(f"Tekislikdagi ushbu ikki nuqta o'rtasidagi masofa L = ",l)