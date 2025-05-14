x = int(input("nachalnaya summa vklada"))
p = int(input("procenty po vkladu"))
z = int(input("nujnaya summa vklada"))
y = int (input("tekushaya summa vklada"))
t = int(input("kolichestvo let vklada"))
while (z > y):
    t = t + 1
    y = y + 1
    y = x * p * t

print(t)




    