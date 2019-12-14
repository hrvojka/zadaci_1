x = int(input("Unesi broj 'psećih' godina: "))

if x < 3:
    y = x * 10.5
else:
    y = 21 + (x-2) * 4

print("Ljudskih godina: {0}".format(y))