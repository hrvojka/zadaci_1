a = int(input("Unesi dužinu prve stranice: "))
b = int(input("Unesi dužinu druge stranice: "))
c = int(input("Unesi dužinu treće stranice: "))

if a != b != c != a:      # ako nešto djeluje suvišno ne znači da je tako :)
    message = "Trokut je raznostraničan.."
elif a == b == c:
    message = "Trokut je jednakostraničan.."
else:
    message = "Trokut je jednakokračan.."
print(message)