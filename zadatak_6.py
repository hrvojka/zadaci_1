x = int(input("Unesi broj 'psećih' godina: "))
n=0
n1=0
y=0
# if x < 3:
#     y = x * 10.5
# else:
#     y = 21 + (x-2) * 4
#
# print("Ljudskih godina: {0}".format(y))

for n in range(x):
    if n < 2:
        n += 1
        x = n*10.5
    else:
        n1 = n1 + 1
        y = n1*4
print("Ljudskih godina: " + str(x+y))