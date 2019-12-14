a = int(input("Unesi dužinu prve stranice: "))
b = int(input("Unesi dužinu druge stranice: "))
c = int(input("Unesi dužinu treće stranice: "))
d = 0

if a != b != c:
    d = "Trokut je raznostraničan.."
elif a == b == c:
    d = "Trokut je jednakostraničan.."
else:
    d = "Trokut je jednakokračan.."
print(d)